from django.urls import path
from .views import book_list_get


urlpatterns = [
    path('', book_list_get, name='home'),
]
