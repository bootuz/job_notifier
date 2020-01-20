from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from scraping import views
import os

urlpatterns = [
    path('index/', views.index, name='index'),
    path(f'{os.environ["TOKEN"]}', csrf_exempt(views.scrape), name='scrape'),
]