from django.urls import path
from decks.views import RetrieveUpdateDestroyDeck, ListCreateDeck, ProgressViewSet, AIDeckViewSet

urlpatterns = [
    path('', ListCreateDeck.as_view(), name='card'),
    path('ai/', AIDeckViewSet.as_view({
        'post': 'create_with_ai',
    }), name='ai_deck'),
    path('<int:deck_id>/', RetrieveUpdateDestroyDeck.as_view(), name='card'),
    path('card/', ProgressViewSet.as_view({
        'post': 'create',
    }), name='create_card'),
    path('<int:deck_id>/card/<int:card_id>/', ProgressViewSet.as_view({
        'delete': 'destroy'
    }), name='retrieve_card'),
]

