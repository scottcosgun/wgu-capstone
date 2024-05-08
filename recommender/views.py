from django.shortcuts import render
from django import forms
import numpy as np
from .models import Book, CustomerSatisfaction
from django.http import JsonResponse

class RecommendBooksForm(forms.Form):
    book = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Enter a book title'}),
        label=''
        )

# Create your views here.
def index(request):
    if request.method == "POST":
        form = RecommendBooksForm(request.POST)
        books = Book.objects.all()
        book_titles = [book.title for book in books]
        if form.is_valid():
            book_title = form.cleaned_data["book"]
            recommended_books = get_recommendations(book_title)

            if recommended_books:
                # Calculate counts for similarity score categories to be used in pie chart
                very_high = sum(1 for book, score in recommended_books if score >= 50)
                high = sum(1 for book, score in recommended_books if 30 <= score < 50)
                medium = sum(1 for book, score in recommended_books if 20 <= score < 30)
                low = sum(1 for book, score in recommended_books if score < 20)

                # Pass through customer satisfaction values
                yes_count = CustomerSatisfaction.get_instance().yes_count
                no_count = CustomerSatisfaction.get_instance().no_count

                return render(request, "recommender/index.html", {
                    "form": form,
                    "recommended_books": recommended_books,
                    "very_high": very_high,
                    "high": high,
                    "medium": medium,
                    "low": low,
                    "yes_count": yes_count,
                    "no_count": no_count,
                    "books": book_titles,
                    "book_title": book_title
                })
            else:
                book_not_found = True
        else:
            book_not_found = False
    else:
        form = RecommendBooksForm()
        book_not_found = False
    books = Book.objects.all()
    book_titles = [book.title for book in books]
    return render(request, "recommender/index.html", {
        "form": RecommendBooksForm(),
        "books": book_titles,
        "book_not_found": book_not_found
    })

# Recommend books function
def get_recommendations(book_title):

    books = Book.objects.all()

    # Create a mapping of book titles to indices
    mapping = {book.title: index for index, book in enumerate(books)}
    
    if book_title in mapping:

        # Retrieve book index
        book_index = mapping[book_title]

        # Load similarity matrix
        similarity_matrix = np.load("similarity_matrix.npy")

        # Compute similarity scores and find similar books to recommend
        similarity_scores = similarity_matrix[book_index]
        similarity_scores_sorted_indices = np.argsort(similarity_scores)[::-1][1:16]
        similarity_scores_sorted_indices = similarity_scores_sorted_indices.tolist()
        recommended_books = [(books[index], round(similarity_scores[index] * 100, 2)) for index in similarity_scores_sorted_indices]

        # Retrieve recommended books from the database
        return recommended_books
    
    else:
        print(f"Error: {book_title} not found in the dataset.")
        return None


def submit_feedback(request):
    if request.method == "POST":
        response = request.POST.get("response")
        if response in ("yes", "no"):
            customer_satisfaction = CustomerSatisfaction.get_instance()
            if response == "yes":
                customer_satisfaction.yes_count += 1
            elif response == "no":
                customer_satisfaction.no_count += 1
            customer_satisfaction.save()
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"error": "Invalid response value"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=405)

def about(request):
    return render(request, "recommender/about.html")