from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    gender = serializers.ChoiceField(choices=Employee.GENDER)
    email = serializers.CharField(
        required=False,
        validators=[UniqueValidator(queryset=Employee.objects.all())]
    )

    class Meta:
        model = Employee
        fields = 'first_name', 'last_name', 'birthday', 'department', 'gender', 'hire_date', 'job_title', 'email', \
                 'extension', 'reports_to', 'salary'
