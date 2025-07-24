
from django.urls import path
from .views import EmployeeView, EmployeeIdView


urlpatterns = [
   path('', EmployeeView.as_view(), name='employee-home'),
   path ('<int:pk>/',EmployeeIdView.as_view(), name='employee-detail'),



]
