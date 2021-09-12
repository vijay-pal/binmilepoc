from django.urls import path

from employee.views import EmployeeListAPIView, AddEmployeeAPIView, EmployeeAPIView

urlpatterns = [
    path('', AddEmployeeAPIView.as_view(), name='create-employee'),
    path('<int:pk>', EmployeeAPIView.as_view(), name='employee-view'),
    path('list', EmployeeListAPIView.as_view(), name='employee-list'),
]
