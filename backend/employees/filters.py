import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
        firstname = django_filters.CharFilter(field_name='firstname', lookup_expr='iexact')
        email = django_filters.CharFilter(field_name='email', lookup_expr='icontains')
        # #between range we can filter
        # int_min=django_filters.CharFilter(method='filter_by_id_range')
        # int_max=django_filters.CharFilter(method='filter_by_id_range')

        
        class Meta:
            model = Employee
            fields = ['firstname','email']
        
        # def filter_by_id_range(self, queryset, name, value,):
              
            
            

