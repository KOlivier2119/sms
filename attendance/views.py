from django.shortcuts import render

# Create your views here.

def attendance_list(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attendance/attendance_list.html', {
        'records': records
    })