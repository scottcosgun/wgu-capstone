from django.core.management.base import BaseCommand
from recommender.utils import compute_book_similarity_matrix
from recommender.models import Book
import numpy as np
import pandas as pd

class Command(BaseCommand):
    help="Computes the cosine similarity matrix for all books in the database and stores it in similarity_matrix.npy"

    def handle(self, *args, **kwargs):
        books = Book.objects.all()
        books_data = pd.DataFrame(list(books.values()))

        # Count the total number of books in the dataset
        total_books = books_data.shape[0]
        print("\nTotal Number of Books:", total_books)

        # Check for duplicate rows
        duplicate_rows = books_data[books_data.duplicated()]

        # Count the occurrences of each unique book title
        book_title_counts = books_data['title'].value_counts()

        # Print the duplicate rows and unique book title counts
        print("Duplicate Rows:")
        print(duplicate_rows)

        print("\nBook Title Counts:")
        print(book_title_counts)

        similarity_matrix = compute_book_similarity_matrix(books_data)
        print("We're saving the similarity matrix with this shape: ", similarity_matrix.shape)
        np.save('similarity_matrix.npy', similarity_matrix)
        self.stdout.write(self.style.SUCCESS("Cosine similarity matrix computed and saved successfully."))