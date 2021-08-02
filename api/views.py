from os import stat
from django import http
from rest_framework.response import Response
from api.serializers import studentSerializer
from rest_framework import serializers, status
from api.models import student
from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse


# Create your views here.
class studentlist(APIView):
    def get(self,request,pk=None):
        if pk is not None:
            stu = student.objects.get(id=pk)
            serializer = studentSerializer(stu)            
        else:
            stu = student.objects.all()
            print(stu)
            serializer = studentSerializer(stu,many=True)
            print(serializer)
        return Response(serializer.data)
            # return jsonResponse(serializer.data.safe=False)

    def post(self, request):
        serializer = studentSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stu = student.objects.get(id=pk)
        stu.delete()
        return Response({'data':'data successfully deleted'})


    def put(self , request , pk = None, format = None):
        stu = student.objects.get(id = pk)
        print(stu)
        serializer = studentSerializer(stu, data = request.data)
        print(serializer)
        if serializer.is_valid():
            print('hh')
            serializer.save()
            return Response({'reply':'Data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)