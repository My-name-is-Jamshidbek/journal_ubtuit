from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='journals'),
    path('<int:pk>/', views.journal_detail, name='journal_detail'),  # Detail view for a single journal
    path('create/', views.journal_create, name='journal_create'),  # Create a new journal
    path('<int:pk>/update/', views.journal_update, name='journal_update'),  # Update an existing journal
    path('<int:pk>/delete/', views.journal_delete, name='journal_delete'),  # Delete a journal
   path('<int:pk>/create/', views.article_create, name='article_create'),  # Create a new article
    path('article/<int:pk>/update/', views.article_update, name='article_update'),  # Update an existing article
    path('article/<int:pk>/delete/', views.article_delete, name='article_delete'),  # Delete a article
]