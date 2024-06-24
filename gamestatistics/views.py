from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MobileGame, SteamGame
from django.db.models import Q

def index(request):
    return render(request, 'index.html')


def developers_that_have_created_multiple_games(request):
    games = MobileGame.objects.all()

    context = {
        "games": games
    }

    return render(request, 'developers_that_have_created_multiple_games.html', context)


def about_me(request):
    return render(request, 'about_me.html')

def steam_games_under_10_and_positive(request):
    games_under_10 = list(SteamGame.objects
                          .filter(price_final__lte=9.99)
                          .filter(Q(rating="Positive") | Q(rating="Very Positive"))
                          .values(
                              "title",
                              "rating",
                              "user_reviews",
                              "price_final",
                              ))
    
    context = {
        "games": games_under_10
    }
    
    return render(request, 'steam_games_under_10_and_positive.html', context)