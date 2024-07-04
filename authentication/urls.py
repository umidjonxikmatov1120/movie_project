from django.urls import path

from authentication.views import RegisterCreateView, MovieCreateView, MovieRetrieveUpdateDeleteView, MovieListView, \
    ReviewListView, ReviewRetrieveUpdateDeleteView

urlpatterns = [
    path('signup/', RegisterCreateView.as_view()),
    path('movies/', MovieListView.as_view()),
    path('movies/create', MovieCreateView.as_view()),
    path('movies/<int:pk>/', MovieRetrieveUpdateDeleteView.as_view()),

    path('reviews/', ReviewListView.as_view()),
    path('reviews/create', RegisterCreateView.as_view()),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDeleteView.as_view()),
]