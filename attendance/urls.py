from django.contrib import admin
from django.urls import path, include
from attendance import views

urlpatterns = [   
    path('records/', views.student_list, name='student_list'),    
    path('register/', views.add_student, name='add_student'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
]
