from bot import bot
from buttons import *
from work_db import *

def ask_car_info(message):
    user_id = message.from_user.id
    car_num = message.text
    bot.send_message(user_id, 'Введите название машины:')
    bot.register_next_step_handler(message, ask_car_name, car_num)



def ask_car_info(message):
    user_id = message.from_user.id
    car_num = message.text

    if car_num.lower() == 'cancel':
        bot.send_message(user_id, 'Операция отменена.')
        return

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Cancel'))
    bot.send_message(user_id, 'Введите название машины:', reply_markup=markup)
    bot.register_next_step_handler(message, ask_car_name, car_num)


def ask_car_name(message, car_num):
    user_id = message.from_user.id
    car_name = message.text

    if car_name.lower() == 'cancel':
        bot.send_message(user_id, 'Операция отменена.')
        return

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Cancel'))
    bot.send_message(user_id, 'Введите описание работ:', reply_markup=markup)
    bot.register_next_step_handler(message, finish_car_info, car_num, car_name)


def finish_car_info(message, car_num, car_name):
    user_id = message.from_user.id
    work_description = message.text

    if work_description.lower() == 'cancel':
        bot.send_message(user_id, 'Операция отменена.')
        return

    insert_car_info(car_num, car_name, work_description)
    bot.send_message(user_id, 'Информация о машине добавлена. Спасибо!')
