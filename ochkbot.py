###importing telebot API - will need only this
import telebot

###our token and bot init
bot = telebot.TeleBot("MAH:TOKEN")



###handler for start and help command
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
        bot.send_message(message.chat.id, "Дратути! \nЭтот бот создан для обратной связи с каналом Очко Баяна - https://t.me/ochkobayanachannel \nВы таки хочете нам шо-то сказать? \nПошлите нам что угодно - картинку, видосик, ссылочку, стикер - даже просто пожелания, и в$



yopta = ['ДА', 'ДАА', 'ДААА', 'YES', 'АГА', 'ЫЫЫ', 'Ы', 'DA', 'DAA', 'DAAA']




###simple about_us info
@bot.message_handler(commands=['about', 'wassup'])
def send_info (message):
        bot.send_message(message.chat.id, "Команда упоротых адептов Мемологии, поклоняющихся Баяну, Паше Дурову и святому духу Прокрастинаци и желающих провернуть фсосайети по-азербайджански. С нами вкусно, кислотно и трешово, будь на связи! \n \nБот написан и протестиро$



###handler for everything text - forwards message to admins
@bot.message_handler(content_types=['text'])
def echo_text(message):
        if message.text.upper() in yopta:
                bot.send_message(message.chat.id, 'Спасибо ёпта :3')
                bot.forward_message(95065439, message.chat.id, message.message_id)###Anvar
                bot.forward_message(1761842, message.chat.id, message.message_id)###Ley
                bot.forward_message(10347651, message.chat.id, message.message_id)###Ramin
                bot.forward_message(3145750, message.chat.id, message.message_id)###Ayk
                bot.forward_message(2160766, message.chat.id, message.message_id)###Lyaman
                bot.forward_message(32924407, message.chat.id, message.message_id)###Ays
                bot.forward_message(1699110, message.chat.id, message.message_id)###Oktay
                bot.forward_message(74677266, message.chat.id, message.message_id)###Hafiz
                bot.forward_message(68680, message.chat.id, message.message_id)###Sinan
        else:
                bot.send_message(message.chat.id, "Мы получили ваше сообщение, спасибо! \nЕсли вы хотите чтоб мы упомянули вас - ответьте ДА")
                bot.forward_message(95065439, message.chat.id, message.message_id)###Anvar
                bot.forward_message(1761842, message.chat.id, message.message_id)###Ley
                bot.forward_message(10347651, message.chat.id, message.message_id)###Ramin
                bot.forward_message(3145750, message.chat.id, message.message_id)###Ayk
                bot.forward_message(2160766, message.chat.id, message.message_id)###Lyaman
                bot.forward_message(32924407, message.chat.id, message.message_id)###Ays
                bot.forward_message(1699110, message.chat.id, message.message_id)###Oktay
                bot.forward_message(74677266, message.chat.id, message.message_id)###Hafiz
                bot.forward_message(68680, message.chat.id, message.message_id)###Sinan





###handler for everything except stickers - forwards message to admins
@bot.message_handler(content_types=['photo', 'document', 'audio', 'voice', 'video_note', 'location'])
def echo_pic(message):
        bot.send_message(message.chat.id, "Мы получили ваше сообщение, спасибо! \nЕсли вы хотите чтоб мы упомянули вас - ответьте ДА")
        bot.forward_message(95065439, message.chat.id, message.message_id)###Anvar
        bot.forward_message(1761842, message.chat.id, message.message_id)###Ley
        bot.forward_message(10347651, message.chat.id, message.message_id)###Ramin
        bot.forward_message(3145750, message.chat.id, message.message_id)###Ayk
        bot.forward_message(2160766, message.chat.id, message.message_id)###Lyaman
        bot.forward_message(32924407, message.chat.id, message.message_id)###Ays
        bot.forward_message(1699110, message.chat.id, message.message_id)###Oktay
        bot.forward_message(74677266, message.chat.id, message.message_id)###Hafiz
        bot.forward_message(68680, message.chat.id, message.message_id)###Sinan

			 
###separate handler for stickers as it is not visible whom is sticker forwarded from - asks for additional info
@bot.message_handler(content_types=['sticker'])
def echo_all(message):
        bot.send_message(message.chat.id, "Так как вы прислали стикер - напишите пару слов о нем, чтоб мы знали что с ним делать")
        bot.forward_message(95065439, message.chat.id, message.message_id)
        bot.forward_message(1761842, message.chat.id, message.message_id)
        bot.forward_message(10347651, message.chat.id, message.message_id)
        bot.forward_message(3145750, message.chat.id, message.message_id)
        bot.forward_message(2160766, message.chat.id, message.message_id)
        bot.forward_message(32924407, message.chat.id, message.message_id)
        bot.forward_message(1699110, message.chat.id, message.message_id)
        bot.forward_message(74677266, message.chat.id, message.message_id)
        bot.forward_message(68680, message.chat.id, message.message_id)



###line below can be used for user name retrieval
#+'\n'+message.from_user.first_name)
###yes you probably ask why don't I use this for sticker handling
### well, fuck you, that's why

###poll
bot.polling()
