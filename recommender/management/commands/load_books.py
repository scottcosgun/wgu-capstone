from django.core.management.base import BaseCommand
import csv
from recommender.models import Book

class Command(BaseCommand):
    help = 'Load book data from CSV file into the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file containing book data')

    def handle(self, *args, **kwargs):
        csv_file_path = kwargs['csv_file']
        self.delete_existing_books()
        self.import_data_from_csv(csv_file_path)
        
    def import_data_from_csv(self, csv_file_path):
        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                Book.objects.create(
                    title=row['Book'],
                    author=row['Author'],
                    description=row['Description'],
                    avg_rating=float(row['Avg_Rating']),
                    num_ratings=int(row['Num_Ratings'].replace(',', '')),
                    url=row['URL']
                )
    def delete_existing_books(self):
        Book.objects.all().delete()