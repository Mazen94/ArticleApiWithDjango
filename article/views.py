from django.shortcuts import render
from rest_framework import generics
from .models import Article
from .serializers import NotesSerializer
from rest_framework import viewsets
        
class ArticleView(viewsets.ModelViewSet):      
  serializer_class = NotesSerializer          
  queryset = Article.objects.all()  