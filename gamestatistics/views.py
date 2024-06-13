from django.shortcuts import render
from django.core.paginator import Paginator
from .models import MobileGame

def index(request):
    return render(request, 'index.html')

def developers_that_have_created_multiple_games(request):
    games = MobileGame.objects.all()

    context = {
        "games": games
    }
    return render(request, 'developers_that_have_created_multiple_games.html', context)