from django.db import models

# Create your models here.

class Student (models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.IntegerField()

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Student1(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    branch = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="students"
    )
    def __str__(self):
        return self.name

class Course(models.Model):
    course = models.CharField(max_length=100)

class Student2(models.Model):
    name = models.CharField(max_length=100)
    course = models.ManyToManyField(Course, related_name="courses")
