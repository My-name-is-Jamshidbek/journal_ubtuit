# news/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_list, name='news_list'),
    path('create/', views.create_news, name='create_news'),
    path('update/<int:pk>/', views.update_news, name='update_news'),
    path('delete/<int:pk>/', views.delete_news, name='delete_news'),
    path('detail/<int:pk>/', views.news_detail, name='news_detail'),
]
