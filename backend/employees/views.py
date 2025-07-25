from django.shortcuts import render
#import Response from rest_framework.response
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializer import EmployeeSerializer
from rest_framework import status
from django.http import Http404
from rest_framework import mixins, generics
from rest_framework import viewsets





# Create your views here.

"""
#Viewset Curd operation for Employee
====================================== """

#viewsets.ModelViewSet Take only queryset and serializer_class as arguments
# from rest_framework import viewsets
#In viewsets you have to also change the urls.py file to use router
# from rest_framework.routers import DefaultRouter

#1 way to define viewset
class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # This will automatically provide list, create, retrieve, update, and destroy actions


#2 way to define viewset
class EmployeeView(viewsets.ViewSet):
    def list(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def retrieve(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)
    def update(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
 




"""
# Generic based CURD Operation for Employee
===========================================
class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    

class EmployeeIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    lookup_field = 'pk'  # Allows using 'pk' in the URL for detail view
    
"""






"""

#Mixin based CURD Operation for Employee
=========================================
class EmployeeView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset =Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    
class EmployeeIdView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self,request, pk):
        return self.retrieve(request, pk)
    def put(self, request, pk):
        return self.update(request,pk)
    def delete(self, request, pk):
        return self.destroy(request,pk)


        """

"""
#Class based CURD Operation for Employee
==========================================
class EmployeeView(APIView):
    def get(self, request):
        # Logic to retrieve employee data
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)


        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
    
class EmployeeIdView(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self,request, pk):
        employee=self.get_object(pk)
       
        serializer= EmployeeSerializer(employee)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employee= self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
       
"""

    

    
    