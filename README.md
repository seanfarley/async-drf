# Testing async views in django

Clone this repo and do the usual django dance:

``` shell
$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py createsuperuser
```

Then load some sample data:

``` shell
$ python manage.py loaddata books/fixtures/books.json
```

There are various branches to bookmark different points in the wsgi -> asgi
transition to help with debugging.
