from django.urls import path
from .views import index, developers_that_have_created_multiple_games

urlpatterns = [
    path('', index, name='index'),  # Root URL for the index page
    path('mobile/', developers_that_have_created_multiple_games, name='developers_that_have_created_multiple_games'),
]
