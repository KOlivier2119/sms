from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.contrib import messages

from attendance.models import Attendance, Student
from attendance.forms import StudentForm


def attendance_list(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attendance_list.html', {
        'records': records
    })


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {
        'students': students
    })


def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('add_student')
        else:
            messages.error(request, 'Failed to add student. Please fix the errors below.')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})



def mark_attendance(request):
    students = Student.objects.all()
    date = timezone.now().date()

    if request.method == 'POST':
        try:
            for student in students:
                is_present = f'student_{student.id}' in request.POST
                Attendance.objects.update_or_create(
                    student=student,
                    date=date,
                    defaults={'present': is_present}
                )
            messages.success(request, 'Attendance marked successfully!')
        except Exception as e:
            messages.error(request, f'Failed to mark attendance: {e}')

        return redirect('attendance_list')

    return render(request, 'mark_attendance.html', {'students': students})