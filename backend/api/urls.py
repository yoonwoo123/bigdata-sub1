from django.conf.urls import url
from django.urls import path
from api.views import movie_views
from api.views import auth_views
from api.views import rating_views
from api.views import movie_genres
from api.views import profile_views


urlpatterns = [
    url('auth/signup-many/$', auth_views.signup_many, name='sign_up_many'),
    url('movies/$', movie_views.movies, name='movie_list'),
    url('ratings/$', rating_views.ratings, name="ratings"),
    url('profiles/$', profile_views.profiles, name='profile_list'),
    path('movies/rating/', movie_views.movie_rating, name="movie_rating"),
    path('movies/view/<int:movie_pk>',movie_views.movie_detail,name="movie_detail"),
    path('movies/views/',movie_views.movie_viewlist,name="movie_viewslist"),
    # path('movies/<str:genre>/$', movie_genres.genres, name="genres"),
]
