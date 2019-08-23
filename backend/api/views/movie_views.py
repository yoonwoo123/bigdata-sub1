from rest_framework import status
from rest_framework.decorators import api_view
from api.models import Movie, Rating
from api.serializers import MovieSerializer
from rest_framework.response import Response
from django.db.models import Avg

@api_view(['GET', 'POST', 'DELETE'])
def movies(request):

    if request.method == 'GET':
        id = request.GET.get('id', request.GET.get('movie', None))
        title = request.GET.get('title', None)

        movies = Movie.objects.all()

        if id:
            movies = movies.filter(pk=id)
        if title:
            movies = movies.filter(title__icontains=title)

        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        movie = Movie.objects.all()
        movie.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'POST':
        movies = request.data.get('movies', None)
        for movie in movies:
            id = movie.get('id', None)
            title = movie.get('title', None)
            genres = movie.get('genres', None)

            if not (id and title and genres):
                continue
            if Movie.objects.filter(id=id).count() > 0 or Movie.objects.filter(title=title).count() > 0:
                continue

            Movie(id=id, title=title, genres='|'.join(genres)).save()

        return Response(status=status.HTTP_200_OK)

# 평균 평점 순으로 정렬
@api_view(['GET', 'POST', 'DELETE'])
def movie_rating(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        for movie in movies:
            ratings = Rating.objects.filter(movie=movie.id) # 다중 행이기 때문에 filter
            avg = ratings.aggregate(avg_rate=Avg('score'))  # 평균값 출력
            if(avg["avg_rate"]==None):
                continue
            
            movie.avg_rate = round(avg["avg_rate"], 2) # 반올림
            movie.save()

        movies = movies.order_by('-avg_rate')
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

# 영화 상세 화면
@api_view(['GET'])
def movie_detail(request, movie_pk):
    if request.method == 'GET':
        movie = Movie.objects.get(id=movie_pk)
        movie.view_cnt += 1
        movie.save()
        print('조회수 증가')
        # movie_users = movie.rating_set.all()

        # for user in movie_users:
        #     profile = user.userid
        #     movie.view_users.add(profile)

        serializer = MovieSerializer(movie)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

# 조회수 순으로 정렬
@api_view(['GET', 'POST', 'DELETE'])
def movie_viewlist(request):
    if request.method == 'GET':
        movies = Movie.objects.all().order_by('-view_cnt')   
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)