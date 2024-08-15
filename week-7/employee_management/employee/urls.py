from django.urls import path
from employee import views

urlpatterns = [
    path("employee/", views.EmployeeView.as_view(), name="employee"),
    path("position/", views.PositionView.as_view(), name="position"),
    path("project/", views.ProjectView.as_view(), name="project"),
    path("project/<int:num>/", views.ProjectView.as_view(), name="delete"),
    path("project_detail/<int:num>/", views.ProjectDetailView.as_view(), name="detail")
]