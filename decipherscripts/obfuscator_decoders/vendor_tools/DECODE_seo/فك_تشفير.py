def SVT(EN_PATH, DE_FILE):
    BIGIN = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b'"
    END = "'))"
    with open(EN_PATH, 'r') as file:
        EN_COD = file.read()
    BIGIN_IND = EN_COD.find(BIGIN) + len(BIGIN)
    END_IND = EN_COD.find(END, BIGIN_IND)
    if BIGIN_IND != -1 and END_IND != -1:
        MSTKHRJ = EN_COD[BIGIN_IND:END_IND]
        with open(DE_FILE, 'w') as file:
            file.write(MSTKHRJ)        
        return MSTKHRJ
    else:
        return None
EN_PATH = input("[?] FILE PATH :")
DE_FILE = "/storage/emulated/0/DECODED_FILE_BABY.py"
MSTKHRJ = SVT(EN_PATH, DE_FILE)
if MSTKHRJ is not None:
    print(f"DONE")
else:
    print("NOT DONE")    
import base64
import zlib
import os
NAME_PATH = DE_FILE
while True:
    try:
        os.system("clear")
        with open(NAME_PATH, "r", encoding="utf-8") as file:
            DEMO = file.read()
        y = DEMO[::-1]
        d = base64.b64decode(y)
        b = zlib.decompress(d)
        b_trimmed = b[53:-48]
        with open(NAME_PATH, "w", encoding="utf-8") as file:
            file.write(repr(b_trimmed)[2:-1])
        print("DONE 🔓")
    except Exception as e:
        print(f"ERROR")
        print("SAVE IT 🔓")
        with open(NAME_PATH, "w", encoding="utf-8") as file:
            file.write(repr(b)[2:-1])            
        with open(NAME_PATH, "w") as file:
                file.write("import marshal\nexec(marshal.loads(" + repr(b) + "))")
        print("SAVE IT 👍")