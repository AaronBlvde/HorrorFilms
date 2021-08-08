import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests
import random

bot = telebot.TeleBot('Token')

number = random.randint(1, 697)


def MovieScraper(num):
    url = f'https://www.imdb.com/search/title/?title_type=feature&num_votes=25000,&genres=horror&sort=user_rating,desc&start={num}&ref_=adv_nxt'
    print(url)
    response = requests.get(url=url).content
    soup = BeautifulSoup(response, 'lxml')

    movie_details = soup.find_all('div', {'class': 'lister-item mode-advanced'})

    text = soup.find('div', class_='lister-item-image float-left')
    links_with_text = [a['href'] for a in text.find_all('a', href=True) if a.text]

    for movie in movie_details:
        movie_name = movie.find('h3', {'class': 'lister-item-header'}).text.replace('\n', '')
        movie_rating = movie.find('div', {'class': 'inline-block ratings-imdb-rating'}).text.strip()
        movie_describe = movie.find_all('p', class_='text-muted')[1].text

        result_name = 'Название фильма: ' + movie_name.split('.', 1)[1] + '\nРейтинг: ' + movie_rating + '\nОписание: '+ '\n' + movie_describe

        return result_name, *links_with_text


def imagescrapper(url):
    site = 'https://www.imdb.com/'+url
    return site


@bot.message_handler(commands=["start"])
def keyboard (message):
    key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key.row("Посоветовать хоррор")
    bot.send_message(message.chat.id, "Выберите действие",reply_markup=key)

@bot.message_handler(content_types=["text"])
def main(message):
    if message.text == "Посоветовать хоррор":
        bot.send_message(message.chat.id, MovieScraper(number)[0])
        bot.send_message(message.chat.id, imagescrapper(MovieScraper(number)[1]))


if __name__ == "__main__":

    bot.polling(none_stop=True, interval=0)