import telebot
import base
import app_api

bot = telebot.TeleBot(base.TOKEN)

print('bot created...')

@bot.message_handler(commands=['start'])
def say_hello(message):
    #print(message)
    bot.send_message(message.chat.id, text='welcome')
    
@bot.message_handler(commands=['help', 'support'])
def support(message):
    bot.reply_to(message, text='tamas 123')
    
@bot.message_handler(commands=['news'])
def shoe_news(message):
    markup = telebot.types.InlineKeyboardMarkup(row_width=2)
    
    btn1 = telebot.types.InlineKeyboardButton(text = 'اخبار ورزشی' ,url ='https://varzesh3.com')
    btn2 = telebot.types.InlineKeyboardButton(text = 'اخبارعمومی' ,url ='https://entekhab.ir')
    btn3 = telebot.types.InlineKeyboardButton(text = 'اخبار اقتصادی' ,url ='https://tradingview.com')

    markup.add(btn1, btn2, btn3)
    
    bot.send_message(message.chat.id, text='یکی از گزینه های زیر را انتخاب کنید',
                     reply_markup=markup)
    
@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup()
    
    btn1 = telebot.types.KeyboardButton(text = 'تماس با ما')
    btn2 = telebot.types.KeyboardButton(text = 'درباره ما')
    btn3 = telebot.types.KeyboardButton(text = 'عضویت')
    btn4 = telebot.types.KeyboardButton(text = 'بازگشت')
    
    markup.add(btn1, btn2, btn3, btn4)
        
    bot.send_message(message.chat.id, text='یکی از گزینه های زیر را انتخاب کنید',
                         reply_markup=markup)
    
    
    
@bot.message_handler(commands=['movie'])
def show_movie_message(message):
    msg = bot.send_message(message.chat.id, text='آیدی فیلم مورد نظر را وارد کنید')
    bot.register_next_step_handler(msg, show_movie_info)

def show_movie_info(message):
    movie_id = message.text
    result = app_api.get_movie_info_by_id(movie_id)
    bot.send_message(message.chat.id, text=f'{result[0] }/ {result[-1]}')
    

@bot.message_handler(commands=['movie_1'])
def show_movie_message(message):
    msg = bot.send_message(message.chat.id, text='اسم فیلم مورد نظر را وارد کنید')
    bot.register_next_step_handler(msg, show_movie_info)

def show_movie_info(message):
    movie_name = message.text
    result = app_api.get_movie_info_by_name(movie_name)
    bot.send_message(message.chat.id, text=f'{result[1] }/ {result[-1]}')
    
 

@bot.message_handler(func=lambda message:True)
def handle_other_message(message):

    if message.text == 'تماس با ما':
        email = 'support@gmail.com'
        mobile = '09123625145'
        post_box = '1425362433'
        info = f'email:{email} / mobile:{mobile} / post_box:{post_box}'
        bot.send_message(message.chat.id, text=info)

    elif message.text =='درباره ما' :
        bot.send_message(message.chat.id, text=' ما یک گروه آموزشی هستیم')



    elif message.text =='بازگشت' :
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text=' باز گشت به منوی اصلی', reply_markup=markup)

    else:
        bot.send_message(message.chat.id, text=' پیام شما را متوجه نشدم')
    
if __name__ == '__main__':
    bot.infinity_polling()
