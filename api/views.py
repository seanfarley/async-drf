from rest_framework.decorators import api_view
from rest_framework.response import Response

from books.models import Book
from .serializers import BookSerializer


@api_view(['GET'])
def book_api_view(request):
    books = Book.objects.all()
    bs = BookSerializer(books, many=True)
    return Response(bs.data)
