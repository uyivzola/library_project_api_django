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

class BookDeleteApiView(generics.DestroyAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer

class BookUpdateView(generics.UpdateAPIView):
    queryset=Book.objects.all()
    serializer_class=BookSerializer
