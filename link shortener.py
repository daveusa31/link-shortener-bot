####################
#    библиотеки    #
####################

import requests    #библа для запросов в сеть
import json        #библа для расшифровки json ответов


####################
#      токены      #
####################

tg_token = 'your token from @botfather'


####################
#       urlы       #
####################


clck_url = 'https://clck.ru/--?url='

tg_url = 'https://api.telegram.org/bot' + tg_token + '/'                                             #ссылка для запроса к телеграму



###########
#   код   #
###########



def get_update():    #функция для получения последнего обновлениея   
	
	for item in result_list:
		number = item

	result_list.remove(number)

	number = number + 1
	result_list.append(number)



	while True:
		r = requests.get(tg_url + 'getupdates')                          
		data = r.json()  

		try:
			chat_id =      data['result'][number]['message']['chat']['id']          
			message_text = data['result'][number]['message']['text'],
			user_name = data['result'][number]['message']['from']['username'],
			message_id = data['result'][number]['message']['message_id']

			break

		except:

			continue 



	if not chat_id in chatid_list:
		chatid_list.append(chat_id)



	data = {'chat_id'      : chat_id,
			'message_text' : message_text,
			'result'       : number
			}
																	 
																	 #cоздаётся словарь с полученными данными         
	return data



def obrabotka():
	data = get_update()

	chat_id = data['chat_id']
	message_text = data['message_text']
	result = data['result']


	send_message_url = tg_url + 'sendMessage?chat_id=' + str(chat_id) + '&text='

	for i in message_text:

		degg = i

	


	if 'http' in degg:
		

		requests.get(send_message_url + 'Сейчас ваша ссылку будет сокращена')

		r = requests.get(clck_url + degg)

		print(r.url)


		requests.get(send_message_url + 'Вот ваша ссылка\n' + r.text)




while True: 
	obrabotka()





