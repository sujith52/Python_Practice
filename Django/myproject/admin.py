from django.contrib import admin

# Register your models here.
from .models import Book
from .models import Student

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price")
    search_fields = ("title", "author")
    list_filter = ("author",)
    def __str__(self):
        return self.title

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "branch")
    search_fields = ("name", "branch")
    list_filter = ("branch", )
    def __str__(self):
        return self.name

