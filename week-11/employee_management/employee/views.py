from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import View
from .models import Employee, Project, EmployeeAddress
from company.models import Position
from django.db.models import Count, Value
from django.db.models.functions import Concat
from .forms import EmployeeForm, ProjectForm
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
import json

# Create your views here.
class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all().order_by("-hire_date")
        for employee in employees:
            employee.position = Position.objects.get(pk=employee.position_id)
        employee_count = Employee.objects.all().count()
        return render(request, "employee.html", {
            "employees": employees,
            "employee_total": employee_count
        })
    
class ProjectView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, "project.html", {
            "projects": projects
        })
    
    def delete(self, request, project_id):
        get_project = Project.objects.filter(id=project_id)
        get_project.delete()
        return JsonResponse({"status": "ok"})

class ProjectDetailView(View):
    def get(self, request, project_id):
        project = Project.objects.annotate(manager_full_name=Concat("manager__first_name", Value(' '), "manager__last_name")).get(id=project_id)
        employee_in_this_project = Employee.objects.filter(project__id=project_id)
        return render(request, "project_detail.html", {
            "project": project,
            "employee_in_this_project": employee_in_this_project
        })

    def put(self, request, project_id):
        data = json.loads(request.body).get('emp_id')
        project = Project.objects.get(id=project_id)
        employee = Employee.objects.get(id=data)
        project.staff.add(employee)
        return JsonResponse({'status': 'ok'}, status=200)
    
    def delete(self, request, project_id, emp_id):
        project = Project.objects.get(id=project_id)
        employee = Employee.objects.get(id=emp_id)
        project.staff.remove(employee)
        return JsonResponse({'status': 'ok'}, status=200)
    
class FormEmployeeView(View):
    def get(self, request):
        form = EmployeeForm()
        return render(request, "employee_form.html", {"form": form})
    '''
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            birth_date = form.cleaned_data["birth_date"]
            hire_date = form.cleaned_data["hire_date"]
            salary = form.cleaned_data["salary"]
            position = form.cleaned_data["position"]

            new_emp = Employee(
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                birth_date=birth_date,
                hire_date=hire_date,
                salary=salary,
                position=position
            )
            new_emp.save()

        return HttpResponseRedirect('/employee/')
    '''
    def post(self, request):
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # save ข้อมูล employee
                    employee = form.save()

                    # save ข้อมูล address ของ employee
                    location = form.cleaned_data["location"]
                    district = form.cleaned_data["district"]
                    province = form.cleaned_data["province"]
                    postal_code = form.cleaned_data["postal_code"]
                    address = EmployeeAddress(
                        employee=employee,
                        location=location,
                        district=district,
                        province=province,
                        postal_code=postal_code
                    )
                    address.save()
            except ObjectDoesNotExist:
                print("Save unsucessfully.")

            return redirect('employee')
        else:
            return render(request, "employee_form.html", {"form": form})
        
class FormProjectView(View):
    def get(self, request):
        form = ProjectForm()
        return render(request, 'project_form.html', {'form': form})

    def post(self, request):
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/project/')
        else:
            return render(request, 'project_form.html', {'form': form})
        
class EditProject(View):
    def get(self, request):
        project = Project.objects.annotate(manager_full_name=Concat("manager__first_name", Value(' '), "manager__last_name"))
        employee_in_this_project = Employee.objects.filter(project__id=num)
        return render(request, "project_detail.html", {
            "project": project,
            "employee_in_this_project": employee_in_this_project
        })
