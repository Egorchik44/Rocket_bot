from telebot import types

button_start = types.InlineKeyboardMarkup()
button_start.add(types.InlineKeyboardButton('Наш сайт', url='https://raketamotorsport.ru'))
button_start.add(types.InlineKeyboardButton('Наш адрес',
                                          url='https://yandex.ru/maps/org/raketa_motorsport/227749354015/?ll=37.246841%2C55.598747&z=15'))


button_add_car = types.ReplyKeyboardMarkup(one_time_keyboard=True)
button_add_car.add(types.KeyboardButton('Cancel'))




