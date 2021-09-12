from django.urls import path

from department.views import DepartmentAPIView, DepartmentListAPIView, AddDepartmentAPIView

urlpatterns = [
    path('', AddDepartmentAPIView.as_view(), name='create-department'),
    path('<int:pk>', DepartmentAPIView.as_view(), name='department-view'),
    path('list', DepartmentListAPIView.as_view(), name='department-list'),
]
