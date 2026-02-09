import telebot
import random

user_balance = 2000

bot = telebot.TeleBot("8237489345:AAEyI6TX4HdISkbc5JC5e-Nfp2ClmR65T2w")

markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = telebot.types.KeyboardButton("Казино бот 🎲")
btn2 = telebot.types.KeyboardButton("Ограбить банк 💸")
btn3 = telebot.types.KeyboardButton("Ограбить прохожего 💸")
btn4 = telebot.types.KeyboardButton("Посмотреть баланс")
markup.add(btn1, btn2, btn3, btn4)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите действие: ", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Казино бот 🎲")
def handle_casino(message):
    a = random.randint(1, 12)
    # Ролл без прикосновений к балансу (безсмысленный)
    if a > 7:
        print("ssssssss")
        bot.send_message(message.chat.id, f"Вы выйграли! Вам выпало '{a}'")

@bot.message_handler(func=lambda m: m.text == "Ограбить банк 💸")
def handle_robbery(message):
    bank_robbery = random.randint(1, 5)
    global user_balance
    # Логика ограбления
    # С проверкой баланса
    if user_balance >= 1000:
        if bank_robbery < 3:
            user_balance += 2000
            bot.send_message(message.chat.id, "Вы ограбили банк и заработали 2000$!!")
        elif bank_robbery >= 3:
            bot.send_message(message.chat.id, "Не удалось ограбить банк!")
            user_balance -= 750
        else:
            bot.send_message(message.chat.id, "Низкий баланс (меньше 1000$)")

@bot.message_handler(func=lambda m: m.text == "Ограбить прохожего 💸")
def handle_thief(message):
    thief_random = random.randint(1, 6)
    global user_balance
    # Логика грабежа
    # Не имеет проверки баланса
    if thief_random > 3:
        bot.send_message(message.chat.id, "Вы успешно сбежали, но и не ограбили")
    else:
        bot.send_message(message.chat.id, "Вы ограбили и сбежали")
        user_balance += 1000

@bot.message_handler(func=lambda m: m.text == "Посмотреть баланс")
def handle_balance(message):
    global user_balance
    bot.send_message(message.chat.id, f"Баланс: {user_balance}")

bot.polling(none_stop=True, interval=0)