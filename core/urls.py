from django.urls import path
from . import views

urlpatterns = [
     path('hello/', views.hello ),
     path('tasks/', views.Tasks),
     path('user/', views.Users),
 ]
 