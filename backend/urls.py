from django.urls import path
from . import views

urlpatterns = [
	path('', views.api_details, name="api_details"),
	path('task-list/', views.get_all_tasks, name="get_all_tasks"),
	path('task-create/', views.create_task, name="create_task"),
	path('task-update/<int:pk>/', views.update_task, name="update_task"),
	path('task-delete/<int:pk>/', views.delete_task, name="delete_task"),
	path('task/<int:pk>/', views.get_task, name="delete_task"),
	
	
]