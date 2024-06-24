from django.db import models

# Create your models here.

class MobileGame(models.Model):
    name = models.CharField(max_length=100)
    developer = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    rating = models.FloatField()

    def __str__(self):
        return self.name
    
class SteamGame(models.Model):
    app_id = models.IntegerField(unique=True)
    title = models.TextField()
    date_release = models.DateField()
    win = models.BooleanField()
    mac = models.BooleanField()
    linux = models.BooleanField()
    rating = models.CharField(max_length=255)
    positive_ratio = models.IntegerField()
    user_reviews = models.IntegerField()
    price_final = models.DecimalField(max_digits=6, decimal_places=2)
    discount = models.DecimalField(max_digits=6, decimal_places=2)
    steam_deck = models.BooleanField()

    def __str__(self):
        return self.title