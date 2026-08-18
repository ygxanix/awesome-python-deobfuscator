#!python3
from zlib import decompress
from marshal import loads
from base64 import b16decode, b32decode, b32hexdecode, b64decode, b85decode
from sys import getsizeof
from os import system
file = input(' inetr: ') 

BYTES = 1024**0
KB = 1024**1
MB = 1024**2
GB = 1024**3
thresholds = (BYTES, KB, MB, GB)
units = ("B", "KB", "MB", "GB")

def funs_parser(funs_names: str, data_):
    t = ""
    s = "b¥b"
    for i in funs_names:
        if s not in t:
            t += f"{i}({s})"
            continue
        t = t.replace(s, f"{i}({s})")
    return t.replace(s, "{}".format(data_))

def get_encrypt_layers(names: tuple):
    all_ = ["decompress", "loads", "b16decode", "b32decode", "b32hexdecode", "b64decode", "b85decode"]
    names = list(names)
    return tuple([name for name in names if name in all_])
    
def fetch_biggest_byte(lbyt):
    lbyt = [i for i in lbyt if i.__class__ == bytes]
    largest = lbyt[0]
    for byt  in lbyt:
        if len(byt) > len(largest):
            largest = byt
    return largest

with open(file, 'r') as file:
    code = file.read()
    code_p = None
    cd_obj = compile(code, "<string>", "exec")
n = 0   

def size_handle(size_in_bytes: int) -> str:
    index = next((i for i, t in enumerate(thresholds) if t > size_in_bytes), len(thresholds) - 1)
    value = round(size_in_bytes / thresholds[index], 2)
    return foramt(size_in_bytes/thresholds[index], f".2f{units[index]}")

def init_code():
    global code
    global code_p
    length = len(code)
    n = 1000
    if length > n:
        code_p = code[: n] + f" ... [{length-100} letters, ]"
    else:
        code_p = code
                        

while True:
    n += 1
    system("clear")
    if cd_obj.__class__ == bytes:
        code = cd_obj.decode()
        cd_obj = compile(code, "<string>", "exec")
    elif cd_obj.__class__ == str:"
        code = cd_obj
        cd_obj = compile(code, "<string>", "exec")
    names = cd_obj.co_names
    data = cd_obj.co_consts
    current_layers = get_encrypt_layers(names)
    #print(names, data, sep="\n\n")
    try:
        byt_data =  fetch_biggest_byte(data)
        code = funs_parser(list(current_layers), byt_data)
    except IndexError:
        init_code()
        print(f"last_code\n\n{code_p}")
        break
    cd_obj = eval(code)
    print("current encrypting layers: ", end="")
    print(*current_layers, sep=",")
    init_code()
    print(f"No.{n}\ncurrent_code\n\n{code_p}")
    input("\npress <enter> to continue ")