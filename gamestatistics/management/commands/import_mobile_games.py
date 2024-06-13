# mobile_games/management/commands/import_mobile_games.py
import csv
from django.core.management.base import BaseCommand
from gamestatistics.models import MobileGame

class Command(BaseCommand):
    help = 'Import mobile games data from CSV file into the database'

    def handle(self, *args, **options):
        self.import_mobile_games()
        self.stdout.write(self.style.SUCCESS('Successfully imported mobile games data'))

    def import_mobile_games(self):
        file_path = r'C:\Users\Admin\Downloads\mobile-games.csv'  # Use a raw string
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                game, created = MobileGame.objects.get_or_create(
                    name=row['Game Name'],
                    defaults={
                        'developer': row['Developer'],
                        'genre': row['Genre'],
                        'rating': row['Rating'],
                    }
                )
                if not created:
                    game.developer = row['Developer']
                    game.genre = row['Genre']
                    game.rating = row['Rating']
                    game.save()
