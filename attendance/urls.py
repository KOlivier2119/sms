from django.contrib import admin
from django.urls import path, include
from attendance import views

urlpatterns = [   
    path('records/', views.attendance_list, name='attendance_list'),    
    path('register/', views.add_student, name='add_student')
]
