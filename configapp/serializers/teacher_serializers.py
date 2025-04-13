from rest_framework import serializers
from . import UserSerializer
from ..models import *
class TeacherSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Teacher
        fields=["id","user","department","descriptions","course"]

class TeacherPostSerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)
    is_teacher = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_student = serializers.BooleanField(read_only=True)
    class Meta:
        model = User
        fields = (
            'id', 'phone_number', 'password', 'email', 'is_active', 'is_staff', 'is_admin', 'is_teacher', 'is_student')


class TeacherPostSerializer(serializers.Serializer):
    user=UserSerializer()
    teachers=TeacherSerializer()
