import base64
import zlib
import os
#------------------------- مكاتب show code -------------------------#
from types import CodeType
from rich.syntax import Syntax
from multiprocessing import Process
from rich.console import Console
import base64
import zlib
import re
import ast
from pathlib import Path
import argparse
#------------------------- الوان تانوية -------------------------#
a1 = '\x1b[1;31m'
a2 = '\x1b[1;34m'
a3 = '\x1b[1;32m'
a4 = '\x1b[1;33m'
a5 = '\x1b[38;5;208m'
a6 = '\x1b[38;5;5m'
#------------------------- سورس تشغيل show code -------------------------#
console = Console()
def show_code(source: str, temp):

    if not temp:
        p = Process(target=show_code, args=(source, 1))
        p.start()
        p.join(5)
        if p.is_alive():
            p.kill()
            console.print("# [red]Plya Team > - File Is Big ... ! We Cant Show Code [/red]")
    else:
        syntax = Syntax(source, "python", line_numbers=True)
        console.print(syntax)
#------------------------- مكاتب + تشغيل اداة الفك -------------------------#
import marshal
import base64
import zlib
import os
import time
import dis
import random
#-------------------------[ Style ]-------------------------#
import os, sys, time, marshal, pyfiglet, py_compile
R = '\x1b[1;31m'
G = '\x1b[1;32m'
B = '\x1b[0;94m'
Y = '\x1b[1;33m'

def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(0.03)
#------------------------- الوان رئيسية -------------------------#
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
SA = '\x1b[38;5;216m'
S2A = '\x1b[1;36m'
S3A = '\x1b[38;5;180m'
S4A= '\x1b[38;5;88m' 
S5A = "\x1b[1;32m" 
S6A= '\x1b[38;5;166m'
K = '\033[2;35m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\033[1;97m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # رمادي
a12 = '\x1b[38;5;220m'  # ذهبي
a13 = '\x1b[38;5;7m'  # فضي
a14 = '\x1b[38;5;153m'  # أزرق فاتح
a15 = '\x1b[38;5;18m'  # أزرق داكن
a16 = '\x1b[38;5;48m'  # أخضر فاتح
a17 = '\x1b[38;5;22m'  # أخضر داكن
a18 = '\x1b[38;5;196m'  # أحمر فاتح
a19 = '\x1b[38;5;88m'  # أحمر داكن
a20 = '\x1b[38;5;226m'  # أصفر فاتح
a21 = '\x1b[38;5;136m'  # أصفر داكن
a22 = '\x1b[38;5;216m'  # برتقالي فات
a23 = '\x1b[38;5;166m'  # برتقالي داكن
a24 = '\x1b[38;5;234m'  # أرجواني فاتح
a25 = '\x1b[38;5;91m'  # أرجواني داكن
a26 = '\x1b[38;5;205m'  # وردي فاتح
a27 = '\x1b[38;5;161m'  # وردي داكن
a28 = '\x1b[38;5;236m'  # أسود فاتح
a29 = '\x1b[38;5;233m'  # أسود داكن
a30 = '\x1b[38;5;255m'  # أبيض فاتح
a31 = '\x1b[38;5;231m'  # أبيض داكن
a32 = '\x1b[38;5;180m'  # بني فاتح
a33 = '\x1b[38;5;94m'  # بني داكن
a34 = '\x1b[38;5;252m'  # رمادي فاتح
a35 = '\x1b[38;5;246m'  # رمادي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[38;5;117m'  # أزرق سماوي

os.system("clear")
from cfonts import render, say
import pyfiglet
output = render(' Plya ', colors=['white', 'green'], align='center')
print(output)   
print("\x1b[1;94m–"*50)
print('\x1b[1;94m> - Welcome To \x1b[1;97mPlya Team - DecodeX ++ ')
print("\x1b[1;94m> - Devlopers \x1b[1;97m~\x1b[1;97m Plya - Team [Arab Developer's] ~")  
print("\x1b[1;94m> - Version\x1b[1;97m : V5 Beta")
print("\x1b[1;94m> - Telegram\x1b[1;97m : @Plya_Team")
print("\x1b[1;94m–"*50)
print('\n')
import sys

