from django.urls import path
from .views import index, developers_that_have_created_multiple_games, about_me, steam_games_under_10_and_positive

urlpatterns = [
    path('', index, name='index'),  # Root URL for the index page
    path('mobile/', developers_that_have_created_multiple_games, name='developers_that_have_created_multiple_games'),
    path('about_me/', about_me, name='about_me'),
    path('steam_games_under_10_and_positive/', steam_games_under_10_and_positive, name='steam_games_under_10_and_positive')
]
