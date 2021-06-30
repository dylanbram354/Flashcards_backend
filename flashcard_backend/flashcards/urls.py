from django.urls import path
from . import views

urlpatterns = [
    path('flashcards/collections', views.CollectionList.as_view()),
    path('flashcards/collections/<int:pk>', views.CollectionDetail.as_view())
]