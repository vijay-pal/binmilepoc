from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from department.models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=Department.objects.all())]
    )

    class Meta:
        model = Department
        fields = 'id', 'name',
        extra_kwargs = {
            "id": {"read_only": True}
        }
