from django import forms
from .models import Student, Attendance

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'classroom', 'gender', 'location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter student name'}),
            'classroom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter classroom name'}),
            'gender': forms.RadioSelect(),
            'location': forms.Select()
        }