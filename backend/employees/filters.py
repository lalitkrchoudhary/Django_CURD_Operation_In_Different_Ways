import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
        firstname = django_filters.CharFilter(field_name='firstname', lookup_expr='iexact')
        email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')

        
        class Meta:
            model = Employee
            fields = ['firstname','email']

