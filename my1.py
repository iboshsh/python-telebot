import telebot
from telebot import types

#5396404909:AAHoln7mbrXCVDlrHEQxpItB-DDQejKk5a4

name = ''
surname = ''
age = 0
bot = telebot.TeleBot("5396404909:AAHoln7mbrXCVDlrHEQxpItB-DDQejKk5a4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Salom':
        bot.reply_to(message, 'Salom Jora')
    elif message.text == 'Assalomu aleykum':
        bot.reply_to(message, 'Vaaleykum assalom, nima gap')
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Salom, keling tanishamiz. Ismingiz nima?")
        bot.register_next_step_handler(message, reg_name)
	#bot.reply_to(message, message.text)

def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, "Familiyangiz?")
    bot.register_next_step_handler(message, reg_surname)

def reg_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, "Yoshingiz nechchida?")
    bot.register_next_step_handler(message, reg_age)

def reg_age(message):
    global age
    #age = message.text
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id,"Raqamlar bilan kirting")

    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Ha', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Yoq', callback_data='no')
    keyboard.add(key_no)
    question = "Siz " + str(age) + ' yoshdamisiz? Sizning ismingiz va familiyangiz: ' + name + ' ' + surname + 'mi?'
    bot.send_message(message.from_user.id, text = question, reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == 'yes':
        bot.send_message(call.message.chat.id, "Tanishganimdan hursandman! Endi Sizni ma'lumotlar bazasiga kiritib qo'ydim")
    elif call.data == 'no':
        bot.send_message(call.message.chat.id, "Keling yana bir marotaba qaytaramiz")
        bot.send_message(call.message.chat.id, "Salom, keling tanishamiz. Ismingiz nima?")
        bot.register_next_step_handler(call.message.chat, reg_name)

bot.infinity_polling()