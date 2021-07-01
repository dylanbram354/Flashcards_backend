from django.shortcuts import render
from .models import Collection, Flashcard
from .serializers import CollectionSerializer, FlashcardSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.
class CollectionList(APIView):

    def get(self, request):
        collection = Collection.objects.all()
        serializer = CollectionSerializer(collection, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CollectionDetail(APIView):

    def get_object(self, pk):
        try:
            return Collection.objects.get(id=pk)
        except Collection.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        collection = self.get_object(pk)
        serializer = CollectionSerializer(collection)
        collection.delete()
        return Response(serializer.data, status=status.HTTP_200_OK)


class FlashcardList(APIView):

    def get(self, request, fk):
        cards = Flashcard.objects.filter(collection_id=fk)
        serializer = FlashcardSerializer(cards, many=True)
        return Response(serializer.data)

    def post(self, request, fk):
        serializer = FlashcardSerializer(data={**request.data, 'collection': fk})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


