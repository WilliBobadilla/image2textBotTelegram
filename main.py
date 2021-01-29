# https://stackoverflow.com/questions/33401767/importerror-no-module-named-pytesseract/33402041
# https://github.com/eternnoir/pyTelegramBotAPI
try:
    import Image
except ImportError:
    from PIL import Image
import datetime
from pytesseract import *
import os


def entrada(lista_files):
    name = input("Introduce el nombre con la extension de la imagen: ")
    if not name in lista_files:
        entrada(lista_files)
    text = pytesseract.image_to_string(Image.open(name))
    print(text)
    # tomamos solo el nombre sin la extension
    name_of_file = name.split(".")[0]+".txt"
    with open(name_of_file, 'w') as arch:
        arch.writelines("Traducido de imagen a texto en fecha: " +
                        str(datetime.datetime.now()) + "\n")
        arch.writelines(text)
    print("Fin")


if __name__ == '__main__':
    print("--------------Archivos disponibles para convertir------------")
    lista_files = os.listdir(os.getcwd())
    print(lista_files)
    entrada(lista_files)
    print(lista_files)
