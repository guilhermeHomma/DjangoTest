from django import urls
from django.urls import path, include
from . import views

from core.api import viewsets as coreviews

from rest_framework import routers


route = routers.DefaultRouter()

route.register(r'departments', coreviews.DepartmentsViewSet, basename='departments')

route.register(r'employees', coreviews.EmployeesViewSet, basename='employees')



urlpatterns = [


    path('', include(route.urls))
]
