from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BookSerializer
from .models import Book

# Create your views here.

class BookView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serilizer = BookSerializer(data= books)
        return Response(serilizer.data)

