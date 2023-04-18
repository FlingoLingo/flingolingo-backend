from rest_framework import serializers

from .models import Card
from decks.models import Progress

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ( 'id', 'rus', 'eng', 'transcription', 'examples')
