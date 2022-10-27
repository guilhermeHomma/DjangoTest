from rest_framework import serializers
from core import models

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Departments
        fields = '__all__'

class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employees
        fields = '__all__'