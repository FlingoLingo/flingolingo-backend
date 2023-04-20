from rest_framework import serializers
from django.forms import model_to_dict
from .models import Deck, Progress
from cards.models import Card

from cards.serializers import CardSerializer


class ProgressSerializer(serializers.ModelSerializer):
    decks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)


    class Meta:
        model = Progress
        fields = ['id', 'is_learned', 'decks' ]

class CardWithProgressSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        card_with_progress = super().to_representation(instance)
        card = model_to_dict(instance.card)

        for key, value in card.items():
            card_with_progress[key] = value
        del card_with_progress["card"]
        return card_with_progress

    class Meta:
        model = Progress
        fields = ['is_learned', 'card' ]
        depth = 0

class DeckSerializer(serializers.ModelSerializer):
    cards = CardWithProgressSerializer(many=True, required=False)
    read_only_fields = ('last_repeated')

    def create(self, validated_data):
        auth_usr = self.context['auth_usr']
        message = Deck.objects.create(owner=auth_usr, **validated_data)

        return message
    class Meta:
        model = Deck
        fields = ['id', 'is_private', 'name', 'last_repeated', 'cards']





class ProgressMarkAsLearnedSerializer(serializers.ModelSerializer):

    class Meta:
        model = Progress
        fields = []

    def update(self, message, validated_data):
        message.is_read = True
        message.save()
        return message
