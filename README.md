# User Guide

## Prerequisites

Ensure that the following programs are installed on your computer:

1. A web browser (this application has been tested in Google Chrome and Safari)
2. Python 3
3. pip
4. numpy
5. pandas
6. scikit-learn
7. django
8. Your preferred IDE (I used Visual Studio Code)

## Setup Instructions

1. Unzip and open the project in your preferred IDE and navigate to the root directory of the project in the terminal window. The root directory is the `book_recommender` folder containing all contents of this project.

2. Run the following command in the terminal window of your IDE to create the cosine similarity matrix for the book recommender algorithm – this might take a minute or so:
    ```bash
    python3 manage.py create_similarity_matrix
    ```

3. Run the following command in the terminal window of your IDE:
    ```bash
    python3 manage.py runserver
    ```

4. In your web browser, copy `http://127.0.0.1:8000/recommender/` into the URL search bar to navigate to the book recommender application. This should take you to the home screen of the application.

5. Click on the input field that reads “Enter a book title.” Begin typing out a book title and choose your book from the drop-down list.
    > **Note:** This program is case sensitive. In this application, “To Kill A Mockingbird” is not the same as “To Kill a Mockingbird”

6. After selecting your book title from the drop-down list, click on the button that reads “Find recommendations!”

7. You should now see a table of 15 book recommendations with their corresponding similarity scores, a pie chart depicting the similarity score distributions of these 15 books, and a pie chart for the customer satisfaction results taken from our short survey in the bottom right. Feel free to share your feedback in that survey!

8. Each book title in the recommendations list is also a link. Clicking on a book title will open a new tab and direct you to the Goodreads page for that book.
