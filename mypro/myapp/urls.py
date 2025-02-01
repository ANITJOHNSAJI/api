from django.contrib import admin
from django.urls import path,include
from . import views 

urlpatterns = [
    path('',views.add_todo,name='index'),
    path('display',views.get_todos,name='display'),
    path('delete/<int:id>',views.delete_todo,name='delete'),
   
]
