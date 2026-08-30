from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Student

def hello(request):
    context = {
        "name" : "Sujith",
        "age" : 22,
        "course" : "Computer Science "
    }
    return render(request, "students/hello.html",context)

def student(request):
    content = {
        "name": "G Sujith Kumar !",
        "goal" : "To become a full stack web developer !",
        "age" : 22
    }
    return render(request, "students/main.html", content)

def student_list(request):
    students = Student.objects.all()
    return render(
        request,
        "students/student_list.html",
        {"students" : students}
    )