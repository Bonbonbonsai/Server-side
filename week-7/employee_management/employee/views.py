from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Employee, Position, Project
from django.db.models import Count

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
        collect_path = Project.objects.filter(id=num)
        return render(request, "project_detail.html", {
            "selected_project": collect_path
        })