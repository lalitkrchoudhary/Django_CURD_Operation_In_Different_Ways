
from django.urls import path, include
from .views import EmployeeView
from rest_framework.routers import DefaultRouter
from .views import EmployeeIdView, EmployeeView


# router = DefaultRouter()
# router.register('emp', EmployeeView, basename='employee')  #EmployeeView is the class we have to define in views.py Register the viewset with the router


urlpatterns = [
   path('', EmployeeView.as_view(), name='employee-home'),
   path ('<int:pk>/',EmployeeIdView.as_view(), name='employee-detail'),
   # path('', include(router.urls)),  # Include the router's URLs


]
