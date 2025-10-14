from django.shortcuts import render
from attendance.models import Attendance

# Create your views here.

def dashboard(request):
    records = Attendance.objects.select_related('student').order_by('-date')
    return render(request, 'attendance_list.html', {
        'records': records
    })