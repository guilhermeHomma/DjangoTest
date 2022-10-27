from rest_framework import viewsets
from core.api import serializer
from core import models

class DepartmentsViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.DepartmentsSerializer
    queryset = models.Departments.objects.all()

class EmployeesViewSet(viewsets.ModelViewSet):
    serializer_class = serializer.EmployeesSerializer
    queryset = models.Departments.objects.all()
