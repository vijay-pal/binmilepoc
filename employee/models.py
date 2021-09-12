from django.db import models

from department.models import Department


def on_delete_manager(instance):
    return instance.reports_to


class Employee(models.Model):
    GENDER = (('M', 'Male'), ('F', 'Female'))
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    birthday = models.DateField(null=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    gender = models.CharField(max_length=1, choices=GENDER, null=False)
    hire_date = models.DateField(null=False, auto_now_add=True)
    job_title = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    extension = models.CharField(max_length=5, null=True, blank=True)
    reports_to = models.ForeignKey('self', null=True, on_delete=models.SET(on_delete_manager))
    salary = models.PositiveIntegerField(null=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta:
        db_table = "employees"
