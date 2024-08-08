from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_entry/', views.add_entry, name='add_entry'),
    path('add_goal/', views.add_goal, name='add_goal'),
]