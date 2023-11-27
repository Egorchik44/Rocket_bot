from bot import bot
from buttons import *
from work_db import *

def is_valid_message(user_message):

    forbidden_words_sh = ["Ярослав", "Егор"]
    if not user_message.text or user_message.text.startswith('/') or len(user_message.text) == 1:
        return True

    user_words = [word.lower() for word in user_message.text.split() if word.isalpha()]
    for word in forbidden_words_sh:
        if word.lower() in user_words:
            return True

    return False



def service_handler(message):
    user_id = message.from_user.id
    user_message = message.text

    if is_valid_message(message):
        button_service_handler = types.InlineKeyboardMarkup()
        button_service_handler.add(types.InlineKeyboardButton('Продолжить', callback_data='continue_sh'))
        button_service_handler.add(types.InlineKeyboardButton('Отказаться от услуги', callback_data='refuse_sh'))
        bot.send_message(user_id, 'Пожалуйста, введите непустое сообщение без символа "/" в начале.', reply_markup = button_service_handler)

    else:

        insert_user_message(user_id, user_message)
        bot.send_message(user_id, 'Спасибо! Ваш запрос обрабатывается.')

        # keyboard = [
        #     [types.InlineKeyboardButton("Да", callback_data='yes')],
        #     [types.InlineKeyboardButton("Нет", callback_data='no')]
        # ]
        # yes_no_sh = types.InlineKeyboardMarkup(keyboard)
        #
        # bot.send_message(user_id, f'Вы уверены в своем запросе ?', reply_markup =yes_no_sh)



# @bot.callback_query_handler(func=lambda prov: True)
# def callback_yes_no_sh_service_handler(prov):
#     user_id = prov.from_user.id
#     try:
#         if prov.data == 'yes':
#             bot.register_next_step_handler(prov.message.text, prov.from_user.id,  insert_user_message)
#             bot.send_message(user_id, 'Спасибо! Ваш запрос обрабатывается.')
#         elif prov.data == 'no':
#             bot.send_message(user_id, ' Ваш запрос отменен.')
#     except Exception as e:
#         print(repr(e))


@bot.callback_query_handler(func=lambda call: True)
def callback_button_sh_service_handler(call):
    user_id = call.from_user.id
    try:
        if call.data == 'continue_sh':
            bot.send_message(user_id, 'Вы выбрали Продолжить!')
            user_message = call.message
            bot.register_next_step_handler(user_message, service_handler)
        elif call.data == 'refuse_sh':
            bot.send_message(user_id, 'Вы выбрали Отказаться от услуги!')
    except Exception as e:
        print(repr(e))