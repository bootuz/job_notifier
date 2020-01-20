from django.urls import path

from scraping import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.scrape, name='scrape'),
]