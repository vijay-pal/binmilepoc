from rest_framework import generics
from rest_framework.permissions import AllowAny

from department import serializers
from department.models import Department
from employee.views import Pagination


class AddDepartmentAPIView(generics.CreateAPIView):
    """
    The class Allow to create a department record by the POST method.
    """
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    permission_classes = AllowAny,


class DepartmentListAPIView(generics.ListAPIView):
    """
       The method allow you to retrieve a list of data by GET method,
       at a time this returns 20 record in the list, we can get next 20 by page passing page=number in request.
       """
    queryset = Department.objects.filter(status=True)
    serializer_class = serializers.DepartmentSerializer
    permission_classes = AllowAny,
    pagination_class = Pagination


class DepartmentAPIView(generics.UpdateAPIView, generics.RetrieveAPIView):
    """
           Methods are allow to invoke multiple methods of REST, like
           UPDATE: Allow to update all data items (In this case required fields are mandatory) of an id,
           PATCH: This method allow to update one or multiple field of data set of specific id (department) &
           GET: By this method we can retrieve data of a department (id)
           """
    queryset = Department.objects.filter(status=True)
    serializer_class = serializers.DepartmentSerializer
    permission_classes = AllowAny,
