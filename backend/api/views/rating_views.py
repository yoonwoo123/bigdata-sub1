from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Rating
from api.models import Profile, Movie
from django.contrib.auth.models import User


@api_view(['POST'])
def ratings(request):

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
        for rating in ratings:
            user = rating.get('user', None)
            movieid = rating.get('movieid', None)
            rate = rating.get('rate', None)
            timestamp = rating.get('timestamp', None)

            Rating(user=User.objects.get(pk=user), movie_id=Movie.objects.get(pk=movieid), rate=rate, timestamp=timestamp).save()

        return Response(status=status.HTTP_201_CREATED)
#.save() ?