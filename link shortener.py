####################
#    библиотеки    #
####################

import requests
import telebot    
####################
#      токены      #
####################

token = 'your bot token from @botfather'


####################
#       urlы       #
####################


clck_url = 'https://clck.ru/--?url='


###############
#    списки   #
###############

chatid_list = []    #список чат айдишников


####################
# дефолтные ответы #
####################


start = 'Здесь будет привественное сообщение'  #это сообщение отправляется, при активации бота
help  = 'Здесь будут все доступные команды'
###########
#   код   #
###########

@bot.message_handler(commands=['start', 'help'])
def handle_start(message):
	if '/start' in message.text: bot.send_message(message.from_user.id, start)
	elif '/help' in message.text: bot.send_message(message.from_user.id, help)
@bot.message_handler(content_types=["text"])
def message_send228(message):
	if message.from_user.id not in chatid_list:
		chatid_list.append(message.from_user.id)
		print(chatid_list)

	if 'http' in message_text:
		bot.send_message(message.from_user.id, 'Сейчас ваша ссылка будет сокращена')
		r = requests.get(clck_url + message_text)
		bot.send_message(message.from_user.id, 'Вот ваша ссылка\n' + r.text)

if __name__ == '__main__':
	bot.infinity_polling()





	


			


