from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


class Employee(ExportModelOperationsMixin('dog'), models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    employee_id = models.IntegerField(unique=True, primary_key=True)
    department = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + " " + self.last_name
