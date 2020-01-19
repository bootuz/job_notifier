from django.urls import path

from scraping import views

urlpatterns = [
    path('scrape/', views.scrape, name='scrape'),
]