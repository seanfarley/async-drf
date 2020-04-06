from django.urls import path
from .views import book_api_view


urlpatterns = [
    path('', book_api_view),
]
