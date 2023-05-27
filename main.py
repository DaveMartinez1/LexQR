import webbrowser
import qrcode
import argparse
import platform
import os
import sys

############----------############
#          By: LexaHck           #
#    https://github.com/LexaHck  #
#                                #
#     From the dark side...      #
#             -2023-             #
############----------############

# Variables globales
parser = argparse.ArgumentParser(usage="python3 -i <url> -o <file-name>")

# Funcion Open_WB
def open_wb(file):
    print("[+] Conversion exitosa!")
    webbrowser.open(file)
    sys.exit()

# Argumentos
parser.add_argument('-i', '--input', help="URL que desea pasar a codigo QR")
parser.add_argument('-o', '--output', help="Nombre con el que desea que se guarde el archivo")

args = parser.parse_args()

if not (args.input or args.output):
    parser.print_help()

img = qrcode.make(args.input)
img.save(f"{args.output}.png")

# Mostrar QR en el navegador
open_wb(f"{args.output}.png")