from django.contrib import admin
from .models import Departments, Employees

@admin.register(Departments)
class DepartmentsAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    pass

@admin.register(Employees)
class EmployeesAdmin(admin.ModelAdmin):
    list_display = ('name', 'department')
    search_fields = ('name',)
    pass
# Register your models here.
