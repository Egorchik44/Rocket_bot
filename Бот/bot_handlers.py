from bot import bot
from buttons import *
from work_db import *
from service import service_handler
from car import ask_car_info

@bot.message_handler(commands=['start'])
def start(message):
    create_tables()
    user_id = message.from_user.id
    user_name = message.from_user.username
    if not user_exists(user_id):
        insert_user(user_id, user_name)

    bot.send_message(message.chat.id,
                     f'Привет, {message.from_user.first_name}! Добро пожаловать в Ракета моторспорт!'
                     f' Я здесь, чтобы помочь вам воплотить в жизнь ваши автомобильные фантазии. Чтобы оставить заявку выполните команду /service',
                     reply_markup=button_start)


@bot.message_handler(commands=['service'])
def service(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Опишите ваши желания.')
    bot.register_next_step_handler(message, service_handler)


@bot.message_handler(commands=['add'])
def add_car(message):
    user_id = message.from_user.id
    bot.send_message(user_id, 'Введите номер машины:', reply_markup=button_add_car)
    bot.register_next_step_handler(message, ask_car_info)
