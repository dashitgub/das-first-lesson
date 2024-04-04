import telebot
import wikipedia
# Токен вашего бота
TOKEN = '6066518469:AAHrI0vr0IxZ6Phj5vHopOcByysRk0YWcjo'

# Создаем объект бота
bot = telebot.TeleBot(TOKEN)

wikipedia.set_lang('ru')

def get_info(word):
    try:
        wikitext = wikipedia.page(word).content[:500]
        return wikitext
    except Exception as e:
        return 'В энциклопедии нет информации об этом'
    

# Обработчик команды "/start"
@bot.message_handler(commands=['start', 'hi', 'hello'])
def start_message(message):
    # Отправляем приветственное сообщение
    message2 = bot.send_message(message.chat_id, 'Привет! Я бот-помощник для работы с WikiPedia. Отправь мне ключевое слово и я найду тебе информацию',  bot.send_sticker(message.chat.id, sticker_id))
    bot.register_next_step_handler(message2, handle_text)
def handle_text(message):
    word = message.text 
    info = get_info(word)
    bot.send_message(message.chat_id, info)
    
    # Отправляем стикер
    sticker_id = 'CAACAgIAAxkBAAEL2AVmDqVysANWskI_iKcBlflrpCE88gACUhMAAjFuOUgEv3MHYx5zkzQE'  # ID вашего стикера
    # bot.send_sticker(message.chat.id, sticker_id)



# Запускаем бота
bot.polling()