import telebot
from telebot import types
from .models import TelegramBot
from client_app.models import SessionRecord
class GetSessions:
    def get_all_session(self):
        try:
            sessions = SessionRecord.objects.all()
            return sessions
        except SessionRecord.DoesNotExist:
            return None

class GetBotSettings:
    def get_telegram_token(self):
        try:
            bot_token = TelegramBot.objects.first()
            return bot_token.telegram_token
        except TelegramBot.DoesNotExist:
            return None
    def get_telegram_chat_id(self):
        try:
            bot_token = TelegramBot.objects.first()
            return bot_token.chat_id
        except TelegramBot.DoesNotExist:
            return None

bot_settings = GetBotSettings()
bot = telebot.TeleBot(bot_settings.get_telegram_token())


@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    mess = f' {chat_id}'
    bot.send_message(message.chat.id, mess)
@bot.message_handler(commands=['menu'])
def set_menu(message):
    chat_id = message.chat.id
    murkup_inline = types.InlineKeyboardMarkup()
    session = types.InlineKeyboardButton(text='Cессії', callback_data='get_all_sessions')
    client = types.InlineKeyboardButton(text='Клієнти', callback_data='get_all_sessions')
    murkup_inline.add(session, client)
    bot.send_message(chat_id,'Меню', reply_markup=murkup_inline)
@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    if call.data=='get_all_sessions':
        murkup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        sessions_today = types.KeyboardButton('Список сессій на сьогодні')
        all_sessions = types.KeyboardButton('Всі сессії')
        murkup_reply.add(sessions_today,all_sessions)
        bot.send_message(call.message.chat.id,"Натисни кнопку", reply_markup=murkup_reply)
@bot.message_handler(content_types=['text'])
def get_sessions(message):
    if message.text == 'Всі сессії':
        session_manager = GetSessions()  # Створити екземпляр класу GetSessions
        sessions = session_manager.get_all_session()  # Викликати метод для отримання сесій
        if sessions:
            text = "Список всіх сесій:\n"
            for session in sessions:
                text += f"Ім'я: {session.client.user.first_name} Дата сессії :{session.session_date} Час сессії: {session.session_time} Статус: {session.status}\n"
            bot.send_message(message.chat.id, text)
        else:
            bot.send_message(message.chat.id, "Сесій не знайдено")

@bot.message_handler()
def SendInformationForm(name, phone_number, description="", telegram=''):
    chat_id = bot_settings.get_telegram_chat_id()
    information = f'Отримані дані з сайту : \n Імя : {name} \n Телеграм: {telegram} \n Номер телефону: {phone_number} \n Опис проблеми: {description}'
    bot.send_message(chat_id, information)

