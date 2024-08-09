from django.urls import path
from . import views

urlpatterns = [
    path('', views.progress, name='progress'),
    path('add_entry/', views.add_entry, name='add_entry'),
    path('add_goal/', views.add_goal, name='add_goal'),
    path('add_shortcut/', views.add_shortcut, name='add_shortcut'),
]