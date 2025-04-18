from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from ..models import *
from ..serializers import *
from django.shortcuts import get_object_or_404

class GroupStudentCreateView(APIView):
    def get(self, request):
        groups = GroupStudent.objects.all()
        serializer = GroupStudentSerializer(groups, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GroupStudentSerializer)
    def post(self, request):
        serializer = GroupStudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupStudentDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(GroupStudent, pk=pk)

    def get(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupStudentSerializer(group)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=GroupStudentSerializer)
    def put(self, request, pk):
        group = self.get_object(pk)
        serializer = GroupStudentSerializer(group, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        group = self.get_object(pk)
        group.delete()
        return Response({"detail": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class TableCreateView(APIView):
    def get(self, request):
        table = Table.objects.all()
        serializer = TableSerializer(table, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TableSerializer)
    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TableDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Table, pk=pk)

    def get(self, request, pk):
        table = self.get_object(pk)
        serializer = TableSerializer(table)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TableSerializer)
    def put(self, request, pk):
        table = self.get_object(pk)
        serializer = TableSerializer(table, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        table = self.get_object(pk)
        table.delete()
        return Response({"detail": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)


class TableTypeCreateView(APIView):
    def get(self, request):
        table_type = TableType.objects.all()
        serializer = TableTypeSerializer(table_type, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TableTypeSerializer)
    def post(self, request):
        serializer = TableTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TableTypeDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(TableType, pk=pk)

    def get(self, request, pk):
        table_type = self.get_object(pk)
        serializer = TableTypeSerializer(table_type)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=TableTypeSerializer)
    def put(self, request, pk):
        table_type = self.get_object(pk)
        serializer = TableTypeSerializer(table_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        table_type = self.get_object(pk)
        table_type.delete()
        return Response({"detail": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

class RoomsCreateView(APIView):
    def get(self, request):
        rooms = Rooms.objects.all()
        serializer = RoomsSerializer(rooms, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RoomsSerializer)
    def post(self, request):
        serializer = RoomsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomsDetailView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Rooms, pk=pk)

    def get(self, request, pk):
        rooms = self.get_object(pk)
        serializer = RoomsSerializer(rooms)
        return Response(serializer.data)

    @swagger_auto_schema(request_body=RoomsSerializer)
    def put(self, request, pk):
        rooms = self.get_object(pk)
        serializer = RoomsSerializer(rooms, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        rooms = self.get_object(pk)
        rooms.delete()
        return Response({"detail": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)