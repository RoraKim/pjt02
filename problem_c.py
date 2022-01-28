import requests
from pprint import pprint


def ranking():
    pass 
    # 여기에 코드를 작성합니다. 

    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '65e2ff9b7e0eb74cfafc3986ea1f4a30',
    'region': 'KR',
    'language': 'ko'
    }

    response = requests.get(BASE_URL+path, params=params)
    data = response.json()
    # print(response.status_code, response.url)
    my_list = []
    for i in data.get('results'):
        my_list.append(i.get('vote_average'))
        new_list = sorted(my_list)[:-6:-1]
        if 
    # return new_list


if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
