from django.shortcuts import get_object_or_404
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User

from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

from .serializers import UserSerializer, ChangePasswordSerializer


class CreateUser(CreateAPIView):

    model = User
    permission_classes = (permissions.AllowAny,)
    serializer_class = UserSerializer

class RetrieveUpdateDestroyUser(RetrieveUpdateDestroyAPIView):
    model = User
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user
    
    def partial_update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            token = Token.objects.get(user=self.object)
            token.delete()
            Token.objects.create(user=self.object)

            return Response({'message': 'Password changed successfully'}, status=200)
        
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        return Response({'message': 'Account deleted successfully'}, status=200)