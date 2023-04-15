from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListCreateAPIView
from rest_framework import permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import ValidationError, PermissionDenied, NotAuthenticated

from .models import Deck, Progress
from .serializers import DeckSerializer, ProgressSerializer
from cards.serializers import CardSerializer
from cards.models import Card

class ListCreateDeck(ListCreateAPIView):
    model = Deck
    permission_classes = (IsAuthenticated,)
    serializer_class = DeckSerializer
    def get_queryset(self):
        return Deck.objects.filter(owner=self.request.user)
    def create(self, request):
        serializer = DeckSerializer(data=request.data, context={'auth_usr': request.user})
        serializer.is_valid(raise_exception=True)
        deck = serializer.save()
        return Response(DeckSerializer(deck).data, status=201)

class RetrieveUpdateDestroyDeck(RetrieveUpdateDestroyAPIView):
    model = Deck
    permission_classes = (IsAuthenticated,)
    serializer_class = DeckSerializer
    lookup_url_kwarg = 'deck_id'
    def get_queryset(self):
        return Deck.objects.filter(owner=self.request.user)


class ProgressViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def create(self, request):
        card_serializer = CardSerializer(data=request.data.get('card'))
        print('card validation1')
        card_serializer.is_valid(raise_exception=True)
        card = Card.objects.get_or_create(**card_serializer.data)[0]
        decks = request.data.get('decks')
        for deck_id in decks:
            deck = get_object_or_404(Deck, id=deck_id, is_private=True, owner=request.user)
            # if deck.is_private and deck.owner != request.user:
            #     raise PermissionDenied("You don't have acces to this deck")
            Progress.objects.get_or_create(deck=deck, card=card)

        progress_serializer = ProgressSerializer(data=request.data.get('card'))
        print('progress validation')
        progress_serializer.is_valid(raise_exception=True)
        return Response(CardSerializer(instance=card).data, status=201)

    def destroy(self, request, deck_id, card_id):
        progress = get_object_or_404(Progress, deck_id=deck_id, card_id=card_id)
        progress.delete()
        return Response(status=204)

# class AddCard(CreateAPIView):
#     model = Progress
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ProgressSerializer
#     lookup_url_kwarg = 'deck_id'


# class RemoveCard(CreateAPIView):
#     model = Progress
#     permission_classes = (IsAuthenticated,)
#     serializer_class = ProgressSerializer
#     lookup_url_kwarg = 'deck_id'
#     queryset = Progress.objects.all()
    