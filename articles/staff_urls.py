from django.urls import path, include
from . import staff_views as views

urlpatterns = [
    path('loaded/', views.loaded_articles, name='loaded_articles'),
    path('buying/', views.buying_articles, name='buying_articles'),
    path('reject/', views.rejected_articles, name='rejected_articles'),
    path('accepted/', views.accepted_articles, name='accepted_articles'),
    path('<int:article_id>/accept/', views.accept_article, name='accept_article'),
    path('<int:article_id>/reject/', views.reject_article, name='reject_article'),
    path('<int:article_id>/buying/', views.buying_article, name='buying_article'),
]
