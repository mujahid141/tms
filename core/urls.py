
from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
     path('toggle_task_complete/<int:task_id>/', views.toggle_task_complete, name='toggle_task_complete'),
    path('taks/', views.user_tasks, name='tasks'),
    path('', views.hello, name='home'),  # Add your home view here
]
