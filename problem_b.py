import requests
from pprint import pprint


def vote_average_movies():
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
        if i.get('vote_average') >= 8:
            my_list.append(i)
    return my_list



if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
