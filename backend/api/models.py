from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, default='M')
    age = models.IntegerField(default=25)
    occupation = models.CharField(max_length=200)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    genres = models.CharField(max_length=500)
    view_users = models.ManyToManyField(Profile, related_name='user_views')
    view_cnt = models.IntegerField(default=0)
    avg_rate = models.FloatField(default=0)

    @property
    def genres_array(self):
        return self.genres.strip().split('|')
def create_movie(**kwargs):
    movie = Movie.objects.create(
        id = kwargs['id'],
        title = kwargs['title'],
        genres = kwargs['genres'],
        view_cnt = kwargs['view_cnt']
    )
    return movie
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    score = models.IntegerField(default=1)
    timestamp = models.IntegerField(default=0)


#  wrapper for create user Profile
def create_profile(**kwargs):

    user = User.objects.create_user(
        username=kwargs['username'],
        password=kwargs['password'],
        is_active=True,
    )

    profile = Profile.objects.create(
        user=user,
        gender=kwargs['gender'],
        age=kwargs['age'],
        occupation=kwargs['occupation']
    )

    return profile



