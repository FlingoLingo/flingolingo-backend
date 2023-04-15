from django.urls import path
from users.views import RetrieveUpdateDestroyUser, CreateUser

urlpatterns = [
    path('register/', CreateUser.as_view(), name='register'),
    path('', RetrieveUpdateDestroyUser.as_view(), name='user'),
]


