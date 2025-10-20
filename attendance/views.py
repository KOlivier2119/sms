from django.shortcuts import render
from attendance.models import Attendance

# Create your views here.

def attendance_list(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attendance_list.html', {
        'records': records
    })

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
    
    return render(request, 'mark_attendance.html')