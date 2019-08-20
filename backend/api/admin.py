from django.contrib import admin
from api.models import Rating, Profile, Movie
from django.contrib.auth.models import User

admin.site.register(Rating)
admin.site.register(Profile)
admin.site.register(Movie)