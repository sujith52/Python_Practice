from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "age", "branch"]
    def clean_age(self):
        age = self.cleaned_data["age"]
        if age < 18 or age > 60:
            raise forms.ValidationError(
                "Student must be abeove 18 and below 60 "
            )
        return age
    def clean_name(self):
        name = self.cleaned_data["name"]
        main = str(name)
        if main.lower() == "catman":
            raise forms.ValidationError(
                "A student name cannot be in catman !"
            )
        return name
