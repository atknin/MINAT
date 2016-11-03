# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import requests
from pprint import pprint
import pyowm

API = '00b44104942478082bd6d7cc3142dc86'

def funct(a,chat_id,bot):
	if a == 'знаю':
		bot.send_message(chat_id, 'время, дата, погода')

	# strftime("%d-%m-%Y %H:%M")
	elif a == 'время':
		bot.send_message(chat_id, datetime.datetime.now().strftime("%H:%M"))
	elif a == 'дата':
		bot.send_message(chat_id, datetime.datetime.now().strftime("%d/%m"))	
	elif a == 'погода':
		owm = pyowm.OWM(API)
		observation = owm.weather_at_place('Moscow,ru')
		tomorrow = pyowm.timeutils.tomorrow()
		forecast = owm.daily_forecast("Moscow,ru")
		w = observation.get_weather()
		# r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Moscow&APPID='+API)
		# print(r.json())
		bot.send_message(chat_id, 'градусы: ' + str(w.get_temperature('celsius')['temp']))
		bot.send_message(chat_id, 'ветер: '+ str(w.get_wind()['speed']))
		bot.send_message(chat_id, 'влажность: '+ str(w.get_humidity()))
		bot.send_message(chat_id, 'давление: '+ str(round((w.get_pressure()['press']/1013.25*760),2))+' мм.рт.ст.')
		bot.send_message(chat_id, 'снег/дождь/облака: '+ str(w.get_snow())+ '/'+str(w.get_rain())+ '/'+str(w.get_clouds()))
		if forecast.will_be_sunny_at(tomorrow)!=False:
			bot.send_message(chat_id, 'Завтра солнечно)')
	

