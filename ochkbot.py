###importing telebot API - will need only this
import telebot

###our token and bot init
bot = telebot.TeleBot("MAH_TOKEN")


###handler for start and help command
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Дратути! \nЭтот бот создан для обратной связи с каналом Очко Баяна - https://t.me/ochkobayanachannel \nВы таки хочете нам шо-то сказать? \nПошлите нам что угодно - картинку, видосик, ссылочку, стикер - даже просто пожелания, и возможно мы их опубликуем!\n*ноэтонеточно*")

	
yopta = ['ДА', 'ДАА', 'ДААА', 'YES', 'АГА', 'ЫЫЫ', 'Ы', 'DA', 'DAA', 'DAAA']




###simple about_us info
@bot.message_handler(commands=['about', 'wassup'])
def send_info (message):
        bot.send_message(message.chat.id, "Команда упоротых адептов Мемологии, поклоняющихся Баяну, Паше Дурову и святому духу Прокрас$



###handler for everything except stickers - forwards message to admins
@bot.message_handler(content_types=['photo', 'document', 'audio', 'voice', 'text', 'video_note', 'location'])
def echo_pic(message):
        if message.text.upper() in yopta:
                bot.send_message(message.chat.id, 'Спасибо ёпта :3')
		bot.forward_message(admin1_chat_id, message.chat.id, message.message_id)###Admin1
 		bot.forward_message(admin2_chat_id, message.chat.id, message.message_id)###Admin2
		bot.forward_message(admin3_chat_id, message.chat.id, message.message_id)###Admin3
		bot.forward_message(admin4_chat_id, message.chat.id, message.message_id)###Admin4
		bot.forward_message(admin5_chat_id, message.chat.id, message.message_id)###Admin5
		bot.forward_message(admin6_chat_id, message.chat.id, message.message_id)###Admin6
		bot.forward_message(admin7_chat_id, message.chat.id, message.message_id)###Admin7
		bot.forward_message(admin8_chat_id, message.chat.id, message.message_id)###Admin8
		bot.forward_message(admin9_chat_id, message.chat.id, message.message_id)###Admin9
        else:
             	bot.send_message(message.chat.id, "Мы получили ваше сообщение, спасибо! \nЕсли вы хотите чтоб мы упомянули вас - ответ$
		bot.forward_message(admin1_chat_id, message.chat.id, message.message_id)###Admin1
 		bot.forward_message(admin2_chat_id, message.chat.id, message.message_id)###Admin2
		bot.forward_message(admin3_chat_id, message.chat.id, message.message_id)###Admin3
		bot.forward_message(admin4_chat_id, message.chat.id, message.message_id)###Admin4
		bot.forward_message(admin5_chat_id, message.chat.id, message.message_id)###Admin5
		bot.forward_message(admin6_chat_id, message.chat.id, message.message_id)###Admin6
		bot.forward_message(admin7_chat_id, message.chat.id, message.message_id)###Admin7
		bot.forward_message(admin8_chat_id, message.chat.id, message.message_id)###Admin8
		bot.forward_message(admin9_chat_id, message.chat.id, message.message_id)###Admin9
  
  
  
###separate handler for stickers as it is not visible whom is sticker forwarded from - asks for additional info
@bot.message_handler(content_types=['sticker'])
def echo_all(message):
	bot.send_message(message.chat.id, "Так как вы прислали стикер - напишите пару слов о нем, чтоб мы знали что с ним делать")
	bot.forward_message(admin1_chat_id, message.chat.id, message.message_id)###Admin1
 	bot.forward_message(admin2_chat_id, message.chat.id, message.message_id)###Admin2
	bot.forward_message(admin3_chat_id, message.chat.id, message.message_id)###Admin3
	bot.forward_message(admin4_chat_id, message.chat.id, message.message_id)###Admin4
	bot.forward_message(admin5_chat_id, message.chat.id, message.message_id)###Admin5
	bot.forward_message(admin6_chat_id, message.chat.id, message.message_id)###Admin6
	bot.forward_message(admin7_chat_id, message.chat.id, message.message_id)###Admin7
	bot.forward_message(admin8_chat_id, message.chat.id, message.message_id)###Admin8
	bot.forward_message(admin9_chat_id, message.chat.id, message.message_id)###Admin9



###line below can be used for user name retrieval
#+'\n'+message.from_user.first_name)
###yes you probably ask why don't I use this for sticker handling
### well, fuck you, that's why

###poll
bot.polling()
