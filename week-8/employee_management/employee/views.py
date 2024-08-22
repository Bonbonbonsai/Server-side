from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Employee, Position, Project
from django.db.models import Count, Value
from django.db.models.functions import Concat
import json

# Create your views here.
class EmployeeView(View):
    def get(self, request):
        employees = Employee.objects.all()
        employee_count = Employee.objects.all().count()
        return render(request, "employee.html", {
            "employees": employees,
            "employee_total": employee_count
        })

class PositionView(View):
    def get(self, request):
        positions = Position.objects.all().annotate(emp_count=Count("employee")).order_by("id")
        return render(request, "position.html", {
            "positions": positions,
        })
    
class ProjectView(View):
    def get(self, request):
        projects = Project.objects.all()
        return render(request, "project.html", {
            "projects": projects
        })
    
    def delete(self, request, num):
        get_project = Project.objects.filter(id=num)
        get_project.delete()
        return JsonResponse({"status": "ok"})

class ProjectDetailView(View):
    def get(self, request, num):
        project = Project.objects.annotate(manager_full_name=Concat("manager__first_name", Value(' '), "manager__last_name")).get(id=num)
        employee_in_this_project = Employee.objects.filter(project__id=num)
        return render(request, "project_detail.html", {
            "project": project,
            "employee_in_this_project": employee_in_this_project
        })

    def put(self, request, num):
        data = json.loads(request.body).get('emp_id')
        project = Project.objects.get(id=num)
        employee = Employee.objects.get(id=data)
        if employee not in project.staff.all():
            project.staff.add(employee)
        return JsonResponse({'status': 'ok'}, status=200)
    
    def delete(self, request, num, emp_id):
        project = Project.objects.get(id=num)
        employee = Employee.objects.get(id=emp_id)
        project.staff.remove(employee)
        return JsonResponse({'status': 'ok'}, status=200)
