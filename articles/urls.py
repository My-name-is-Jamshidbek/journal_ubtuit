from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.journal_list, name='list_journal'),
    path('<int:journal_id>/', views.journal_detail, name='journal_detail'),
    path('search/', views.search_articles, name='search_article'),
    path('my/', views.user_article_list, name='my_articles'),
    path('my/user/create-article/', views.create_article, name='create_article'),
    path('my/<int:article_id>/', views.article_detail, name='user_article_detail'),
    path('my/<int:article_id>/update/', views.update_article, name='user_article_update'),
    path('my/<int:article_id>/delete/', views.delete_article, name='user_article_delete'),
]
