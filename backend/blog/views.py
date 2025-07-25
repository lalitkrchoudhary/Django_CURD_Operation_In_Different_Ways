from django.shortcuts import render
from rest_framework import generics
from .models import Blog,Comment
from .serializers import BlogSerializer,CommentSerializer

# Create your views here.

class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentsView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class=BlogSerializer
    lookup_field='pk'

class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    lookup_field='pk'


