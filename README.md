# intership003
Test work.
For greater compatibility, the application runs in docker
I wrote tests, but they are not complete
Of course, you still need to work with environment variables, authorization and authentication
...and much more...
for start:
```docker-compose up -d --build
   docker-compose exec web python manage.py migrate --noinput
   docker-compose exec web python manage.py createsuperuser
  http://127.0.0.0:8000/all_lessons/
  http://127.0.0.0:8000/product_lessons/<int:product_id>/
  http://127.0.0.0:8000/product_stats/<int:product_id>/
  

