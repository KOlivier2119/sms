from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    LOCATION_CHOICES = [
        ('campus', 'Campus'),
        ('outside', 'Outside'),
    ]
    name = models.CharField(max_length=50)
    classroom = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')
    location = models.CharField(max_length=10, choices=LOCATION_CHOICES, default='campus')

    class Meta:
        db_table = "students"

    def __str__(self):
        return self.name + " - " + self.classroom   


class Attendance(models.Model): 
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now())
    present = models.BooleanField(default=False)


    class Meta:
        db_table = "attendance"

    def __str__(self):
        return f"{self.student.name} - {self.date} - {'Present' if self.present else 'Absent'}"

