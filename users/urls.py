from django.urls import path
from users.views import RetrieveUser, HelloView, CreateUserView

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('register/', CreateUserView.as_view(), name='register'),
    path('<int:user_id>/', RetrieveUser.as_view(), name='user_detail')
]


