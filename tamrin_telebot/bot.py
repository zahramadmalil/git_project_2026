import telebot
import base
import app_api
from datetime import datetime


bot = telebot.TeleBot(base.TOKEN)

print('bot created...')



def save_search_log(user_id, username, search_text):
    try:
        with open('search_log.txt', 'a', encoding='utf-8') as f:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            f.write(f'[{now}] user:{user_id} | @{username} | search: {search_text}\n')
    except Exception as e:
        print(f'log error: {e}')



@bot.message_handler(commands=['start'])
def say_hello(message):
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)

    btn1 = telebot.types.KeyboardButton(text='🔍 جستجوی فیلم')
    btn2 = telebot.types.KeyboardButton(text='⭐ فیلم‌های محبوب')
    btn3 = telebot.types.KeyboardButton(text='❓ راهنما')

    markup.add(btn1, btn2)
    markup.add(btn3)

    welcome_text = (
        f'سلام {message.from_user.first_name} عزیز 👋\n'
        f'🎬 به ربات جستجوی فیلم خوش آمدید!\n\n'
        f'یکی از گزینه های زیر را انتخاب کنید'
    )

    bot.send_message(message.chat.id, text=welcome_text, reply_markup=markup)



@bot.message_handler(commands=['about'])
def show_about(message):
    about_text = (
        '🎬 ربات جستجوی فیلم\n\n'
        '📌 نسخه 1.0\n'
        '👨‍💻 توسعه دهنده: دانشجوی پایتون\n'
        '📅 تاریخ: ۱۴۰۵/۰۶/۲۴\n\n'
        '🔗 منبع داده: moviesapi.ir\n'
        '🎯 هدف: تمرین API و کتابخانه Telebot'
    )
    bot.send_message(message.chat.id, text=about_text)



@bot.message_handler(commands=['help'])
def show_help_command(message):
    help_text = (
        '📚 راهنمای ربات:\n\n'
        '/start - شروع و نمایش منوی اصلی\n'
        '/about - درباره ربات\n'
        '/help - این راهنما\n\n'
        '🗂 گزینه های منو:\n'
        '🔍 جستجوی فیلم - جستجو با نام\n'
        '⭐ فیلم‌های محبوب - لیست فیلم‌ها\n'
        '❓ راهنما - نمایش راهنما'
    )
    bot.send_message(message.chat.id, text=help_text)



@bot.message_handler(func=lambda message: True)
def handle_menu_options(message):
    user_text = message.text
    user_id = message.from_user.id
    username = message.from_user.username or 'unknown'

    
    if user_text == '🔍 جستجوی فیلم':
        msg = bot.send_message(message.chat.id, text='🎬 اسم فیلم مورد نظر را وارد کنید')
        bot.register_next_step_handler(msg, search_movie_by_name)

    
    elif user_text == '⭐ فیلم‌های محبوب':
        show_popular_movies(message)

    
    elif user_text == '❓ راهنما':
        show_help_command(message)

    
    else:
        bot.send_message(message.chat.id, text=' پیام شما را متوجه نشدم. لطفا از منو استفاده کنید')



def search_movie_by_name(message):
    movie_name = message.text.strip()
    user_id = message.from_user.id
    username = message.from_user.username or 'unknown'

    
    save_search_log(user_id, username, movie_name)

    
    result = app_api.get_movie_info_by_name(movie_name)

    
    if result == 'ERROR':
        bot.send_message(message.chat.id, text='❌ خطا در ارتباط با سرور. لطفا دوباره تلاش کنید')

    elif result == 'EMPTY':
        bot.send_message(message.chat.id, text=f'😔 فیلمی با نام "{movie_name}" یافت نشد')

    else:
        
        markup = telebot.types.InlineKeyboardMarkup(row_width=1)

        for movie in result[:10]:  
            btn_text = f'{movie["title"]} ({movie.get("year", "?")})'
            callback_data = f'movie_{movie["id"]}'
            btn = telebot.types.InlineKeyboardButton(
                text=btn_text,
                callback_data=callback_data
            )
            markup.add(btn)

        bot.send_message(
            message.chat.id,
            text=f'🔍 نتایج جستجو برای "{movie_name}":\n\nبرای دیدن اطلاعات کامل روی نام فیلم کلیک کنید:',
            reply_markup=markup
        )



