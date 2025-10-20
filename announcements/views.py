from django.shortcuts import render
from announcements.models import Announcement

# Create your views here.

def announcements_list(request):
    
    records = Announcement.objects.select_related('teacher').order_by('-date_posted')
    return render(request, 'announcements/announcement_list.html', {
        'records': records
    })