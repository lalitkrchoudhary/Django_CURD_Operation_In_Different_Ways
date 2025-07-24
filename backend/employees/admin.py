from django.contrib import admin

# Register your models here.

from .models import Employee

#resister employee model to admin without decorator
admin.site.register(Employee)
