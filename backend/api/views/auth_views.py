from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.models import create_profile, Profile
from api.serializers import ProfileSerializer

@api_view(['POST'])
def signup_many(request):
    if request.method == 'POST':
        profiles = request.data.get('profiles', None)
        for profile in profiles:
            username = profile.get('username', None)
            password = profile.get('password', None)
            age = profile.get('age', None)
            occupation = profile.get('occupation', None)
            gender = profile.get('gender', None)

            create_profile(username=username, password=password, age=age,
                           occupation=occupation, gender=gender)
        serializer = ProfileSerializer(profiles, many=True)

        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