def show_popular_movies(message):
    result = app_api.get_popular_movies(page=1)

    if result == 'ERROR':
        bot.send_message(message.chat.id, text='❌ خطا در ارتباط با سرور')

    elif result == 'EMPTY':
        bot.send_message(message.chat.id, text='😔 فیلمی یافت نشد')

    else:
        
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)

        for movie in result[:8]:   
            btn_text = f'🎬 {movie["title"]}'
            callback_data = f'movie_{movie["id"]}'
            btn = telebot.types.InlineKeyboardButton(
                text=btn_text,
                callback_data=callback_data
            )
            markup.add(btn)

        
        btn_more = telebot.types.InlineKeyboardButton(
            text='📄 مشاهده صفحه بعد »',
            callback_data='more_movies_2'
        )
        markup.add(btn_more)

        bot.send_message(
            message.chat.id,
            text='⭐ لیست فیلم‌های محبوب:\n\nبرای مشاهده اطلاعات کامل کلیک کنید:',
            reply_markup=markup
        )



@bot.callback_query_handler(func=lambda call: True)
def handle_inline_buttons(call):
    callback_data = call.data
    chat_id = call.message.chat.id

    
    if callback_data.startswith('movie_'):
        movie_id = callback_data.replace('movie_', '')

        try:
            movie_id = int(movie_id)
            result = app_api.get_movie_info_by_id(movie_id)

            if result == 'ERROR':
                bot.send_message(chat_id, text='❌ خطا در دریافت اطلاعات فیلم')
            else:
                title, country, director, year, imdb_rate, plot, actors, genres, poster = result

                genres_text = ', '.join(genres) if genres else 'نامشخص'

                info_text = (
                    f'🎬 {title}\n\n'
                    f'📅 سال ساخت: {year}\n'
                    f'🌍 کشور: {country}\n'
                    f'🎥 کارگردان: {director}\n'
                    f'⭐ امتیاز IMDB: {imdb_rate}\n'
                    f'🎭 ژانر: {genres_text}\n'
                    f'👥 بازیگران: {actors}\n\n'
                    f'📝 خلاصه:\n{plot}'
                )

                bot.send_message(chat_id, text=info_text)

        except Exception as e:
            bot.send_message(chat_id, text=f'❌ خطا: {str(e)}')

    
    elif callback_data.startswith('more_movies_'):
        page = int(callback_data.replace('more_movies_', ''))
        result = app_api.get_popular_movies(page=page)

        if result == 'ERROR':
            bot.send_message(chat_id, text='❌ خطا در ارتباط با سرور')
        elif result == 'EMPTY':
            bot.send_message(chat_id, text='😔 فیلم بیشتری یافت نشد')
        else:
            markup = telebot.types.InlineKeyboardMarkup(row_width=2)

            for movie in result:
                btn_text = f'🎬 {movie["title"]}'
                callback_data_new = f'movie_{movie["id"]}'
                btn = telebot.types.InlineKeyboardButton(
                    text=btn_text,
                    callback_data=callback_data_new
                )
                markup.add(btn)

            
            nav_btns = []
            if page > 1:
                nav_btns.append(
                    telebot.types.InlineKeyboardButton(
                        text='« صفحه قبل',
                        callback_data=f'more_movies_{page - 1}'
                    )
                )
            nav_btns.append(
                telebot.types.InlineKeyboardButton(
                    text='صفحه بعد »',
                    callback_data=f'more_movies_{page + 1}'
                )
            )
            markup.add(*nav_btns)

            bot.send_message(
                chat_id,
                text=f'📄 صفحه {page} از لیست فیلم‌ها:',
                reply_markup=markup
            )

    
    bot.answer_callback_query(call.id)



if __name__ == '__main__':
    try:
        print('ربات در حال اجرا...') 
        bot.infinity_polling()
    except Exception as e:
        print(f'خطا در اجرای ربات: {e}')
