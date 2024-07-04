from rest_framework import serializers

from authentication.models import RegisterModel, MovieModel, ReviewModel


class RegisterSerializer(serializers.ModelSerializer):
    model = RegisterModel
    fields = ['id', 'username', 'password', 'email']


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieModel
        fields = ['id', 'title', 'genre', 'release_year', 'description', 'rating']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = ['id', 'movies', 'rating', 'comment', 'created_at']