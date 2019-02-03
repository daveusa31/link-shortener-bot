####################
#    библиотеки    #
####################

import requests    #библа для запросов в сеть
import json        #библа для расшифровки json ответов
from time import sleep


####################
#      токены      #
####################

tg_token = 'your bot token from @botfather'


####################
#       urlы       #
####################


clck_url = 'https://clck.ru/--?url='

tg_url = 'https://api.telegram.org/bot' + tg_token + '/'    



###############
#    списки   #
###############

result_list = [3]   #список
chatid_list = []    #список чат айдишников


####################
# дефолтные ответы #
####################


start = 'Здесь будет привественное сообщение'  #это сообщение отправляется, при активации бота
help  = 'Здесь будут все доступные команды'






###########
#   код   #
###########



def get_update():    #функция для получения последнего обновлениея   

	
	for i in updateid_list:
		number = i

	updateid_list.remove(number)

	number = number + 1

	updateid_list.append(number)


	while True:

		r = requests.get(tg_url + 'getupdates?offset=' + str(number))

		data = r.json()  

		

			

		try:
			chat_id =      data['result'][0]['message']['chat']['id'],
			       
			message_text = data['result'][0]['message']['text'],

			user_name = data['result'][0]['message']['from']['username'],

			message_id = data['result'][0]['message']['message_id'],

			update_id = data['result'][0]['update_id']

			break

		except:

			continue 


		
	data = {'chat_id'      : chat_id,
			'message_text' : message_text
			
			}
																	 
																	 #cоздаётся словарь с полученными данными         
	return data





def obrabotka():
	data = get_update()

	chat_id = data['chat_id']
	message_text = data['message_text']
	result = data['result']


	send_message_url = tg_url + 'sendMessage?chat_id=' + str(chat_id) + '&text='

	message_text = message_text[0]

	


	if 'http' in message_text:
		

		requests.get(send_message_url + 'Сейчас ваша ссылку будет сокращена')

		r = requests.get(clck_url + message_text)


		requests.get(send_message_url + 'Вот ваша ссылка\n' + r.text)


	elif '/start' or '/help' in message_text:
		
		if '/start' in message_text:
		
			requests.get(send_message_url + start)
			
		elif '/help' in message_text:
			
			requests.get(send_message_url + help)
			
			
	
			
			
while True: 
	sleep(2)
	obrabotka()
	print(chatid_list)     # логается чат айдишники из списка
	print('В боте', len(chatid_list), 'юзеров') #логается кол-во человек, открывших бот
	print('было получено', result_list 'сообщений') #логается кол-во полученных сообщений





