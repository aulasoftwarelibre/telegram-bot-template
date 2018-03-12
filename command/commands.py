# coding=utf-8
import requests
import os
from hackathon import bot
from telebot import util


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(commands=['change'])
def change(message):
    """
    Ejemplo de API abierta

    Usa la API definida en https://bitcoincharts.com/about/markets-api/
    para saber el tipo de cambio de una moneda
    :param message:
    :return:
    """
    exchange = util.extract_arguments(message.text).upper()
    if not exchange:
        bot.reply_to(message, "Debe indicar un tipo de cambio. Ej.: EUR, USD, ...")
        return

    # request.get(url).json() Devuelve los datos de una API pública
    response = requests.get('http://api.bitcoincharts.com/v1/weighted_prices.json').json()
    if exchange not in response:
        bot.reply_to(message, "No se ha encontrado el tipo de cambio")
        return

    bot.reply_to(message, "Un bitcoin equivale a %s %s" % (response[exchange]['24h'], exchange))


@bot.message_handler(commands=['weather'])
def weather(message):
    """
    Ejemplo de API con Token en la URL

    Usa la API definida en https://openweathermap.org/current para conocer el tiempo
    en una ciudad
    """
    weather_token = os.environ.get('OPENWEATHER_TOKEN', False)
    if not weather_token:
        bot.reply_to(message, "Debe configurarse el token de openweather")
        return

    city = util.extract_arguments(message.text).upper()
    if not city:
        bot.reply_to(message, "Debe indicar una ciudad")
        return

    url = 'https://api.openweathermap.org/data/2.5/weather?q=%s,es&lang=sp&units=metric&APPID=%s' % (city, weather_token)
    response = requests.get(url=url)

    if response.status_code is not requests.codes.ok:
        bot.reply_to(message, "Error al consultar el tiempo")
        return

    data = response.json()
    bot.reply_to(message, "La temperatura es de %sºC" % data['main']['temp'])


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    """
    Hace un 'eco' de lo que se recibe y no se ha procesado en algún comando anterior.
    :param message:
    :return:
    """
    bot.reply_to(message, message.text)
