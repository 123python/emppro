from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Emp
from .serializers import EmpSeriallizer

class EmpView(APIView):
    def get(self,request):
        emp=Emp.objects.all()
        serializer=EmpSeriallizer(emp,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=EmpSeriallizer(data=request.data)
        if serializer.is_valid():
            ename=serializer.data.get('ename')
            email=serializer.data.get('email')
            msg="hello {}, your mail is {}".format(ename,email)
            emp=Emp.objects.create(ename=ename,email=email)
            return Response({'message':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

