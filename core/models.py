from unittest.util import _MAX_LENGTH
from django.db import models

class Departments(models.Model):
    name = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return self.name

class Employees(models.Model):
    name = models.CharField(max_length = 40)
    email = models.CharField(max_length = 40)
    department = models.ForeignKey(Departments, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name