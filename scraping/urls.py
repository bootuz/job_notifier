from django.urls import path

from scraping import views

urlpatterns = [
    path('/', views.index, name='index'),
    path('scrape/', views.scrape, name='scrape'),
]