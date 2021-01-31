import telebot as tb
import requests
import shutil
import main

API_TOKEN = "1507843069:AAEOcU9ulclTOjSZmzhGEk4znlTguiqT9Ns"
bot = tb.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, "Hola! soy un bot que se encarga de convertir toda imagen en texto, si es posible :)")

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(content_types=['photo'])
def handle_all_media(message):
    print("Recibiendo")
    file_id = message.json["photo"][0]["file_id"]
    file_info = bot.get_file(file_id) 
    print(file_info.file_path) 
    file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(API_TOKEN, file_info.file_path))
    print(file)
    main.mkdir()
    if file.status_code == 200:
        with open("images/imagen.jpg", "wb") as f:
            f.write(file.content)

    bot.reply_to(message, "Texto: \n" + main.convertidor('images/imagen.jpg'))

bot.polling()