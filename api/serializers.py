from django.db.models import fields
from rest_framework import serializers
from .models import student
from api import models

class studentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self,validated_data):
        return student.objects.create(**validated_data)

    def update(self,instance,validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.name)
        instance.city = validated_data.get('city',instance.name)
        instance.save()
        return instance

