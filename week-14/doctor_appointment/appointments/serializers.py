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
            "details",
            "created_by"
        ]

    def update(self, instance, validated_data):
        instance.doctor = validated_data.get('doctor', instance.doctor)
        instance.patient = validated_data.get('patient', instance.patient)
        instance.date = validated_data.get('date', instance.date)
        instance.at_time = validated_data.get('at_time', instance.at_time)
        instance.details = validated_data.get('details', instance.details)
        instance.created_by = validated_data.get('created_by', instance.created_by)
        instance.save()
        return instance

    def validate(self, data):
        appointment_datetime = datetime.combine(data['date'], data['at_time'])
        if appointment_datetime < datetime.now():
            raise serializers.ValidationError("The appointment date or time must be in the future.")
        return data