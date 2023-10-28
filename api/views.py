# from django.shortcuts import render
from rest_framework import generics
from .models import Todo
from .serializer import TodoSerializer

# Create your views here.

# get post update and dlt
class TodoGetCreate(generics.ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

class TodoUpdateDlt(generics.RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer