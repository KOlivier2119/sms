from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    announcements = models.TextField(max_length=100)

    class Meta:
        db_table = "teachers"

    def __str__(self):
        return f"{self.name} - {self.subject}"

class Announcement(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        db_table = "announcements"

    def __str__(self):
        return self.title