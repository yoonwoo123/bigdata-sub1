from django.conf.urls import url
from django.urls import path
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views
from api.views import movie_genres

urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.ratings, name="ratings"),
    path('movies/<str:genre>/$', movie_genres.genres, name="genres"),
]
