from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_necessity, name='create_necessity'),
    path('<int:necessity_id>/', views.read_necessity, name='read_necessity'),
    path('<int:necessity_id>/update/', views.update_necessity, name='update_necessity'),
    path('<int:necessity_id>/delete/', views.delete_necessity, name='delete_necessity'),
    path('list/', views.list_necessities, name='list_necessities'),  # Add this line
]
