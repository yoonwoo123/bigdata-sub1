from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import Rating
from api.models import Profile, Movie
from api.serializers import RatingSerializer
from django.contrib.auth.models import User


@api_view(['GET', 'POST', 'DELETE'])
def ratings(request):

    if request.method == 'GET':
        ratings = Rating.objects.all()
        
        serializer = RatingSerializer(ratings, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        Rating.objects.all()
        Rating.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        ratings = request.data.get('ratings', None)
        for rating in ratings:
            user = rating.get('user', None)
            movieid = rating.get('movieid', None)
            score = rating.get('score', None)
            timestamp = rating.get('timestamp', None)

            Rating(user=User.objects.get(pk=user), movie_id=Movie.objects.get(pk=movieid), rate=rate, timestamp=timestamp).save()

        return Response(status=status.HTTP_200_OK)
#.save() ?