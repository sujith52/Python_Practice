from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("hello/", views.hello),
    path("students/", views.student),
    path("students_list/", views.student_list, name= "students_list"),
    path("student_add/", views.add_student, name="add_student"),
    path("register/", views.register_view, name = "register"),
    path("login/", views.login_view, name = "login"),
    path("dashboard/", views.dashboard, name = "dashboard"),
    path("logout/", views.logout_view, name = "logout"),
]