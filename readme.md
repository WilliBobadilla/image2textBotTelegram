# Imagen a texto bot telegram :robot:

Proyecto donde se realiza un bot de telegram que recibe una imagen y retorna el texto encontrado.



## Requirements:

1. telebot
2. PyTelegramBotAPI==2.2.3
3. pytesseract
4. PIL

# Instrucciones para levantar el bot :computer:

* Crear API TOKEN siguiendo este tutorial: https://www.codementor.io/@karandeepbatra/part-1-how-to-create-a-telegram-bot-in-python-in-under-10-minutes-19yfdv4wrq

* Crear un archivo token.py y guardar el token dado en una variable "API_TOKEN" (guardar como string)

<p>1. Clonar la repo</p>

```bash
git clone https://github.com/WilliBobadilla/image2textBotTelegram
```

<p>2. Moverte al directorio de la repo</p>

```bash
cd  hendylaCasasScrapper
```

<p>3. Crear el virtualenv</p>

```bash
virtualenv env
```

o si no funciona lo anterior

```bash
python -m virtualenv env
```

<p>4. Activar el virtual env</p> 
** Para linux

```bash
source env/bin/activate
```

\*\*\* En el caso de no contar con virtualenv

```bash
pip install virtualenv
```

\*\* Para windows

```bash
cd env
cd Scripts
activate.bat
cd ..
cd ..
```

Estos ultimos dos cd .. llevan de nuevo a la raiz del proyecto, en el caso de que esten usando windows hacer esto.

<p>5. Instalar dependencias</p>

```bash
pip install -r requirements.txt
```

<p>Instalar un exe del tesseract (Solo para windows): https://github.com/UB-Mannheim/tesseract/wiki</p>


<p>6. Correr el proyecto </p>

```bash
python bot.py
```

## Instrucciones de uso :blue_book:
1. Abrir telegram, y buscar el nombre de tu Bot en el buscador, el BotFather te da el link para ingresar al bot.
2. Al ingresar enviar el comando /start
3. Enviar una imagen con texto y esperar la respuesta
