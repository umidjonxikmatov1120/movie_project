from django.shortcuts import render
from rest_framework import permissions, generics
from rest_framework.generics import CreateAPIView, ListAPIView

from authentication.custom_pagination import CustomPagination
from authentication.models import RegisterModel, MovieModel, ReviewModel
from authentication.serializers import RegisterSerializer, MoviesSerializer, ReviewSerializer


class RegisterCreateView(CreateAPIView):
    queryset = RegisterModel.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = RegisterSerializer


class MovieListView(ListAPIView):
    queryset = MovieModel.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MoviesSerializer
    pagination_class = CustomPagination

class MovieCreateView(CreateAPIView):
    queryset = MovieModel.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MoviesSerializer


class MovieRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieModel.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = MoviesSerializer


class ReviewListView(ListAPIView):
    queryset = ReviewModel.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination

class ReviewCreateView(CreateAPIView):
    queryset = ReviewModel.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewModel.objects.all()
    permission_classes = [permissions.AllowAny, ]
    serializer_class = ReviewSerializer