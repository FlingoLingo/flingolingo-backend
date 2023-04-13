from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class RetrieveUser(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_url_kwarg = 'user_id'


from .serializers import UserSerializer


class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,) 
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)