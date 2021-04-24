from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status


from reports.models import ExcelFile
from users.models import User
from .serializers import SendDataSerializer


class OrderViewSet(ModelViewSet):
    queryset = ExcelFile.objects.filter(is_order=True)
    serializer_class = SendDataSerializer
    http_method_names = ['get']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class SendDataViewSet(ModelViewSet):
    queryset = ExcelFile.objects.all()
    serializer_class = SendDataSerializer
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(request.data)
        is_order = serializer.data['is_order']
        exel_id = serializer.data['id']
        ExcelFile.objects.filter(id=exel_id).update(is_order=is_order)
        return Response(status=status.HTTP_201_CREATED)


