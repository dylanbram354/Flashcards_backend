from django.urls import path
from . import views

urlpatterns = [
    path('flashcards/collections', views.CollectionList.as_view()),
    path('flashcards/collections/info/<int:pk>', views.CollectionDetail.as_view()),
    path('flashcards/cards_in_collection/<int:fk>', views.FlashcardList.as_view())
]