s = sys.argv
text = ""
for x in range(1, len(s)):
    text = text + s[x] + " "

try:
    with open(text.strip(), "r") as file:
        besto2 = file.read()
        with open("Plya_Team.py", "w") as output_file:
            output_file.write(besto2)
except FileNotFoundError:
    print("File not found. Please check the file path.")
with open("Plya_Team.py", "r") as file:

    search_enc = file.read()
#-------------------------[Dec Cython]-------------------------#
if """import marshal\nexec(marshal.loads(b'""" in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_01/decode_mar.py')
#-------------------------[ فك جميع انواع لامبدا ]-------------------------#
elif '''exec((lambda __, _, : _''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda V1 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda V1 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/lambda.py')  
    
elif '''exec((lambda __, _:''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda V1 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mObfuscate Simple Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/lambda.py')  
                  
elif '''exec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___)''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda V2 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda V2 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/lambda.py')  
#-------------------------[ فك ترميزات السهلة ]-------------------------#
elif '''exec(__import__(''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mObf Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mObf Base64 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')
    
elif '''exec(zlib.decompress(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mZlib \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mZlib Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')
  
elif '''exec(lzma.decompress(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLzma \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLzma Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(gzip.decompress(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mGzip \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mGzip Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(base64.b64decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase64 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(base64.b32decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase32 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(base64.b16decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase16 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(zlib.decompress(base64.b64decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase64 - Zlib \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase64 - Zlib Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(lzma.decompress(base64.b64decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase64 - Lzma \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase64 - Lzma Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(gzip.decompress(base64.b64decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase64 - Gzip \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase64 - Gzip Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(zlib.decompress(base64.b32decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase32 - Zlib \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase32 - Zlib Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(lzma.decompress(base64.b32decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase32 - Lzma \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase32 - Lzma Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(Gzip.decompress(base64.b32decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase32 - Gzip \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase32 - Gzip Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(zlib.decompress(base64.b16decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase16 - Zlib \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase16 - Zlib Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(lzma.decompress(base64.b16decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase16 - Lzma \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase16 - Lzma Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(Gzip.decompress(base64.b16decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mBase16 - Gzip \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mBase16 - Gzip Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(Gzip.decompress(zlib.decompress(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mGzip - Zlib \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mGzip - Zlib Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(zlib.decompress(gzip.decompress(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mZlib - Gzip \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mZlib - Gzip Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(lzma.decompress(zlib.decompress(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLzma - Zlib \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLzma - Zlib Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')  

elif '''exec(zlib.decompress(lzma.decompress(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mZlib - Lzma \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mZlib - lzma Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/enc_simple.py')
    
elif '''exec(marshal.loads(zlib.decompress(base64.b64decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Zlib Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Zlib Base64 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')  
                      
elif '''exec(marshal.loads(zlib.decompress(base64.b32decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Zlib Base32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Zlib Base32 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    

elif '''exec(marshal.loads(zlib.decompress(base64.b16decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Zlib Base16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Zlib Base16 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    
    
elif '''exec(marshal.loads(zlib.decompress(base64.b85decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Zlib Base85 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Zlib Base85 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    
    
elif '''exec(marshal.loads(gzip.decompress(base64.b85decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Gzip Base85 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Gzip Base85 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    
    
elif '''exec(marshal.loads(lzma.decompress(base64.b85decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Lzma Base85 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Lzma Base85 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    
    
elif '''exec(marshal.loads(gzip.decompress(base64.b64decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Gzip Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Gzip Base64 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/tools/mar.py')
    
elif '''exec(marshal.loads(gzip.decompress(base64.b32decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Gzip Base32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Gzip Base32 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    
    
elif '''exec(marshal.loads(gzip.decompress(base64.b16decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Gzip Base16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Gzip Base16 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    
    
elif '''exec(marshal.loads(lzma.decompress(base64.b64decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Lzma Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Lzma Base64 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/tools/mar.py')
    
elif '''exec(marshal.loads(lzma.decompress(base64.b32decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Lzma Base32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Lzma Base32 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    
    
elif '''exec(marshal.loads(lzma.decompress(base64.b16decode(b''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mMarshal Lzma Base16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mMarshal Lzma Base16 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    

elif '''exec(codecs.decode(''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mCodecs \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mCodecs Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    

elif '''exec(bytes.fromhex(''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mHex \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mHex Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_cod.py')                    
#-------------------------[ Dec Obfuscate ]-------------------------#
elif '''_ = lambda __ : __import__('zlib').decompress(__[::-1])''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Zlib \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Zlib Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/m.py')       
    
elif '''_ = lambda __ : __import__('marshal').loads(__[::-1])''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_mar.py')                    

elif '''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Zlib \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Zlib Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_zlib.py')                    

elif '''_ = lambda __ : __import__('marshal').loads(__import__('base64').b64decode(__[::-1]))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Base64 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_base.py')                    

elif '''_ = lambda __ : __import__('marshal').loads(__import__('base64').b32decode(__[::-1]))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Base32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Base32 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_base32.py')                    

elif '''_ = lambda __ : __import__('marshal').loads(__import__('base64').b16decode(__[::-1]))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Base16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Base16 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_bot/besto_base16.py')                    

elif '''_ = lambda __ : __import__('base64').b64decode(__[::-1])''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Base64 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/b.py')    

elif '''_ = lambda __ : __import__('base64').b32decode(__[::-1])''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Base32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Base32 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/basee.py')

elif '''_ = lambda __ : __import__('base64').b16decode(__[::-1])''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Base16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Base16 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/base.py')

elif '''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Zlib Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Zlib Base64 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/basezlibb.py')                       

elif '''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Zlib Base32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Zlib Base32 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/basezlibbb.py')                    

elif '''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Zlib Base16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Zlib Base16 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/basezlib.py')                       
    
elif '''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Zlib Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Zlib Base64 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_01/baseee.py')

elif '''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])));''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Zlib Base32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Zlib Base32 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_01/basee.py')

elif '''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Zlib Base16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Zlib Base16 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_01/base.py')

elif '''_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])))))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Lzma Gzip Zlib Base64 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Lzma Gzip Zlib Base64 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_01/mar_lzma_gzip_zlib.py')

elif '''_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b32decode(__[::-1])))))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Lzma Gzip Zlib Base32 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Lzma Gzip Zlib Base32 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_01/mar_lzma_gzip_zlib_32.py')
    
elif '''_ = lambda __ : __import__('marshal').loads(__import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b16decode(__[::-1])))))''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mLambda - Marshal Lzma Gzip Zlib Base16 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mLambda - Marshal Lzma Gzip Zlib Base16 Rυииιg ...\n")
    os.system(f'python3.9 /sdcard/decode/Plya_Team/plya_01/mar_lzma_gzip_zlib_16.py')
    
elif '''Offuscats(''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97mObf Offuscats \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97mObf Offuscats ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/obf.py')  
#-------------------------[ Dec 🔒 ]-------------------------#
elif '''def custom_decrypt(encrypted_text)''' in search_enc:
    slow("\n\x1b[1;94m> - Pℓуα Tєαм \x1b[1;97mDєᴄσᴅєX ++ Rυииιиg ...\n\x1b[1;94m> - Wєℓᴄσмє \x1b[1;97mBσѕѕ\n\x1b[1;94m> - Tнє Fιℓє Iѕ Eиᴄσᴅιиg \x1b[1;97m🔒 \n\x1b[1;94m> - Tσσℓ Dєᴄσᴅє \x1b[1;97m🔒 Rυииιg ...\n")
    os.system(f'python /sdcard/decode/Plya_Team/plya_bot/kfl.py')                    
#-------------------------[ Dec Marshal ]-------------------------#  
else:
    exit(' This Enc Cant Dec It ')