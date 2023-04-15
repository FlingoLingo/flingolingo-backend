from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated

from .models import Card
from .serializers import CardSerializer
from decks.serializers import ProgressSerializer
from decks.models import Progress
# class CreateCard(CreateAPIView):
#     model = Card
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CardSerializer

# class RetrieveCard(RetrieveAPIView):
#     model = Card
#     permission_classes = (IsAuthenticated,)
#     lookup_url_kwarg = 'card_id'
#     serializer_class = Card
#     def get_queryset(self):
#         return Progress.objects.filter(deck__owner=self.request.user)

    