import requests
import random
import os
from user_agent import generate_user_agent
import pyfiglet
import sys
import time
os.system('clear')
os.system('clear')

# = = = = = = = = = = = = 

Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح


def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)


to(
    f"\033[31;m TOOL >> \033[1;36mACCOUNT CREATOR\n\033[1;31m DEVELOPER >>\033[1;33m @Theyhates_joker\n\033[31;m")
print('')
print('\033[32;m')

from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except:
    system('pip install websocket-client')
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []


def work():
    global failed, success, retry
    username = choice('qwertyuiooasdfghjklzxcvpbnm') + ''.join(choices(list('qwertyuioasdfghjklzxcvbnpm1234567890'), k=16))
    try:
        con = create_connection("wss://195.13.182.213/Auth",
                                header={"app": "com.safeum.android", "host": None, "remoteIp": "195.13.182.213",
                                        "remotePort": str(8080), "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                                        "time": "2024-04-11 11:00:00", "url": "wss://51.79.208.190/Auth"},
                                sslopt={"cert_reqs": CERT_NONE})
        con.send(dumps(
            {"action":"Register","subaction":"Desktop","locale":"en_GB","gmt":"+05","password":{"m1x":"2077bbef25efe7518d487a570cb5cff8bacce03bb8418cc2a72c83f987e8e02d","m1y":"4aee85ecae1ce39e52d690c662f341885dffa280417a62c3c26830d51a0441a0","m2":"57223fab5ca6a91db7de1ecf173cee63c398017f8d73b8d43fa3981a325ea4f2","iv":"b6b6ad34a53220f1b38e90a7fac885c7","message":"4fdd6b0d4261b56507a814f8358599fa9bce770d209f243e0ab3aa1a411b69414f99388249d4a4e2b006bdc72c7f1afa8a53b98912cfe088b1894c0edfeb2e160f79e19ba8964eacb92f0875ad18a7a9"},"magicword":{"m1x":"fc4762a0cd77ffdae1f58f98a84b3a28503110925c7e675bfc1827044b62625e","m1y":"fa551a50e6b7aa7fecff96b115fbddeaff7664ec19f51139892434d04a566ccd","m2":"2a5e35d6b73977416ff99832f897d6a13190bdbef9bf1c9cb0ad7e7d8e6ed755","iv":"e5f21c784e485b6b923c75b80e8e33b6","message":"2096641ea3c7858d3085a9123b3ae7c3"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi 23106RN0DA","softwareversion":"1.1.0.2300","nickname":"bsgsh827bajhsgacs","os":"AND","deviceuid":"7796efb323b2256e","devicepushuid":"*f92aqZpYSn2P-E7ppWbR0J:APA91bGgELDGPktrrRKqhpc4IWptOHq1ApVl9lQOWi5UzR7KmDDRmStUvdH_EAyyb5vJTDnC20708oKa1wwQT9bSjiu3RSz85a2WB8hCVBU9auPEQrNnTQjK5C3HW_4-jc7vL6u7gsgF","osversion":"and_13.0.0","id":"1457177093"}))
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            b = accounts.append(username + ':bhai')
            print(b)
            with open('SafeUM.txt', 'a') as f:
                f.write(username + ":bhai | TG : @Theyhates_joker\n")

        else:
            failed += 1
    except:
        retry += 1


start = ThreadPoolExecutor(max_workers=1000)


while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + 'Success : ' + str(success) + '\n\n\n' + ' ' * 25 + 'Failed : ' + str(
        failed) + '\n\n\n' + ' ' * 25 + 'ReTry : ' + str(retry))
    hh = str(failed) + str(success) + str(retry)
    if int(success) >= 200:
        fuck()
        print("Created Acc successfull")
        
    
    if int(success) > int(0):
        z = "\n".join(accounts)
        
        print("CREATED ACCOUNTS>>\n", z)
        

    os.system('clear')
