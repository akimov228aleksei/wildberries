from django.urls import path
from .views import ListArticles

urlpatterns = [
    path('articles/', ListArticles.as_view()),
]
