from typing import Optional	
from subprocess import Popen, PIPE
print(''''
██████╗     ███████╗     ██████╗     ██████╗     ██████╗     ███████╗
██╔══██╗    ██╔════╝    ██╔════╝    ██╔═══██╗    ██╔══██╗    ██╔════╝
██║  ██║    █████╗      ██║         ██║   ██║    ██║  ██║    █████╗  
██║  ██║    ██╔══╝      ██║         ██║   ██║    ██║  ██║    ██╔══╝  
██████╔╝    ███████╗    ╚██████╗    ╚██████╔╝    ██████╔╝    ███████╗
╚═════╝     ╚══════╝     ╚═════╝     ╚═════╝     ╚═════╝     ╚══════╝                                                              
 ___                            ___           
(   )                          (   )          
 | |      .--.       .--.       | |   ___     
 | |     /    \     /    \      | |  (   )    
 | |    |  .-. ;   |  .-. ;     | |  ' /      
 | |    | |  | |   |  |(___)    | |,' /       
 | |    | |  | |   |  |         | .  '.       
 | |    | |  | |   |  | ___     | | `. \      
 | |    | '  | |   |  '(   )    | |   \ \     
 | |    '  `-' /   '  `-' |     | |    \ .    
(___)    `.__.'     `.__,'     (___ ) (___)                                            
''')
a=input("entre file hashlib: ")
name=a.split("/")[-1].split(".")[0]
a=open(a,"r").read()
a=a.replace("exec","#")
exec(a)

decrypted_script_custom = custom_decrypt(code)
exec(decrypted_script_custom)

key = "mokqfÇfehÆcfÇkdÈÇ"
code=marshal.loads(zlib.decompress(base64.b64decode(code.encode())))
import importlib, sys
pyc_data = importlib._bootstrap_external._code_to_timestamp_pyc(code)
with open('TAEMC4_lock.pyc', 'wb') as f:
    f.write(pyc_data)
    print("TAEMC4_lock.pyc")
class DecompilePyc:
    def __init__(self, filename: str):
        self.filename = filename
        
        self.std = Popen(["pycdc2", filename], stdout=PIPE,
                         stderr=PIPE)

    def get_source(self) -> Optional[str]:
        out = self.std.stdout.read().decode()
        err = self.std.stderr.read().decode()
        if out and err:
            return out + '\n' + err
        elif out:
            return out
        else:
            #print(err)
            return "you need to pycdc2 in termux to dec .pyc"
a=DecompilePyc("TAEMC4_lock.pyc").get_source()
b=open(f"dec_{name}.py","w")
b.write(a)
print(f"dec_{name}.py")
print(a)