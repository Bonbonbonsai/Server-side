from django.urls import path
from employee import views

urlpatterns = [
    path("employee/", views.EmployeeView.as_view(), name="employee"),
    path("position/", views.PositionView.as_view(), name="position"),
    path("project/", views.ProjectView.as_view(), name="project"),
    path("project/<int:project_id>/", views.ProjectView.as_view(), name="delete"),
    path("project/detail/<int:project_id>/", views.ProjectDetailView.as_view(), name="detail"),
    path("project/detail/<int:project_id>/add-user/", views.ProjectDetailView.as_view(), name="addUser"), 
    path("project/detail/<int:project_id>/remove-user/<int:emp_id>/", views.ProjectDetailView.as_view(), name="removeUser"),
    path("employee/form/", views.FormEmployeeView.as_view(), name="employeeForm")
]
