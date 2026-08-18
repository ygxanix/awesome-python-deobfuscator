from os import system as mina
mina('clear')
logo = """
  __  __ _             
 |  \/  (_)            
 | \  / |_ _ __   ___  
 | |\/| | | '_ \ / _ \ 
 | |  | | | | | | (_) |
 |_|  |_|_|_| |_|\___/ 
 Creator : i4m mino
 im girl doesn't that mean girl cant coding🤍
 Teacher : Sasuke <>
 ~~~~~~~~~~~~
                       """
print(logo)
try:
    open("/data/data/com.termux/files/usr/bin/pycdc")
    open("/data/data/com.termux/files/usr/lib/python3.11/minopyc.py", "r").read()
    open("/data/data/com.termux/files/usr/bin/pycdas")
except:
    mina("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdc")
    mina("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/pycdas")
    mina("curl -O https://raw.githubusercontent.com/i4mMino/pycdc/main/minopyc.py")
    mina("mv pycdc /data/data/com.termux/files/usr/bin/")
    mina("mv pycdas /data/data/com.termux/files/usr/bin/")
    mina("mv minopyc.py /data/data/com.termux/files/usr/lib/python3.11/")
    mina("chmod 777 /data/data/com.termux/files/usr/lib/python3.11/minopyc.py")
    mina("chmod 777 /data/data/com.termux/files/usr/bin/pycdc")
    mina("chmod 777 /data/data/com.termux/files/usr/bin/pycdas")


file=input("Enter File Name You Want To Decode : ")
mina(f"cp {file} .b.py")
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
print('Please Wait Trying to Decoding , made By Mino')
while True:
    
    file = open(".b.py", "r").read()
    
    if "(__import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(b" in file:
        
        filer = file.split("exec(")[1]
        
        open(".b.py", "w").write("import minopyc,marshal\ncode =("+filer+"\nminopyc.dump_to_pyc(code, '.a.py')")
        mina("python3 .b.py;pycdc .a.py > .b.py")
        
    
    elif "exec(_(" in file:
        
        c= file.split('exec(_(')[1]
        
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
            print('The Tool Can Just Decoded Data & Saved At : decoded-Data.py')
            mina("pycdas .a.py > decoded-Data.py")
            mina("rm .a.py;rm .b.py")
        else:
            print('The Tool Decoded & Saved At : decoded-Tool.py')
            open("decoded-Tool.py", "w").write(c)
            mina("rm .a.py;rm .b.py")
            break
        break
      
exit("goodbye🤍")