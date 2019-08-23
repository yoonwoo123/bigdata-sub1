from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Profile
from api.serializers import ProfileSerializer
from rest_framework.response import Response


@api_view(['GET', 'POST', 'DELETE'])
def profiles(request):

    if request.method == 'GET':
        user = request.GET.get('user', request.GET.get('user', None))
        title = request.GET.get('title', None)

        profiles = Profile.objects.all()

        serializer = ProfileSerializer(profiles, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        Profile.objects.all()
        profile.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        profiles = request.data.get('profiles', None)
        for profile in profiles:
            user = profile.get('user', None)
            gender = profile.get('gender', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            

            if not (user and gender and age):
                continue

            Profile(user=user, gender=gender, age=age, occupation=occupation).save()

        return Response(status=status.HTTP_200_OK)
