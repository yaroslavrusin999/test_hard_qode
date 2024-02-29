from django.shortcuts import render
from rest_framework import permissions, viewsets

from student.models import Student
from student.serializers import StudentSerializer


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all().order_by('-date_joined')
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAdminUser]
