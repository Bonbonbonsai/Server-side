from django import forms
from .models import *

class EmployeeForm(forms.Form):
    gender_choices = [
        ("M", "M"),
        ("F", "F"),
        ("LGBT", "LGBT")
    ]

    first_name = forms.CharField(label="First name:", max_length=155, required=True)
    last_name = forms.CharField(label="Last name:", max_length=155, required=True)
    gender = forms.ChoiceField(label="Gender:", choices=gender_choices, required=True)
    birth_date = forms.DateField(label="Birth date:", widget=forms.DateInput(attrs={"type" :"date"}), required=True)
    hire_date = forms.DateField(label="Hire date:", widget=forms.DateInput(attrs={"type" :"date"}), required=True)
    salary = forms.DecimalField(label="Salary:", max_digits=10, decimal_places=2, initial=0, required=True)
    position = forms.ModelChoiceField(
        label="Position:",
        queryset=Position.objects.all(),
        required=True
    )