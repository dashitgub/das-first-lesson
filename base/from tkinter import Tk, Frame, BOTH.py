import openai
import requests
import telebot

bot = telebot.TeleBot('6477725881:AAGqkGdK06o-_cqiUvfVxfnOBsWeZo1nHVA')  
openai.api_key = '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'
token = '6477725881:AAGqkGdK06o-_cqiUvfVxfnOBsWeZo1nHVA'
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, что ты хочешь узнать?')


url = f'https://api.telegram.org/bot{token}/sendSticker'
sticker_id = 'STICKER_ID'
data = {
     'chat_id': 'CHAT_ID',
     'sticker': 'CAACAgIAAxkBAAELsaNl8w6Xi6BOYJjsFI3ajtchbBQWnQAC-SsAAgMGiEidMe3YikoBtTQE'
 }
def generate_response_with_gpt(prompt):
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt}],
    temperature=0.7,
    max_tokens=1000,
  )
  return response.choices[0].message['content']

@bot.message_handler(content_types='text')
def message_reply(message):
  answer = generate_response_with_gpt(message.text)
  bot.send_message(message.chat.id, answer)

bot.polling()
