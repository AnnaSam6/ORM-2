from django.shortcuts import render
from .models import Student


def student_list(request):
    # Используем prefetch_related для оптимизации запросов
    students = Student.objects.prefetch_related('teachers').all()
    return render(request, 'school/student_list.html', {'students': students})
