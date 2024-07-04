from django.contrib.auth.models import AbstractUser
from django.db import models


class RegisterModel(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'register'
        verbose_name_plural = 'registers'


class MovieModel(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    description = models.TextField()
    rating = models.FloatField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'movie'
        verbose_name_plural = 'movies'


class ReviewModel(models.Model):
    rating = models.FloatField()
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movies = models.ForeignKey(MovieModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'review'
        verbose_name_plural = 'reviews'