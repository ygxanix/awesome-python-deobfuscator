from os import system as mina
import time
import sys
import time
import os
import pyfiglet
import os,sys
import requests
from datetime import datetime
import pytz
import sys
import os
G1 = '\x1b[1;97m'
G2 = '\x1b[38;5;196m'
G3 = '\x1b[1;33m'
G4 = '\x1b[1;96m'
G5 = '\x1b[38;5;8m'
G6 = '\x1b[38;5;48m'
G7 = '\x1b[38;5;47m'
G8 = '\x1b[38;5;49m'
G9 = '\x1b[38;5;50m'
G10 = '\x1b[1;34m'
G11 = '\x1b[38;5;14m'
G12 = '\x1b[38;5;123m'
G13 = '\x1b[38;5;122m'
G14 = '\x1b[38;5;86m'
G14 = '\x1b[38;5;121m'
G15 = '\x1b[38;5;205m'
G16 = '\x1b[1;92m\x1b[38;5;208m'
G17 = '\x1b[1;92m\x1b[38;5;209m'
G18 = '\x1b[1;92m\x1b[38;5;210m'
G19 = '\x1b[1;92m\x1b[38;5;211m'
G20 = '\x1b[1;92m\x1b[38;5;212m'
G21 = '\x1b[1;92m\x1b[38;5;46m'
G23 = '\x1b[1;92m\x1b[38;5;47m'
G24 = '\x1b[1;92m\x1b[38;5;48m'
G25 = '\x1b[1;92m\x1b[38;5;49m'
G26 = '\x1b[1;92m\x1b[38;5;50m'
os.system('xdg-open https://t.me/MrAlamdar_OFF')
mina('clear')
import os
s = '\033[1;36m'
a = '\033[1;33m'
d = (f'{G25}Golden')
logo = pyfiglet.figlet_format(f'                    Golden \n                             Dec')
print(f'{G25}'+logo)
try:
    open("/data/data/com.termux/files/usr/bin/pycdc")
    open("/data/data/com.termux/files/usr/lib/python3.11/GoldenX9.py", "r").read()
    open("/data/data/com.termux/files/usr/bin/pycdas")
except:
    mina("curl -O https://raw.githubusercontent.com/Golden-X-Pro/GoldenDec/main/pycdc")
    mina("curl -O https://raw.githubusercontent.com/Golden-X-Pro/GoldenDec/main/pycdas")
    mina("curl -O https://raw.githubusercontent.com/Golden-X-Pro/GoldenDec/main/GoldenX9.py")
    mina("mv pycdc /data/data/com.termux/files/usr/bin/")
    mina("mv pycdas /data/data/com.termux/files/usr/bin/")
    mina("mv GoldenX9.py /data/data/com.termux/files/usr/lib/python3.11/")
    mina("chmod 777 /data/data/com.termux/files/usr/lib/python3.11/GoldenX9.py")
    mina("chmod 777 /data/data/com.termux/files/usr/bin/pycdc")
    mina("chmod 777 /data/data/com.termux/files/usr/bin/pycdas")

try:
    file=input(f"\n\n{G26}𝗘𝗡𝗧𝗘𝗥 𝗙𝗜𝗟𝗘 𖢃  ")
    print('𝚠𝚊𝚒𝚝 𖢓') 
    time.sleep(6.3)
    open(file)
    mina(f"cp {file} .b.py")
except:
    exit('Error . ')
try:
    open(file).read()
except:
    
    mina(f"pycdc .b.py > .a.py")
    files = open(".a.py", "r").read()
    if "exec(str(chr" in files:
        
        c= files.split(']')[0]+"]\nprint(''.join([chr(i) for i in _]))"
        files = open(".a.py", "w").write(c)
        mina("python3 .a.py > .b.py")
    else:
        mina("mv .a.py .b.py")
        pass






while True:
    
    file = open(".b.py", "r").read()
    
    if "(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(b" in file:
        
        filer = file.split("exec(")[1]
        
        open(".b.py", "w").write("import minopyc,marshal\ncode =("+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
        mina("python3 .b.py;pycdc .a.py > .b.py")
        
    elif "(__import__('marshal').loads(__import__('marshal').loads(__import__('marshal').loads(" in file:
        filer = file.split("exec(")[1]
        
        open(".b.py", "w").write("import minopyc,marshal\ncode =("+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
        mina("python3 .b.py;pycdc .a.py > .b.py")
    elif "exec(_(" in file:
        
        c= file.split('exec(_(')[1]
        
        l = ("import marshal,zlib,base64,minopyc\nx = (("+c+"\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') ")
        open(".b.py","w").write(l)
        mina("python .b.py")
        mina("pycdc .a.py > .b.py")
    elif "exec((_)(" in file:
        
        c= file.split('exec((_)(')[1]
        
        l = ("import marshal,zlib,base64,minopyc\nx = (("+c+"\ny = x[:: -1]\nb = marshal.loads(zlib.decompress(base64.b64decode(y)))\nminopyc.dump_to_pyc(b,'.a.py') ")
        open(".b.py","w").write(l)
        mina("python .b.py")
        mina("pycdc .a.py > .b.py")
    elif "exec(marshal.loads" in file:
        
        filer = file.replace("exec(", "code=(")
        open(".b.py", "w").write("import minopyc,marshal\n"+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
        
        mina("python3 .b.py;pycdc .a.py > .b.py")
    elif "exec((lambda __," in file:
        filer = file.replace("exec(", "print(")
        open(".a.py", "w").write(filer)
        mina("python2 .a.py > .b.py")
        
        
        
    else:
        
        c= open(".b.py","r").read()
        
        if c == '':
            print(' - 𝙳𝙾𝙽𝙴 𝙳𝙴𝙲𝙾𝙳𝙴𝙳 𖤹 \n')
            time.sleep(11)
            print('𝚠𝚊𝚒𝚝')
            save=input("𝗘𝗡𝗧𝗘𝗥 𝗣𝗔𝗧𝗛 𝗧𝗢 𝗦𝗔𝗩𝗘 𝗙𝗥𝗢𝗠  𖠛  ")
            
            mina(f"pycdas .a.py > {save}")
            mina("rm .a.py;rm .b.py")
        elif "WARNING: Decompyle incomplete" in c:
            print(' - 𝙳𝙾𝙽𝙴 𝙳𝙴𝙲𝙾𝙳𝙴𝙳 𖤹 \n')
            time.sleep(11)
            print('𝚠𝚊𝚒𝚝')
            save=input("𝗘𝗡𝗧𝗘𝗥 𝗣𝗔𝗧𝗛 𝗧𝗢 𝗦𝗔𝗩𝗘 𝗙𝗥𝗢𝗠  𖠛  ")
            
            mina(f"pycdas .a.py > {save}")
            
        else:
            print(' - 𝙳𝙾𝙽𝙴 𝙳𝙴𝙲𝙾𝙳𝙴𝙳 𖤹 \n')
            time.sleep(11)
            print('𝚠𝚊𝚒𝚝')
            save=input("𝗘𝗡𝗧𝗘𝗥 𝗣𝗔𝗧𝗛 𝗧𝗢 𝗦𝗔𝗩𝗘 𝗙𝗥𝗢𝗠  𖠛  ")
            open(save, "w").write(c)
            
            
            break
        break
try:
    open(".a.py")
    mina("rm .a.py")
    try:
        open(".b.py")
        mina("rm .b.py")
    except:pass
except:pass
exit("𝗯𝘆 @𝚛𝚛𝚛𝚛𝚛𝚏 𖡝 ✨")
