from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("hello/", views.hello),
    path("students/", views.student),
    path("students_list/", views.student_list),

]