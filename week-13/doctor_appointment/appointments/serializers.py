from rest_framework import serializers
from .models import Doctor, Patient, Appointment
from datetime import datetime

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id",
            "name",
            "specialization",
            "phone_number",
            "email"
        ]

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = [
            "id",
            "name",
            "phone_number",
            "email",
            "address"
        ]

class AppointmentSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()
    patient = PatientSerializer()

    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "patient",
            "date",
            "at_time",
            "details"
        ]

    def validate(self, data):
        appointment_datetime = datetime.combine(data['date'], data['at_time'])
        if appointment_datetime < datetime.now():
            raise serializers.ValidationError("The appointment date or time must be in the future.")
        return data
    
class AppointmentPostSerializer(serializers.ModelSerializer):
    doctor = serializers.PrimaryKeyRelatedField(
        queryset=Doctor.objects.all()
    )
    patient = serializers.PrimaryKeyRelatedField(
        queryset=Patient.objects.all()
    )

    class Meta:
        model = Appointment
        fields = [
            "id",
            "doctor",
            "patient",
            "date",
            "at_time",
            "details"
        ]

    def validate(self, data):
        appointment_datetime = datetime.combine(data['date'], data['at_time'])
        if appointment_datetime < datetime.now():
            raise serializers.ValidationError("The appointment date or time must be in the future.")
        return data