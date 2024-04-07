from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.article_list, name='list_article'),
    path('my/', views.user_article_list, name='my_articles'),
    path('create-article/', views.create_article, name='create_article'),
    path('<int:article_id>/', views.article_detail, name='article_detail'),
    path('<int:article_id>/update/', views.update_article, name='article_update'),
    path('<int:article_id>/delete/', views.delete_article, name='article_delete'),
]
