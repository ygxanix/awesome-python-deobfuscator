#pylint:disable=E0001
import re


def function(source: str, function_name: str) -> str:
    pattern: str = r"(" + function_name + r"(?:[\s]+)?\()"
    while True:
        func_names = re.findall(pattern, source)
        if len(func_names) == 0:
            break

        for func_name in func_names:
            index = source.find(func_name)
            if index:
                break

        if index == -1:
            break
        text = func_name
        open_brakets = 1
        for char in source[index + len(func_name):]:
            text += char
            if char == ")":
                open_brakets -= 1
            elif char == "(":
                open_brakets += 1
            if open_brakets == 0:
                break

        yield source[source.find(text):source.find(text) + len(text)]
        source = source[:source.find(text)] + source[source.find(text) + len(text):]

import marshal
import base64
import zlib
import os
import time
import dis
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
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
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
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
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
a1 = '\x1b[1;31m'  # أحمر
a2 = '\x1b[1;34m'  # أزرق
a3 = '\x1b[1;32m'  # أخضر
a4 = '\x1b[1;33m'  # أصفر
a5 = '\x1b[38;5;208m'  # برتقالي
a6 = '\x1b[38;5;5m'  # أرجواني
a7 = '\x1b[38;5;13m'  # وردي
a8 = '\x1b[1;30m'  # أسود
a9 = '\x1b[1;37m'  # أبيض
a10 = '\x1b[38;5;52m'  # بني
a11 = '\x1b[38;5;8m'  # نـــمـــࢪودي
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
a34 = '\x1b[38;5;252m'  # نـــمـــࢪودي فاتح
a35 = '\x1b[38;5;246m'  # نـــمـــࢪودي داكن
a36 = '\x1b[38;5;228m'  # ذهبي فاتح
a37 = '\x1b[38;5;172m'  # ذهبي داكن
a38 = '\x1b[38;5;188m'  # فضي فاتح
a39 = '\x1b[38;5;247m'  # فضي داكن
a40 = '\x1b[0;34m'  # أزرق سماوي
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
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
#asu = random.choice([m,k,h,u,b])
AB_A='\x1b[1;97m' # ابيض خط عربض
RS='\x1b[30m' #رصاصي
AH_F='\x1b[31m'   #احمر فاتح
AKH_F='\x1b[32m' #اخضر فاتح
AS_T='\x1b[33m'#اصفر طوخ
SM='\x1b[34m'  #سمائي
BN='\x1b[35m'#بنفسجي
AZ_T='\x1b[36m'  #ازرك طوخ
AB_KH='\x1b[37m' #ابيض خط خفيف
AH_T='\x1b[91m'  #احمر طوخ
AKH_T='\x1b[92m'#اخضر طوخ
AS_F='\x1b[93m'    #اصفر فاتح
WR='\x1b[95m'      #وردي
p='\x1b[38;5;208m' #برتقالي
AH2='\x1b[38;5;204m' 
AS2='\x1b[38;5;220m'
MJ='\x1b[38;5;193m'
MJ2='\x1b[38;5;216m'
MJ3='\x1b[38;5;190m'
O='\x1b[0;96m'     # Biru Muda
P='\x1b[38;5;231m' # Putih
J='\x1b[38;5;208m' # Jingga
MJ4='\x1b[38;5;106m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
E = '\033[1;31m'
G = '\033[1;35m'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصف
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح
M = '\x1b[1;37m'#ابیض
S = '\033[1;33m'
Z = '\033[1;31m' #احمر
R = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
C1 = '\033[2;35m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
P = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
Z = '\x1b[1;31m'
R = '\x1b[1;31m'
X = '\x1b[1;33m'
F = '\x1b[2;32m'
C = '\x1b[1;97m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
E = '\x1b[1;31m'
B = '\x1b[2;36m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
F = '\x1b[2;32m'
L = '\x1b[1;95m'
E = '\x1b[1;31m'
G = '\x1b[1;32m'
S = '\x1b[1;33m'
Z = '\x1b[1;31m'
X = '\x1b[1;33m'
Z1 = '\x1b[2;31m'
F = '\x1b[2;32m'
A = '\x1b[2;39m'
C = '\x1b[2;35m'
B = '\x1b[2;36m'
Y = '\x1b[1;34m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
Z = '\x1b[1;30m'
sir = '\x1b[41m\x1b[1;97m'
x = '\x1b[m'
m = '\x1b[1;91m'
k = '\x1b[93m'
h = '\x1b[1;92m'
hh = '\x1b[32m'
u = '\x1b[95m'
kk = '\x1b[33m'
b = '\x1b[1;96m'
p = '\x1b[0;34m'
AB_A = '\x1b[1;97m'
RS = '\x1b[30m'
AH_F = '\x1b[31m'
AKH_F = '\x1b[32m'
AS_T = '\x1b[33m'
SM = '\x1b[34m'
BN = '\x1b[35m'
AZ_T = '\x1b[36m'
AB_KH = '\x1b[37m'
AH_T = '\x1b[91m'
AKH_T = '\x1b[92m'
AS_F = '\x1b[93m'
WR = '\x1b[95m'
p = '\x1b[38;5;208m'
AH2 = '\x1b[38;5;204m'
AS2 = '\x1b[38;5;220m'
MJ = '\x1b[38;5;193m'
MJ2 = '\x1b[38;5;216m'
MJ3 = '\x1b[38;5;190m'
O = '\x1b[0;96m'
W = '\x1b[38;5;231m'
J = '\x1b[38;5;208m'
MJ4 = '\x1b[38;5;106m'
r1 = '''[38;5;8m'''
m1 = '''[38;5;196m'''
a1 = '''[1;31m'''
a2 = '''[1;34m'''
a3 = '''[1;32m'''
a4 = '''[1;33m'''
a5 = '''[38;5;208m'''
a6 = '''[38;5;5m'''
a7 = '''[38;5;13m'''
a8 = '''[1;30m'''
a9 = '''[1;37m'''
a10 = '''[38;5;52m'''
a11 = '''[38;5;8m'''
a12 = '''[38;5;220m'''
a13 = '''[38;5;7m'''
a14 = '''[38;5;153m'''
a15 = '''[38;5;18m'''
a16 = '''[38;5;48m'''
a17 = '''[38;5;22m'''
a18 = '''[38;5;196m'''
a19 = '''[38;5;88m'''
a20 = '''[38;5;226m'''
a21 = '''[38;5;136m'''
a22 = '''[38;5;216m'''
a23 = '''[38;5;166m'''
a24 = '''[38;5;234m'''
a25 = '''[38;5;91m'''
a26 = '''[38;5;205m'''
a27 = '''[38;5;161m'''
a28 = '''[38;5;236m'''
a29 = '''[38;5;233m'''
a30 = '''[38;5;255m'''
a31 = '''[38;5;231m'''
a32 = '''[38;5;180m'''
a33 = '''[38;5;94m'''
a34 = '''[38;5;252m'''
a35 = '''[38;5;246m'''
a36 = '''[38;5;228m'''
a37 = '''[38;5;172m'''
a38 = '''[38;5;188m'''
a39 = '''[38;5;247m'''
a40 = '''[38;5;117m'''
P = '''[1;97m'''
M = '''[1;91m'''
H = '''[1;92m'''
K = '''[1;93m'''
B = '''[1;94m'''
U = '''[1;95m'''
O = '''[1;96m'''
N = '''[0m'''
Z = '''[1;30m'''
sir = '''[41m[1;97m'''
x = '''[m'''
m = '''[1;91m'''
k = '''[93m'''
h = '''[1;92m'''
hh = '''[32m'''
u = '''[95m'''
kk = '''[33m'''
b = '''[1;96m'''
p = '''[0;34m'''
os.system("clear")




 
   

    
def decode():
    
  #      print('')
 #    elif choice == "2":
    print(a1+'                                                 ██████╗  ███████╗  ██████╗  ██████╗  ██████╗  ███████╗')
    print(a2+'                                                 ██╔══██╗ ██╔════╝ ██╔════╝ ██╔═══██╗ ██╔══██╗ ██╔════╝')
    print(a3+'                                                 ██║  ██║ █████╗   ██║      ██║   ██║ ██║  ██║ █████╗')
    print(a4+'                                                 ██║  ██║ ██╔══╝   ██║      ██║   ██║ ██║  ██║ ██╔══╝')
    print(a5+'                                                 ██████╔╝ ███████╗ ╚██████╗ ╚██████╔╝ ██████╔╝ ███████╗')
    print(a6+'                                                 ╚═════╝  ╚══════╝  ╚═════╝  ╚═════╝  ╚═════╝  ╚══════╝')
    print(a7+'                                                                          @A_T_9')
    print(a8+'                                                                          @N_Z_8')
    print(a9+'                                                                      ress_ReSs_RESS')
    print('')
    print(a1+'〖01〗--»\033[1;34m  \033[41m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;31m Marshal [3.9] ')
    print(a1+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a1+'〖02〗--»\033[1;34m  \033[41m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;31m Marshal [3.11]  ')
    print(a1+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a1+'〖03〗--»\033[1;34m  \033[41m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;31m Marshal [3.12]  ')
    print(a1+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a1+'〖04〗--»\033[1;34m  \033[41m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;31m Marshal [3.13]  ')
    print(a1+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a2+'〖05〗--»\033[1;34m  \033[44m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;34m Enc Maeyouf  ')
    print(a2+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a2+'〖06〗--»\033[1;34m  \033[44m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;34m HEX ➤ bese64 ➤ zlib  ')
    print(a2+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')    
    print(a2+'〖07〗--»\033[1;34m  \033[44m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;34m HEX  ')
    print(a2+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a2+'〖08〗--»\033[1;34m  \033[44m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;34m Base64 ➤ Base16 ➤ Base32 ➤ Base85  ')
    print(a2+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')   
    print(a3+'〖09〗--»\033[1;34m  \033[42m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[0;32m zlib  ')
    print(a3+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')  
    print(a3+'〖10〗--»\033[1;34m  \033[42m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[0;32m lzma ➤ zlib ')
    print(a3+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')    
    print(a3+'〖11〗--»\033[1;34m  \033[42m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[0;32m gzip ➤ lzma ➤ zlib ')
    print(a3+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')     
    print(a3+'〖12〗--»\033[1;34m  \033[42m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[0;32m exec ( ( lambda ________• ________ : ________  ')
    print(a3+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')    
    print(a4+'〖13〗--»\033[1;34m  \033[43m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;33m base64 ➤ zlib  ')
    print(a4+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a4+'〖14〗--»\033[1;34m  \033[43m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;33m By Uncompyle6  ')
    print(a4+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a4+'〖15〗--»\033[1;34m  \033[43m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;33m By Mardis  ')
    print(a4+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬        ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a4+'〖16〗--»\033[1;34m  \033[43m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;33m By Pycdc   ')
    print(a4+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬        ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a5+'〖17〗--»\033[1;34m  \x1b[38;5;208m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[38;5;208m Strings  ')
    print(a5+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a5+'〖18〗--»\033[1;34m  \x1b[38;5;208m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[38;5;208m M.Maeyouf  ')
    print(a5+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a5+'〖19〗--»\033[1;34m  \x1b[38;5;208m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[38;5;208m lock (🔒)   ')
    print(a5+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a5+'〖20〗--»\033[1;34m  \x1b[38;5;208m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[38;5;208m Lambda ➤ Marshal ➤ Base64 ➤ zlib [V1]  ')
    print(a5+'    ▭▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a6+'〖21〗--»\033[1;34m  \033[45m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[38;5;5m Lambda ➤ Marshal ➤ Base64 ➤ zlib [V2]  ')
    print(a6+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a6+'〖22〗--»\033[1;34m  \033[45m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[38;5;5m Marshal ➤ Base64 ➤ BB5  ')
    print(a6+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a6+'〖23〗--»\033[1;34m  \033[45m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[38;5;5m _= lambda__ : __lmport__(zlib).  ')
    print(a6+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a6+'〖24〗--»\033[1;34m  \033[45m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[38;5;5m _=lambda__ : __import__(base64).  ')
    print(a6+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a8+'〖25〗--»\033[1;34m   \x1b[1;30m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;30m lambda ➤ Marshal ➤ zlib [V3]  ')
    print(a8+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a8+'〖26〗--»\033[1;34m  \x1b[1;30m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;30m 😀😁😂🤣😃😄😅😆  ')
    print(a8+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a8+'〖27〗--»\033[1;34m  \x1b[1;30m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;30m Base2  ')
    print(a8+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a8+'〖28〗--»\033[1;34m  \x1b[1;30m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;30m Base4  ')
    print(a8+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a9+'〖29〗--»\033[1;34m  \033[47m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;37m Base16  ')
    print(a9+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a9+'〖30〗--»\033[1;34m  \033[47m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;37m Base32  ')
    print(a9+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a9+'〖31〗--»\033[1;34m  \033[47m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;37m Base64  ')
    print(a9+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print(a9+'〖32〗--»\033[1;34m  \033[47m\x1b[1;97m⌯╼═══❬Decode═══╾⌯\x1b[0;34m\x1b[1;97m ➤ \x1b[1;37m Base85  ')
    print(a9+'    ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬         ▬▭▬▬▭▬▬▭▬▬▭▬▬▭▬▭▬▬          ')
    print('')
    print("\033[1;97m [###########################]")
    print("\033[1;97m [Cython decryption  [100] ")
    print("\033[1;97m [###########################]")
    print("\033[1;97m [Encryption changed  [200] ")
    print("\033[1;97m [###########################]")
    print("\033[1;97m [Automatic recognition  [300] ")
    print("\033[1;97m [###########################]")
    print("\033[1;97m [00] -  Exit Tool")

    
 
    
    
    
    print('')
    
    print('')    
    while True:
        choice = input("\033[1;97m[√] - Choose : ")
        if choice == "1":      
            
            os.system("clear")
            print('')          
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            data=str(open(file,"r").read())
            open("Dec_Als","w").write(data)
            os.system(f'marshal-magic Dec_Als -m normal -o Decode_Dec_Als')                    
            print('')
            time.sleep(2)
            print('\n') 
            print('[•] Decode Done √')
            time.sleep(1)
            exit()
        elif choice == "2":
            os.system("clear")
            alose2()
            print("")
        elif choice == "3":
            os.system("clear")
            alose3()
            print('')
        elif choice == "4":
            os.system("clear")
            alose4()
            print('')
        elif choice == "5":
            os.system("clear")
            alose5()
            print('')
        elif choice == "6":
            os.system("clear")
            alose6()
            print("")
        elif choice == "7":
            os.system("clear")
            alose7()
            print('')            
        elif choice == "8":
            os.system("clear")
            alose8()
            print('')
        elif choice == "9":
            os.system("clear")
            alose9()
            print('')
        elif choice == "10":
            os.system("clear")
            alose10()
            print('')
        elif choice == "11":
            os.system("clear")
            alose11()
            print('')
        elif choice == "12":
            os.system("clear")
            alose12()
            print('')
        elif choice == "13":
            os.system("clear")
            alose13()
            print('')
        elif choice == "14":
            os.system("clear")
            alose14()
            print('')
        elif choice == "15":
              os.system("clear")
              os.system("python3.9 /storage/emulated/0/Decode_Ali3/marshal55.py")
        elif choice == "16":
              os.system("clear")
              os.system("python3.9 /storage/emulated/0/Decode_RESS/decode_mar.py")
        elif choice == "17":
            os.system("clear")
            alose17()
        elif choice == "18":
            os.system("clear")
            alose18()
        elif choice == "19":
            os.system("clear")
            alose19()
            
        elif choice == "20":
            os.system("clear")
            alose20()
def alose2():
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            open("Dec_Als","w").write(data)
            os.system("python2 Dec_Als > Decode_Dec_Als")
            print('')                                  
            time.sleep(2)
            print('[•] Decode Done √')
            time.sleep(1)
            exit()  
            
def alose2():
            os.system("clear")
            print('')
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            open("Als_By.py","w").write(data)
            os.system("python2 Als_By.py > Decode_Als_By.py")
            print('')                                  
            time.sleep(2)
            print('[•] Decode Done √')
            time.sleep(1)
            exit()   
def alose3():
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","encrypt1 = ")
            data2=f"""{data}\nwith open('dec_file.py','w') as file: 
            file.write(str(encrypt1))"""
            
            open("Dec_Als","w").write(data2)
            os.system("python2 Dec_Als > Decode_Dec_Als")
            print('')                                  
            time.sleep(2)
            print('[•] Decode Done √')
            time.sleep(1)
            exit()	                 
        
def alose4():     
            os.system("clear")
            print('Welcome To Decode Uncompyle 6 [Under Maintenance]')
            print('')          
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")         
            data=str(open(file,"r").read())
            open("Als_By.py","w").write(data)
            os.system(f'marshal-magic Als_By.py -m normal -o Decode_Als_By.py')                    
            alose=str(open("Decode_Als_By.py","r").read())
            data3=f"""#Decode By "Als_By"\n{alose}"""
            open("Decode_Als_By.py","w").write(data3)
            time.sleep(1)
            print('\n') 
            print('[•] Decode Done √')
            time.sleep(1)
            os.system("clear")
            exit()   
def alose5():
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            with open(file, mode='w') as save_dis:
                os.system(f'mardis {file}')
            exit()           
            print('')
            time.sleep(2)
            print('\n') 
            print('[•] Decode Done √')
            time.sleep(1)
            exit() 
            
def alose6():    
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")       
            with open(file, mode='w') as save_dis:
                os.system(f'pycdc {file}')
                time.sleep(2)
                print('\n')
                print('[•] Decode Done √')    
                time.sleep(1)
                exit()
                
def alose7():    
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")         
            with open(file, mode='w') as save_dis:
                os.system(f'strings {file}')
                time.sleep(2)
                print('\n')
                print('[•] Decode Done √')    
                time.sleep(1)
                exit()
def alose8():    
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")         
            data=str(open(file,"r").read())
            open("Als_By.py","w").write(data)
            os.system(f'marshal-magic Als_By.py -m normal -o Decode_Als_By.py')                    
            print('')
            time.sleep(2)
            print('\n') 
            print('[•] Decode Done √')
            time.sleep(1)
            exit()

def alose9():    
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec(marshal.loads(zlib.decompress(base64.b64decode(code.encode()))))","print((zlib.decompress(base64.b64decode(code.encode()))))")
            open("Dec_Als","w").write(data)
            os.system("python Dec_Als > Decode_Dec_Als")
            print('')
            time.sleep(2)
            print('\n') 
            print('[•] Decode Done √')
            time.sleep(1)
            exit()            
def alose10():                          
            os.system("clear")
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")
            print('')
            print('\n') 
            print('[•] Decode Done √')
            menu()
def alose11():    
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")  
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")             
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")                         
            file=input("\x1b[1;31m[\x1b[1;31mDecode Dec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("exec(_(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Dec_Als","w").write(data2)            
            os.system("python Dec_Als > Decode_Dec_Als")
            als=str(open("Decode_Dec_Als","r").read())
            data3=f"""#Decode By Dec\nimport marshal\nexec(marshal.loads({als}))"""
            open("Dec_Als","w").write(data3)
            os.system("marshal-magic Dec_Als -m normal -o Decode_Dec_Als")                                     
            print('')
            print('\n') 
            print('[•] Decode Done √')
            exit()     
def alose12():    
            print('')
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            open("Als_By.py","w").write(data)
            os.system("python Als_By.py > Decode_Als_By.py")
            alose=str(open("Decode_Als_By.py","r").read())
            data3=f"""#Decode By "Als"\n{alose}"""
            open("Decode_Als_By.py","w").write(data3)    
            alose2()    
def alose13():    
            print('Decode |  lambad zlib')
            print('')
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            data2="""_ = lambda __ : __import__('zlib').decompress(__[::-1])\n"""
            open("Dec_Als","w").write(data)
            os.system("python2 Dec_Als > Decode_Als_By.py")
            print('')                                  
   
            print('[•] Decode gone √')
            time.sleep(1)
            print('')
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
 
            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
       
            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
 
            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
       
            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
 
            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
       
            print('[•] Decode gone √')
            
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            time.sleep(1)
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
 
            print('[•] Decode gone √')
            
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
       
            print('[•] Decode gone √')
            
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
          
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
 
            print('[•] Decode gone √')
   
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
          
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  

            print('[•] Decode gone √')
            
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            
            data2=f"""_ = lambda __ : __import__('zlib').decompress(__[::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            print('')                                  
       
            print('[•] Decode gone √')
            exit()

def alose14():    
            
            print('')        
            file=input("\033[2;32m[\x1b[\x1b[38;5;208mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")            
            data2=f"""_ = lambda  : import('base64').b64decode([::-1]);{data}"""
            open("Dec_als.py","w").write(data2)
            os.system("python2 Dec_als.py > Decode_Als_By.py")
            als=str(open("Decode_Als_By.py","r").read())
            data3=f"""#Decode By "Dec als"\n{als}"""
            open("Decode_Als_By.py","w").write(data3)   
def alose15():
            print('')        
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")            
            data2=f"""_ = lambda __ : __import__('base64').b64decode(__[::-1]);{data}"""
            open("Als_By.py","w").write(data2)
            os.system("python2 Als_By.py > Decode_Als_By.py")
            als=str(open("Decode_Als_By.py","r").read())
            data3=f"""#Decode By "Dec als"\n{als}"""
            open("Decode_Als_By.py","w").write(data3)
            alose15()
def alose17():
            print('')
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            open("Als_By.py","w").write(data)
            os.system("python Als_By.py > Decode_Als_By.py")
            alose=str(open("Decode_Als_By.py","r").read())
            data3=f"""#Decode By "Als"\n{alose}"""
            open("Decode_Als_By.py","w").write(data3)    
            alose17()    
def alose18():
            print('')
            file=input("\x1b[1;31m[\x1b[1;31mAls\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            open("dec_codecs.py","w").write(data)
            os.system("python dec_codecs.py > Decode_Als_codecs.py")
            alose=str(open("Decode_Als_codecs.py","r").read())
            data3=f"""#Decode By "Als"\n{alose}"""
            open("Decode_Als_codecs.py","w").write(data3)    
            alose18()
def alose19():
            print('')
            file=input("\x1b[1;31m[\x1b[1;31mDec\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())
            data=ogge.replace("exec","print")
            open("Als_By.py","w").write(data)
            os.system("python Als_By.py > Decode_Als_By.py")
            alose=str(open("Decode_Als_By.py","r").read())
            data3=f"""#Decode By "Als"\n{alose}"""
            open("Decode_Als_By.py","w").write(data3)   
def alose20():
            os.system("clear")
            file=input("\x1b[1;31m[\x1b[1;31mDecode Plya_Team\x1b[1;31m] \033[1;97m> - Enter File : ")
            ogge=str(open(file,"r").read())          
            data=ogge.replace("_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(b","_ =") 
            data2=f"""import base64\nimport zlib\n{data}\n
y = _[::-1]

d = base64.b64decode(y)

b = zlib.decompress(d)

print(b)
 """           
            open("Plya_Als.py","w").write(data2)            
            os.system("python als_by.py > Decode_Plya_Team.py")
            besto=str(open("Decode_Dec_by.py","r").read())
            data3=f"""#Decode By Plya Team\nimport marshal\nexec(marshal.loads({besto}))"""
            open("Als_by.py","w").write(data3)
            os.system("marshal-magic Plya_Team.py -m normal -o Decode_Plya_Team.py")
            print('')
            print('\n') 
            print('[•] Decode Done √')
            
            
        
            	      	    	      
        



                   
                  
                  	           	                  	            	           	                  	            
if __name__ == "__main__":
    decode()