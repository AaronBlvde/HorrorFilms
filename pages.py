import requests
from bs4 import BeautifulSoup

def MovieScraper(star_rating):
    for i in range(1, 697, 50):
        url = f'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=horror&sort=user_rating,desc&start={i}&ref_=adv_nxt'
        response = requests.get(url=url).content
        soup = BeautifulSoup(response, 'lxml')

        movie_details = soup.find_all('div', {'class': 'lister-item mode-advanced'})
        for movie in movie_details:
            movie_name = movie.find('h3', {'class': 'lister-item-header'}).text.replace('\n', '')
            movie_rating = movie.find('div', {'class': 'inline-block ratings-imdb-rating'}).text.strip()
            movie_describe = movie.find_all('p', class_='text-muted')[1].text

            if float(movie_rating) >= star_rating and float(movie_rating) < star_rating + 1:
                yield movie_name, movie_rating, movie_describe


if __name__=='__main__':
    start = print('Здесь вы можете найти хоррор-фильмы по нужному рейтингу по шкале от 1 до 10.')
    start1 = print('Если фильмы не нашлись, значит фильмов с таким рейтингом нет.')
    start2 = print('Поиск будет совершаться по базе imdb.Удачного поиска :)')
    rating = float(input('\nВведите рейтинг: '))
    waiting = print('Пожалуйста, подождите. Достаём данные с сайта imdb...')
    for movie_name, star_rating, movie_describe in MovieScraper(rating):
        print('\nНазвание фильма:', movie_name)
        print('Рейтинг:', star_rating)
        print('Описание фильма:', movie_describe)
        print()
