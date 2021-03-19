import telebot
from telebot import types
import time
import random
from time import sleep


bot = telebot.TeleBot("")
dead = 999


def main():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Мой баланс')
    key2 = types.KeyboardButton('Купить кошелёк')
    markup.add(key1)
    markup.add(key2)
    return markup

def kali():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('1 товар (400руб)')
    key2 = types.KeyboardButton('2 товар (600руб)')
    key3 = types.KeyboardButton('3 товар (1500руб)')
    key4 = types.KeyboardButton('4 товар (3500руб)')
    key5 = types.KeyboardButton('Exit')
    markup.add(key1)
    markup.add(key2)
    markup.add(key3)
    markup.add(key4)
    markup.add(key5)
    return markup
def main1():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton('Проверить поступление на счёт')
    key2 = types.KeyboardButton('Назад')
    markup.add(key1)
    markup.add(key2)
    return markup
def main2():
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(' ')
    markup.add(key1)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, """Привет я бот который продаст тебе хороший кошелёк с балансом. 
Обязательно при покупке напиши в комментарий номер товара.Номер товара получишь при оформлении заказа""", reply_markup=main())


@bot.message_handler(content_types=['text'])
def cont(message):
    if message.text == 'Мой баланс':
        bot.send_message(message.chat.id, "Ваш баланс состовляет: 0 рублей", reply_markup=main())
    elif message.text == 'Купить кошелёк':
        bot.send_message(message.chat.id, """Все кошельки проверены на валид.
QiwiWallet - в наличие 43 аккаунта

Кошелёк с балансом 500-1000 руб  -  400 руб (13 кошельков)       

Кошелёк с балансом 800-1500 руб  -  600 руб (6 кошельков)        

Кошелёк с балансом 2000-3000 Руб - 1500 руб (11 кошельков)       

Кошелёк с балансом 5000-8000 руб - 3500 руб (13 кошельков)       

При покупке кошелька вы получаете запароленный архив. 
В нём находится Логин:пароль
Серия и номер паспорта. 
Прокси с которого был авторизован аккаунт.
Имя Фамилия Отчество владельца.
Номера виртуальных карт(Если карта присутсвует) 
Подробный мануал по использованию кошелька(Чтобы его не забанили)
Также номер телефона от кошелька отвязан.

Все кошельки были получены брутом и фишингом!  

Аккаунты добавляются каждую неделю.""", reply_markup=kali())
    elif message.text == 'Назад':
    	bot.send_message(message.chat.id, """Все кошельки проверены на валид.
QiwiWallet - в наличие 43 аккаунта

Кошелёк с балансом 500-1000 руб  -  400 руб (13 кошельков)       

Кошелёк с балансом 800-1500 руб  -  600 руб (6 кошельков)        

Кошелёк с балансом 2000-3000 Руб - 1500 руб (11 кошельков)       

Кошелёк с балансом 5000-8000 руб - 3500 руб (13 кошельков)       

При покупке кошелька вы получаете запароленный архив. 
В нём находится Логин:пароль
Серия и номер паспорта владельца. 
Прокси с которого был авторизован аккаунт.
Имя Фамилия Отчество владельца.
Номера виртуальных карт(Если карта присутствует) 
Подробный мануал по использованию кошелька(Чтобы его не забанили)
Также номер телефона от кошелька отвязан.

Все кошельки были получены брутом и фишингом!  

Аккаунты добавляются каждую неделю.""", reply_markup=kali())
    elif message.text == '1 товар (400руб)':
        bot.send_message(message.chat.id, """Вы выбрали кошелёк QiwiWallet с балансом от 500-1000руб.
Оплата происходит чисто с Qiwi.com
Отправьте 400руб на счет +7 916 907-86-58

Обязательно напишите в комментарии

'Оплата:Счёт #"""+ str(random.randint(400000,499999)) +"' (Без ковычек)", reply_markup=main1())
    elif message.text == 'Проверить поступление на счёт':
    	bot.send_message(message.chat.id, 'Платёж ещё не получен. Ожидайте 30 секунд после отправки платёжа', reply_markup=main2())
    	dead = 1
    	while dead < 4:	
    		time.sleep(3)
    		bot.send_message(message.chat.id, 'Поиск вашего платежа.')
    		time.sleep(3)
    		bot.send_message(message.chat.id, '...')
    		time.sleep(3)
    		dead = dead + 1
    	bot.send_message(message.chat.id, 'Платёж не найден!')
    	bot.send_message(message.chat.id, 'Повторите проверку снова', reply_markup=main1())
    elif message.text == '2 товар (600руб)':
        bot.send_message(message.chat.id, '''Вы выбрали кошелёк QiwiWallet с балансом от 800-1500руб.
Оплата происходит чисто с Qiwi.com
Отправьте 600руб на счет +7 916 907-86-58

Обязательно напишите в комментарии 

"Оплата:Счёт #'''+ str(random.randint(400000,499999)) +'" (Без ковычек)', reply_markup=main1())
    elif message.text == '3 товар (1500руб)':
        bot.send_message(message.chat.id, '''Вы выбрали кошелёк QiwiWallet с балансом от 2000-3000руб.
Оплата происходит чисто с Qiwi.com
Отправьте 1000руб на счет +7 916 907-86-58

Обязательно напишите в комментарии 

"Оплата:Счёт #'''+ str(random.randint(400000,499999)) +'" (Без ковычек)', reply_markup=main1())
    elif message.text == '4 товар (3500руб)':
        bot.send_message(message.chat.id, '''Вы выбрали кошелёк QiwiWallet с балансом от 5000-8000руб.
Оплата происходит чисто с Qiwi.com
Отправьте 3500руб на счет +7 916 907-86-58

Обязательно напишите в комментарии

"Оплата:Счёт #'''+ str(random.randint(400000,499999)) +'" (Без ковычек)', reply_markup=main1())
    elif message.text == 'Exit':
    	bot.send_message(message.chat.id, '''Привет я бот который продаст тебе хороший кошелёк с балансом. 
Обязательно при покупке напиши в комментарий номер товара.Номер товара получишь при оформлении заказа''', reply_markup=main())
    else:
        bot.send_message(message.chat.id, "Cложно понять", reply_markup=main())




bot.polling(none_stop=False, interval=0, timeout=20)
























