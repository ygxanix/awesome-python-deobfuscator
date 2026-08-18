P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m'
Black = '\033[0;30m'        
Red = '\033[0;31m'       
Green = '\033[0;32m'       
Yellow = '\033[0;33m'     
Blue = '\033[0;34m'         
purple = '\033[0;35m'    
Cyan = '\033[0;36m'        
White = '\033[0;37m'
import re
import subprocess
file="marshal.py"
def get_fun_name(code):
          pattern = r'exec[\s]*\((\w*?)\([\"\'].*'
          matches = re.findall(pattern, code, re.DOTALL)
          if len(matches)>0:
           return matches[0]
          else:
           return "d"
def getCode(file):
        with open(file,"r") as f:
                code=f.read()
        return code
def runBash(bash_command):
    # تنفيذ الأمر والتقاط الإخراج
    try:
        result = subprocess.check_output(bash_command, shell=True, stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        # في حالة حدوث خطأ
        result = e.output

    # الإخراج محفوظ في المتغير result
    
    #print(result)
    return result
    
def decode(fileIn):
	decoder=f"""\n
def {get_fun_name(getCode(fileIn))}(text, key):
    return ''.join(chr((ord(char) - key) % 65536) for char in text)\n
"""
	code=getCode(fileIn)
	fullCode=decoder+code.replace("exec","print")
	with open(fileIn,"w") as f:
		f.write(fullCode.replace("exec","print"))
	
	outs= runBash(f"python {fileIn}")
	if "print" in outs or "exec" in outs:
		with open(fileIn,"w") as f:
			f.write(outs)
		return outs
	else:
		return "error"

def decodeCaesar(file):
	x=1
	while decode(file)!="error":
		print("decode " +str(x))
		x+=1

def enc_normal():
    amerx= ('enc_normal')
    print(amerx)
    code = input(' [+] Єиτєя Fiℓє Иαмє » ')
    decodeCaesar(code)
    print("\n", purple + 'τнis τσσℓ ωαs ɒєcσɒєɒ вy ɒєcσɒєя ρяσ' + Cyan + '\n нαvє α ɢσσɒ ɒαy')
enc_normal()