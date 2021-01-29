import telebot as tb
import requests
import shutil

API_TOKEN = "1507843069:AAEOcU9ulclTOjSZmzhGEk4znlTguiqT9Ns"
bot = tb.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hola, bienvenido!")

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(content_types=['photo'])
def handle_all_media(message):
    #print(message)
    file_id = message.json["photo"][0]["file_id"]
    bot.reply_to(message, "Recibido" + str(file_id))
    file_info = bot.get_file(file_id) 
    print(file_info.file_path) 
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))
    print(file)
    if file.status_code == 200:
        with open("ggg.jpg", "wb") as f:
            f.write(file.content)

bot.polling()