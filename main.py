import requests
from bs4 import BeautifulSoup

def MovieScraper(star_rating):
    url = 'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=horror&sort=moviemeter,desc'
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
    rating = float(input('Введите рейтинг: '))
    for movie_name, star_rating, movie_describe in MovieScraper(rating):
        print('Название фильма:', movie_name)
        print('Рейтинг:', star_rating)
        print('Описание фильма:', movie_describe)
        print()
