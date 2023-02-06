from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('task_view/update/<int:id>/', views.update, name='update'),
    path('task_view/', views.task_view, name='task_view'),
    path('task_view/delete/<int:id>/', views.delete, name='delete'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
    # path('', views.TaskListView.as_view(), name='task_view'),
    # path('delete/<int:pk>/',  views.TaskDeleteView.as_view(), name='delete'),
    # path('detail/<int:pk>', views.TaskDetailView.as_view(), name='detail'),
    # path('edit/<int:pk>', views.TaskUpdateView.as_view(), name='edit'),
    # path('task_view', views.task, name='task_view'),
]