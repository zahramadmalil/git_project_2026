import requests


def get_movie_info_by_id(movie_id):
    try:
        url = f'https://moviesapi.ir/api/v1/movies/{movie_id}'
        response = requests.get(url)
        if response.status_code != 200:
            return 'ERROR'
        else:
            response = response.json()
            title = response['title']
            country = response['country']
            director = response['director']
            year = response['year']
            imdb_rate = response['imdb_rating']
            plot = response.get('plot', 'ندارد')
            actors = response.get('actors', 'ندارد')
            genres = response.get('genres', [])
            poster = response.get('poster', '')

            return (title, country, director, year, imdb_rate, plot, actors, genres, poster)
    except Exception as e:
        return 'ERROR'



def get_movie_info_by_name(movie_name):
    try:
        url = f'https://moviesapi.ir/api/v1/movies'
        params_dict = {
            'q': movie_name
        }
        response = requests.get(url, params=params_dict)
        if response.status_code != 200:
            return 'ERROR'
        else:
            response = response.json()
            data_list = response.get('data', [])
            if not data_list:
                return 'EMPTY'

            
            results = []
            for movie in data_list:
                movie_data = {
                    'id': movie['id'],
                    'title': movie['title'],
                    'year': movie.get('year', 'نامشخص'),
                    'country': movie.get('country', 'نامشخص'),
                    'imdb_rate': movie.get('imdb_rating', 'نامشخص'),
                    'genres': movie.get('genres', []),
                    'poster': movie.get('poster', '')
                }
                results.append(movie_data)

            return results
    except Exception as e:
        return 'ERROR'


def get_popular_movies(page=1):
    try:
        url = f'https://moviesapi.ir/api/v1/movies'
        params_dict = {
            'page': page
        }
        response = requests.get(url, params=params_dict)
        if response.status_code != 200:
            return 'ERROR'
        else:
            response = response.json()
            data_list = response.get('data', [])
            if not data_list:
                return 'EMPTY'

            
            results = []
            for movie in data_list:
                movie_data = {
                    'id': movie['id'],
                    'title': movie['title'],
                    'year': movie.get('year', 'نامشخص'),
                    'genres': movie.get('genres', []),
                    'poster': movie.get('poster', '')
                }
                results.append(movie_data)

            return results
    except Exception as e:
        return 'ERROR'


if __name__ == '__main__':
    movie_name = input('enter movie name: ')
    result = get_movie_info_by_name(movie_name)
    print(f'result: {result}')
