import requests
import json

API_URL = 'http://localhost:8000/api/'
headers = {'content-type': 'application/json'}

def create_users(num_users):
    user_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    request_data = {'profiles': []}
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }

    for line in user_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + userid
        age = int(age)
        occupation = occupation_map[int(occupation)]

        request_data['profiles'].append({
            'username': username,
            'password': username,
            'age': age,
            'gender': gender,
            'occupation': occupation
        })

        if len(request_data['profiles']) >= num_users:
            break

    response = requests.post(API_URL + 'auth/signup-many/', data=json.dumps(request_data), headers=headers)
    # print(response)
    # print(request_data)
    # print(response.text)


def create_movies():
    movie_data = open('./movies.dat', 'r', encoding='ISO-8859-1')
    request_data = {'movies': []}
    for line in movie_data.readlines():
        [id, title, genres] = line.split('::')
        genres = genres[:-1].split('|')
        request_data['movies'].append({
            'id': id,
            'title': title,
            'genres': genres
        })


    response = requests.post(API_URL + 'movies/', data=json.dumps(request_data), headers=headers)
    # print(response)
    # print(request_data)
    # print(response.text)


def create_ratings(num_users):
    rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')
    request_data = {'ratings': []}

    for line in rating_data.readlines():
        [user, movieid, rate, timestamp] = line.split('::')
        rate = int(rate)
        timestamp = int(timestamp)
        request_data['ratings'].append({
            'user': user,
            'movieid': movieid,
            'rate': rate,
            'timestamp': timestamp,
        })

        if len(request_data['ratings']) >= num_users:
            break

    response = requests.post(API_URL + 'ratings/', data=json.dumps(request_data), headers=headers)
    # print(response)
    print(request_data)

def create_profiles():
    profile_data = open('./users.dat', 'r', encoding='ISO-8859-1')
    request_data = {'profiles': []}
    occupation_map = {
        0: "other", 1: "academic/educator", 2: "artist", 3: "clerical/admin", 4: "college/grad student",
        5: "customer service", 6: "doctor/health care", 7: "executive/managerial", 8: "farmer", 9: "homemaker",
        10: "K-12 student", 11: "lawyer", 12: "programmer", 13: "retired", 14: "sales/marketing",
        15: "scientist", 16:  "self-employed", 17: "technician/engineer", 18: "tradesman/craftsman",
        19: "unemployed", 20: "writer"
    }
    
    for line in profile_data.readlines():
        [userid, gender, age, occupation, zipcode] = line.split('::')
        username = 'user' + userid
        age = int(age)
        occupation = occupation_map[int(occupation)]

        request_data['profiles'].append({
            'username': username,
            'password': username,
            'age': age,
            'gender': gender,
            'occupation': occupation
        })

    # rating_data = open('./ratings.dat', 'r', encoding='ISO-8859-1')

    # for line in rating_data.readlines():
    #     [user, movieid, rate, timestamp] = line.split('::')
    #     rate = int(rate)
    #     timestamp = int(timestamp)
    #     request_data['profiles'].append({
    #         'movieid': movieid,
    #         'rate': rate,
    #         'timestamp': timestamp,
    #     })
    # # print(request_data)
    response = requests.post(API_URL + 'profiles/', data=json.dumps(request_data), headers=headers)

if __name__ == '__main__':
    num_users = 20
    create_movies()
    create_users(num_users)
    create_ratings(num_users)
    create_profiles()
