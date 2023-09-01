from django.shortcuts import render

from .models import Book, Category
from .serializers import BookSerializer, CategorySerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


class BookListApiView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailApiView(generics.RetrieveAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

# Function based view way
@api_view(['GET'])
def book_list_view(request, *args, **kwargs):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    
    return Response(serializer.data)
