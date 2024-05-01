from django.urls import path
from . import views



urlpatterns = [
    path('', views.TaskMenu , name='tasks'),
    path('add/', views.addTask, name='add-task'),
    path('show/<int:id>/', views.showTask, name='show-task'),
    path('delete/<int:id>/', views.deleteTask, name='delete-task'),
    path('category/<str:name>/', views.Task_category, name='category-task'),
    path('add_category/', views.add_category, name='add-category'),
]