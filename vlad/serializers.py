from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from django.contrib.auth import authenticate

from users.models import User
from reports.models import ExcelFile


class SendDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = '__all__'


class OrderViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExcelFile
        fields = '__all__'
