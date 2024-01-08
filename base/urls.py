from django.urls import path
from django.contrib.auth.views import LogoutView
from .import views



urlpatterns = [
    # authentication
    path('login/',views.CostomLoginView.as_view(),name='login'),
    path('logout/',views.CostomLogoutView.as_view(),name='logout'), 
    path('register/',views.RegisterPage.as_view(),name='register'), 

    # base urls 
    path('',views.TaskList.as_view(),name='tasks'),
    path('task/<int:pk>/',views.TaskDetail.as_view(),name='task_detail'),
    path('create_task/',views.TaskCreate.as_view(),name='task_create'),
    path('create_update/<int:pk>/',views.TaskUpdate.as_view(),name='task_update'),
    path('task_delete/<int:pk>/',views.TaskDelete.as_view(),name='task_delete'),
]