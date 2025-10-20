from django.shortcuts import render, redirect
from attendance.models import Attendance, Student
from django.http import JsonResponse
from django.utils import timezone
from attendance.forms import StudentForm

# Create your views here.

def attendance_list(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attendance_list.html', {
        'records': records
    })

def add_student(request): 
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('attendance_list')
    else: 
        form = StudentForm()
    return render(request, 'add_student.html', {'form': form})

def mark_attendance(request):
    students = Student.objects.all()
    date = timezone.now().date()

    if request.method == 'POST':
        for student in students:
            is_present = f'student_{student.id}' in request.POST
            Attendance.objects.update_or_create(
                student=student,
                date=date,
                defaults={'present': is_present}
            )
        return redirect('attendance_list')
    
    return render(request, 'attendance_list.html')