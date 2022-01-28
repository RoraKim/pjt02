import requests
from pprint import pprint


def popular_count():
    pass 
    # 여기에 코드를 작성합니다.  
    
    BASE_URL = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '65e2ff9b7e0eb74cfafc3986ea1f4a30',
    }

    response = requests.get(BASE_URL+path, params=params)
    data = response.json()

#print(type(data)) # dict
# print(type(data.get('results'))) #list
    return len(data.get('results')) #20





if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
