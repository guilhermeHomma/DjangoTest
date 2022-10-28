import imp
from django import urls
from django.urls import path, include
from . import views

from core.api import viewsets as coreviews

from rest_framework import routers

from . import views

route = routers.DefaultRouter()

route.register(r'departments', coreviews.DepartmentsViewSet, basename='departments')

route.register(r'employees', coreviews.EmployeesViewSet, basename='employees')


urlpatterns = [

    path('api/', include(route.urls)),
    path('', views.index),
]
