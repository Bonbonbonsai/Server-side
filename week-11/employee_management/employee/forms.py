from django import forms
from django.forms import ModelForm
from .models import *
from company.models import Position
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
    position_id = forms.ModelChoiceField(
        label="Position:",
        queryset=Position.objects.using("db2").all(),
        required=True
    )
    location = forms.CharField(widget=forms.TextInput(attrs={"cols": 30, "rows": 3}))
    district = forms.CharField(max_length=100)
    province = forms.CharField(max_length=100)
    postal_code = forms.CharField(max_length=15)

    class Meta:
        model = Employee
        fields = [
            "first_name", 
            "last_name", 
            "gender", 
            "birth_date", 
            "hire_date", 
            "salary", 
            "position_id",
            "location",
            "district",
            "province",
            "postal_code"
        ]
        widgets = {
            'birth_date': forms.widgets.DateInput(attrs={'type': 'date'}),
            'hire_date': forms.widgets.DateInput(attrs={'type': 'date'})
        }
    
    def clean(self):
        cleaned_data = super().clean()
        hire_date = cleaned_data.get("hire_date")
        position = cleaned_data.get("position_id")

        cleaned_data["position_id"] = position.id
        return cleaned_data

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