# gamestatistics/management/commands/import_steam_games.py
import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from gamestatistics.models import SteamGame


class Command(BaseCommand):
    help = 'Import Steam games data from CSV file into the database'

    def handle(self, *args, **options):
        self.import_steam_games()
        self.stdout.write(self.style.SUCCESS('Successfully imported Steam games data'))

    def import_steam_games(self):
        file_path = r'C:\Users\Admin\Downloads\games.csv\games.csv'  # Use your actual file path here
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    # Create or update the SteamGame entry
                    game, created = SteamGame.objects.get_or_create(
                        app_id=row['app_id'],
                        defaults={
                            'title': row['title'],
                            'date_release': row['date_release'],
                            'win': row['win'].lower() == 'true',
                            'mac': row['mac'].lower() == 'true',
                            'linux': row['linux'].lower() == 'true',
                            'rating': row['rating'],
                            'positive_ratio': int(row['positive_ratio']),
                            'user_reviews': int(row['user_reviews']),
                            'price_final': row['price_final'],
                            'discount': row['discount'],
                            'steam_deck': row['steam_deck'].lower() == 'true',
                        }
                    )
                    if not created:
                        # Update the existing entry if it already exists
                        game.title = row['title']
                        game.date_release = row['date_release']
                        game.win = row['win'].lower() == 'true'
                        game.mac = row['mac'].lower() == 'true'
                        game.linux = row['linux'].lower() == 'true'
                        game.rating = row['rating']
                        game.positive_ratio = int(row['positive_ratio'])
                        game.user_reviews = int(row['user_reviews'])
                        game.price_final = row['price_final']
                        game.discount = row['discount']
                        game.steam_deck = row['steam_deck'].lower() == 'true'
                        game.save()

                except (ValueError) as e:
                    return None

