from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


def generate_phone_number():
   return ReplyKeyboardMarkup([
      [KeyboardButton(text='Отправить свой контакт 📞', request_contact=True)]
   ], resize_keyboard=True)


def generate_location():
   return ReplyKeyboardMarkup([
      [KeyboardButton(text='🚚 Отправить своё местоположение 🚚', request_location=True)],
      [KeyboardButton(text='🏫 Выбрать филиал 🏫')]
   ], resize_keyboard=True)


def generate_main_menu():
   return ReplyKeyboardMarkup([
      [KeyboardButton(text='✅ Сделать заказ')],
      [KeyboardButton(text='📒 История заказа'), KeyboardButton(text='🛒 Корзина'), KeyboardButton(text='⚙ Настройки')]
   ])


def generate_geolocation():
   return ReplyKeyboardMarkup([
      [KeyboardButton(text='Отправить свою геопозицию', request_location=True)]
   ], resize_keyboard=True)


def commit_button_address():
   markup = InlineKeyboardMarkup()
   markup.row(
      InlineKeyboardButton(text='Да', callback_data='yes'))
   markup.row(InlineKeyboardButton(text='Нет', callback_data='no'))
   return markup


def generate_categories_menu(categories):
   markup = InlineKeyboardMarkup(row_width=2)
   buttons = []
   markup.row(
      InlineKeyboardButton(text='Всё меню', url='https://telegra.ph/Vsyo-menyu-PROWEB-EDA-06-25-3')
   )
   for category in categories:
      # [(1, Лаваши), (2, Бургеры)]
      btn = InlineKeyboardButton(text=category[1], callback_data=f'category_{category[0]}') # category_1
      buttons.append(btn)
   markup.add(*buttons)
   return markup


def generate_products_menu(products):
   markup = InlineKeyboardMarkup(row_width=2)
   buttons = []
   for product_id, product_name in products:
      btn = InlineKeyboardButton(text=product_name, callback_data=f'product_{product_id}')
      buttons.append(btn)
   markup.add(*buttons)
   markup.row(
      InlineKeyboardButton(text='Назад', callback_data='main_menu')
   )
   return markup


def generate_product_buttons(product_id, category_id, quantity=1):
   markup = InlineKeyboardMarkup()
   prev_btn = InlineKeyboardButton(text='➖', callback_data=f'change_{product_id}_{quantity-1}')
   next_btn = InlineKeyboardButton(text='➕', callback_data=f'change_{product_id}_{quantity+1}')
   quan_btn = InlineKeyboardButton(text=str(quantity), callback_data='quantity')
   add_to_cart = InlineKeyboardButton(text='Хочу 😍😋', callback_data=f'cart_{product_id}_{quantity}')
   back = InlineKeyboardButton(text='Назад', callback_data=f'back_{category_id}')
   markup.row(prev_btn, quan_btn, next_btn)
   markup.row(add_to_cart)
   markup.row(back)
   return markup


def generate_cart_product(cart_id, cart_products):
   markup = InlineKeyboardMarkup()
   markup.row(
      InlineKeyboardButton(text='🚀 Оформить заказ', callback_data=f'order_{cart_id}')
   )
   for product in cart_products:
      markup.row(
         InlineKeyboardButton(text=f'❌ {product[1]}', callback_data=f'delete_{product[0]}')
      )
      prev_btn = InlineKeyboardButton(text='➖', callback_data=f'edit_{product[0]}_{product[2] - 1}')
      next_btn = InlineKeyboardButton(text='➕', callback_data=f'edit_{product[0]}_{product[2] + 1}')
      quan_btn = InlineKeyboardButton(text=str(product[2]), callback_data='quantity')
      markup.row(prev_btn, quan_btn, next_btn)
   return markup


def status(cart_id):
   markup = InlineKeyboardMarkup()
   markup.row(
      InlineKeyboardButton(text='Доставлен✅', callback_data=f'ready_{cart_id}')
   )
   markup.row(
      InlineKeyboardButton(text='Отменен', callback_data='cancel')
   )
   return markup
