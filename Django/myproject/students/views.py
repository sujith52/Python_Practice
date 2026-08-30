from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
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

def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("students_list")
    else:
        form = StudentForm()
    return render(
        request,
        "students/add_student.html",
        {"form": form}
    )

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(
                request,
                "students/login.html",
                {"error": "Invalid username or password "}
            )
    return render(request, "students/login.html")

@login_required
def dashboard(request):
    return render(
        request,
        "students/dashboard.html"
    )

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(
        request,
        "students/register.html",
        {"form": form}
    )

def logout_view(request):
    logout(request)
    return redirect("login")