from django import forms
from django.forms import ModelForm
from .models import *
from django.core.exceptions import ValidationError
from datetime import datetime

'''
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
'''

class EmployeeForm(ModelForm):
    gender_choices = [
        ("M", "M"),
        ("F", "F"),
        ("LGBT", "LGBT")
    ]

    first_name = forms.CharField(label="First name:", max_length=155, required=True)
    last_name = forms.CharField(label="Last name:", max_length=155, required=True)
    gender = forms.ChoiceField(label="Gender:", choices=gender_choices, required=True)
    birth_date = forms.DateField(label="Birth date:", widget=forms.DateInput(attrs={"type" :"date"}))
    hire_date = forms.DateField(label="Hire date:", widget=forms.DateInput(attrs={"type" :"date"}))
    salary = forms.DecimalField(label="Salary:", max_digits=10, decimal_places=2, initial=0)
    position = forms.ModelChoiceField(
        label="Position:",
        queryset=Position.objects.all(),
        required=True
    )

    class Meta:
        model = Employee
        fields = "__all__"
    
    def clean(self):
        cleaned_data = super().clean()
        hire_date = cleaned_data.get("hire_date")

        if hire_date > datetime.now().date():
            self.add_error("hire_date", "Hire date cannot be in the future.")

        return cleaned_data

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "manager",
            "start_date",
            "due_date"
        ]
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        due_date = cleaned_data.get("due_date")
        if start_date > due_date:
            self.add_error(
                'start_date',
                'Start date should not be before Due date'
            )
        return cleaned_data