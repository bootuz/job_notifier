from django.urls import path

from scraping import views
import os

urlpatterns = [
    path('index/', views.index, name='index'),
    path(f'{os.environ["TOKEN"]}', views.scrape, name='scrape'),
]