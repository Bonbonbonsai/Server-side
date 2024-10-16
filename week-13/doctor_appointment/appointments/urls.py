from django.urls import path
from appointments import views

urlpatterns = [
    path('doctors/', views.DoctorList.as_view(), name='doctor-list'),
    path('patients/', views.PatientList.as_view(), name='patient-list'),
    path('appointment/', views.AppointmentList.as_view(), name='appointment-list'),
    path('appointment/<int:pk>/', views.AppointmentDetail.as_view(), name='appointment-detail')
]