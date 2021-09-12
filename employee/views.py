from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny

from employee import serializers
from employee.models import Employee


class Pagination(PageNumberPagination):
    page_size = 20


class AddEmployeeAPIView(generics.CreateAPIView):
    """
    The class Allow to create an employee record by the POST method.
    """
    queryset = Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer
    permission_classes = AllowAny,


class EmployeeAPIView(generics.UpdateAPIView, generics.RetrieveAPIView):
    """
    The class allow to invoke multiple methods of REST, like
    UPDATE: Allow to update all data items (In this case required fields are mandatory) of an id,
    PATCH: This method allow to update one or multiple field of data set of specific id (employee) &
    GET: By this method we can retrieve data of an employee (id)
    """
    queryset = Employee.objects.filter(status=True)
    serializer_class = serializers.EmployeeSerializer
    permission_classes = AllowAny,


class EmployeeListAPIView(generics.ListAPIView):
    """
    The method allow you to retrieve a list of data by GET method,
    at a time this returns 20 record in the list, we can get next 20 by page passing page=number in request.
    """
    queryset = Employee.objects.filter(status=True)
    serializer_class = serializers.EmployeeSerializer
    permission_classes = AllowAny,
    pagination_class = Pagination
