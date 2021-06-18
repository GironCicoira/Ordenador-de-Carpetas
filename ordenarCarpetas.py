import os
import shutil

ruta_descargas = 'C:\\Users\\giron\\Downloads\\'
ext_texto = ['.docx', '.txt', '.doc', '.pdf', '.pptx']
ext_foto = ['.png', '.jpg', '.jpeg', '.gif']
ext_sfk = ['.sfk']

def Ordenar(archivo, ext):
    for i in ext_texto:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Text')
    for i in ext_foto:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Fotos')
    if ext != '':
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Otros')

def main():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        Ordenar(archivo, ext)
main()