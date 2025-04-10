from django.contrib.auth import user_login_failed
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..make_token import *
from ..serializers import *
class LoginApi(APIView):
    permission_classes = [AllowAny,]

    def post(self,request):
        serializer=LoginSrializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.validated_date.get("user")
        tokken["salom"]="h1"
        token["is_admin"]=user.is_superuser
        return Response(data=token,status=status.HTTP_200_OK)





