import base64
import marshal
import zlib
import gzip
import time
import codecs
import os
import sys
import time
import random

def mahos():
    anim = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□","[\x1b[1;92m■■\x1b[0m□□□□□□□□", "[\x1b[1;93m■■■\x1b[0m□□□□□□□", "[\x1b[1;95m■■■■\x1b[0m□□□□□□", "[\x1b[1;94m■■■■■\x1b[0m□□□□□", "[\x1b[38;5;26m■■■■■■\x1b[0m□□□□", "[\x1b[1;96m■■■■■■■\x1b[0m□□□", "[\x1b[38;5;86m■■■■■■■■\x1b[0m□□", "[\x1b[38;5;96m■■■■■■■■■\x1b[0m□", "[\x1b[38;5;203m■■■■■■■■■■\x1b[0m]"]
    am = ('\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m')
    for i in range(50):
        time.sleep(.1)
        os.system('clear')
        sys.stdout.write(f"\r \x1b[38;5;203mجـاري التـشفير... \033[1;92m" + anim[i % len(anim)] +"\x1b[0m ")
        sys.stdout.write(f"\r \x1b[38;5;203mجـاري التـشفير... \033[1;92m" + am[i % len(am)] +"\x1b[0m ")
        sys.stdout.flush()


#------------------------------[الالوان]------------------------------
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\x1b[38;5;208m' #برتقالي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
U = '\x1b[1;37m'#ابیض

#------------------------------[الالوان]------------------------------
print(f'''{B}{E}=============================={B}
|{F}[+] YouTube    : {B}|أحمد الحراني 
|{F}[+] TeleGram  : {B} maho_s9    |
|{F}[+] Instagram  : {B}ahmedalharrani |
|{F}[+] Tool  : {B}Encode Tool |
|{F}[+] Service  : {B}All In One|
{E}==============================''')
def encode_file(file_name, encoding_functions):
    with open(file_name, "r", encoding="utf-8") as file:
        code = file.read()

    for encode_function in encoding_functions:
        code = encode_function(code)
        time.sleep(2) 

    with open("enc-" + file_name.split('.')[0] + ".py", "w", encoding="utf-8") as enc_file:
        enc_file.write("#https://t.me/maho9s\n# -*- coding: utf-8 -*-\n")
        enc_file.write(code)

def base64_encode(code):
    encoded_base64 = base64.b64encode(code.encode()).decode()
    return "import base64\nexec(base64.b64decode('" + encoded_base64 + "'))"

def base32_encode(code):
    encoded_32 = base64.b32encode(code.encode()).decode()
    return "import base64\nexec(base64.b32decode('" + encoded_32 + "'))"

def lambda_encode(code):
    compressed_data = zlib.compress(code.encode('utf-8'))
    return "import zlib\nexec(zlib.decompress(" + repr(compressed_data) + ").decode())"

def zlib_encode(code):
    compressed_zlib = zlib.compress(code.encode('utf-8'))
    encoded_zlib = base64.b64encode(compressed_zlib).decode()
    return "import zlib\nimport base64\nexec(zlib.decompress(base64.b64decode('" + encoded_zlib + "')).decode())"

def gzip_encode(code):
    compressed_gzip = gzip.compress(code.encode())
    encoded_gzip = base64.b64encode(compressed_gzip).decode()
    return "import gzip\nimport base64\nexec(gzip.decompress(base64.b64decode('" + encoded_gzip + "')).decode())"

def marshal_encode(code):
    compiled_code = compile(code, '<string>', 'exec')
    encrypted_code = base64.b64encode(marshal.dumps(compiled_code, 10))
    return "import marshal\nimport base64\nexec(marshal.loads(base64.b64decode('" + encrypted_code.decode() + "')))"

def hex_encode(code):
    encoded_hex = code.encode().hex()
    return "exec(bytes.fromhex('" + encoded_hex + "'))"



def marshal_zlib_encode(code):
    compiled_code = compile(code, "<string>", 'exec')
    marshaled_code = marshal.dumps(compiled_code)
    compressed_code = zlib.compress(marshaled_code)
    encoded_code = "import zlib\nimport base64\nimport marshal\nexec(marshal.loads(zlib.decompress(" + repr(compressed_code) + ")))"
    return encoded_code

def encoded_rot13(code):
    encoded_rot13 = codecs.encode(code, 'rot_13')
    return "import codecs\nexec(codecs.decode(" + repr(encoded_rot13) + ", 'rot_13'))\n"
    
file_name = input(f'{B} Enter Your File Name: {S} ')
mahos()
encode_file(file_name, [base64_encode, base32_encode, lambda_encode, zlib_encode, gzip_encode, marshal_encode, marshal_zlib_encode, hex_encode ,encoded_rot13])
print(f'{F}تم تشفير الملف بنجاح باسم enc-{file_name}!')