from django.urls import path
from appointments import views as appointment_views
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('doctors/', appointment_views.DoctorList.as_view(), name='doctor-list'),
    path('patients/', appointment_views.PatientList.as_view(), name='patient-list'),
    path('appointment/', appointment_views.AppointmentList.as_view(), name='appointment-list'),
    path('appointment/<int:pk>/', appointment_views.AppointmentDetail.as_view(), name='appointment-detail')
]