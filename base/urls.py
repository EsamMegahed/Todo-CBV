from django.urls import path

from .import views



urlpatterns = [
    path('',views.TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',views.TaskDetail.as_view(),name='task_detail'),
    path('create_task/',views.TaskCreate.as_view(),name='task_create'),
    path('create_update/<int:pk>/',views.TaskUpdate.as_view(),name='task_update'),
]