from django.urls import path
from . import views

urlpatterns = [
    path('flashcards/collections', views.CollectionList.as_view()),
    path('flashcards/collections/info/<int:pk>', views.CollectionDetail.as_view()),
    path('flashcards/investigate_collection/<int:fk>', views.FlashcardsInCollection.as_view()),
    path('flashcards/modify_card/<int:pk>', views.ModifyCard.as_view())
]