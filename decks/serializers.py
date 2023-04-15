from rest_framework import serializers

from .models import Deck, Progress
from cards.models import Card

from cards.serializers import CardSerializer


class ProgressSerializer(serializers.ModelSerializer):
    decks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Progress
        fields = ['id', 'is_learned', 'decks' ]

class DeckSerializer(serializers.ModelSerializer):
    cards = ProgressSerializer(many=True, required=False)

    def create(self, validated_data):
        auth_usr = self.context['auth_usr']
        message = Deck.objects.create(owner=auth_usr, **validated_data)

        return message
    class Meta:
        model = Deck
        fields = ['id', 'is_private', 'name', 'description', 'cards']





class ProgressMarkAsLearnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Progress
        fields = []

    def update(self, message, validated_data):
        message.is_read = True
        message.save()
        return message
