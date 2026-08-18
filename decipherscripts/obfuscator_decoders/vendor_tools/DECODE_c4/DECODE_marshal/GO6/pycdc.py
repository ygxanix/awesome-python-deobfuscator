import os,time,sys
import py_compile
def slow(T):
    for r in T + '\n':
        sys.stdout.write(r)
        sys.stdout.flush()
        time.sleep(0.03)
def seo_is_taemC4():
    anim = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□","[\x1b[1;92m■■\x1b[0m□□□□□□□□", "[\x1b[1;93m■■■\x1b[0m□□□□□□□", "[\x1b[1;95m■■■■\x1b[0m□□□□□□", "[\x1b[1;94m■■■■■\x1b[0m□□□□□", "[\x1b[38;5;26m■■■■■■\x1b[0m□□□□", "[\x1b[1;96m■■■■■■■\x1b[0m□□□", "[\x1b[38;5;86m■■■■■■■■\x1b[0m□□", "[\x1b[38;5;96m■■■■■■■■■\x1b[0m□", "[\x1b[38;5;203m■■■■■■■■■■\x1b[0m]"]
    am = ('\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m','\x1b[38;5;203m')
    for i in range(30):
        time.sleep(0.1)
        os.system('clear')
        sys.stdout.write(f"\r \x1b[38;5;203mdecode_TAEMC4_Tools... \033[1;92m" + anim[i % len(anim)] +"\x1b[0m ")
        sys.stdout.write(f"\r \x1b[38;5;203mdecode_TAEMC4_Tools ... \033[1;92m" + am[i % len(am)] +"\x1b[0m ")
        sys.stdout.flush()
seo_is_taemC4()
os.system('clear')
try:
 from cfonts import render, say
except:
 os.system('pip install python-cfonts')
output = render('T A E M C 4', colors=['white', 'red'], align='center')
print(output)
def decode_fix_pyc():
   slow('''                                     
  ____    _____    ____           ____   __   __   ____ 
 |  _ \  | ____|  / ___|         |  _ \  \ \ / /  / ___|
 | | | | |  _|   | |             | |_) |  \ V /  | |    
 | |_| | | |___  | |___          |  __/    | |   | |___ 
 |____/  |_____|  \____|  _____  |_|       |_|    \____|
                         |_____|                        
   ''')
   input_file = input('Enter the input file: ')
   output_file = 'dec_TAEMC4.py'
   decode_command = f'pycdc {input_file} > {output_file}'
   os.system(decode_command)
   slow('Decoding done by ᏆℰᎯℳ_ℂ4 𖠏 *_*')

decode_fix_pyc()