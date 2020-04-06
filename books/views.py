from django.template.response import TemplateResponse

from .models import Book


def book_list_get(request):
    ctx = {
        "object_list": Book.objects.all()
    }
    return TemplateResponse(request, "books/book_list.html", context=ctx)
