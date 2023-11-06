from django.views.generic import ListView
from django.shortcuts import render

from .models import Student

class StudentListView(ListView):
    model = Student
    template_name = 'school/students_list.html'
    context_object_name = 'students'
    ordering = 'group'

def students_list(request):
    return StudentListView.as_view()(request)
