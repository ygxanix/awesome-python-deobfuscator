'''import os, sys
os.system('pkg install python')
os.system('pkg install tur-repo')
os.system('pkg update')
os.system('pkg install python3.9')
os.system('pip3.9 install rich')
os.system('pip3.9 install requests')
os.system('pip3.9 install autopep8')
os.system('pip3.9 install telebot')
os.system('cp Dev1.py /data/data/com.termux/files/usr/bin')'''
import os
#os.system('cp pycdc2 /data/data/com.termux/files/usr/bin')
#os.system('cd /data/data/com.termux/files/usr/bin')
#os.system('chmod +x *')
#os.system('cd /storage/emulated/0/TEAM_RDA/')
import telebot,requests,sys,autopep8
from telebot import TeleBot
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
from sys import argv
import time  
from os import system, chdir, path
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
		

Copyright=['@DEVIL_DECODER']
		
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
	p='''DEVIL_DECODER = False
if DEVIL_DECODER:
    
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
		source =source.replace(h,"    os.system('pip install")
	cobe="#Decoded By  : @obh_44  : @DEVIL_DECODER \n\n"
	#source=cobe+source+'\n'+cobe
#	source=source.split('        ')
#	source=''.join(source)
#	source=autopep8.fix_code(source)
#	source=autopep8.fix_code(source)
#	source=autopep8.fix_code(source)
#	source=autopep8.fix_code(source)
#	source=autopep8.fix_2to3(source)
#	source=yapf.file_resources(source)
#	source=autopep8.fix_lines(source)
	#Kill_non('decoded.py')

#	os.system('autopep8 --in-place --aggressive --aggressive decoded.py')
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
        p.join(30)
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
        self._magic_number: bytes = b'a\r\r\n\x00\x00\x00\x00\tq\x98d\x0b\x00\x00\x00'
        

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



def get_bytecode(source: str) -> CodeType:
    return compile(source, "<strings>", "exec")


def get_bytecode_from_file(filename: str) -> CodeType:
    try:
        with open(filename, "r") as f:
            data = f.read()
        return get_bytecode(data)
    except UnicodeDecodeError:
        with open(filename, "rb") as f:
            data = f.read()
        return marshal.loads(data[16:])

def clean_source(source: Union[str, bytes]) -> Union[str, bytes, CodeType]:
    if type(source) == str:
        try:
           
            #source=source.replace("'))","'")
            
            #open('3737373737373','w').write(source)
            get_bytecode(source)
            return source
        except SyntaxError:
           # print(source)
           
            print("# This is not a python file or maybe there is a syntax error!")

            
        except ValueError:
            return source.encode()
    try:
        
        return source.decode("utf-8")
    except UnicodeDecodeError :
        return get_bytecode(source)
def open_file(filename) -> Union[str, bytes, CodeType]:
    try:
        with open(filename, "r") as r_file:
            source=r_file.read()
            
            source=source.replace("exec(loads","exec(marshal.loads")
            h="WARNING: lin/ker: /data/data/com.termux/files/usr/bin/pycdc2: unsupported flags DT_FLAGS_1=0x8000001"
            source =source.replace(h,"#")
            h="WARNING: linker: /data/data/com.termux/files/usr/bin/pycdc: unsupported flags DT_FLAGS_1=0x8000001"
            source =source.replace(h,"#")
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
            source=source.replace("exec((_)(","_ = lambda __ : __import__('zlib').decompress(__[::-1]);exec((_)(")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('base64').b64decode(__[::-1]);exec((_)(")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)(")
            source=source.replace("exec(loads","exec(marshal.loads")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__[::-1]));exec((_)(")
            source=source.replace("exec((_)(","_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(")
            
            source=source.replace("exec(_(","_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(")
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
	os.system('clear')
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
				xe3=marsh3(xe3)
				
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
		#Pyprivet(outo).source()
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
				open('dhdhrhrhrhd.txt','w').write(file)
				
				print('7t74ueuru3u3u')
				
				save(file,'w','ou')
				
				
				
			
				
				
				
			
			#pass
				

		except Exception as E:
			print(E)
			print('okk')

		
	
	
	

	

def decoder(la,lo:Optional[int] =1 ):
    
    
	
	
	
	
	la+=1
	
	source = open_python_file(outo)
	
	file_type = get_file_type(outo)
	
#	print(source)	
	if file_type == "zip":
	       pass
	elif type(source)==str:
	     if 'x84!Z' in source:
	     	open('47474747474.txt','w').write(source)
	     	print(7437373737)
	     	Pyprivet(source).source()
	     


	           	
	           
	           	
	           		       
	      

	     source: Union[str, None, CodeType] = FakeFunction(source, outo).get_source()
	           	
	     	
	     
	     
	     
	      
	       	
	       	
	       	#print(source)
	       	
	       	
	       
	       	
	       	
	       
	       
	       
	       
	
	elif type(source) == bytes:
	       
	       
	       source: str = DecompilePyc(outo).get_source()
#	       if '(lambda'  in source :
	           
#	           print(source)
#	           print(lo)
	           
#	           marsh3()
	           
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

	           
	     
	       
	       
	       	
#	       source=source.replace('# File: AFRIT(0.1)(2).py (Python 3.9)','#decoded by @obh_44')
#	       source=source.split('# Source Generated with Decompyle++')[1]
#	       source=source.split('Warning:')[0]

	       show_code(source, 0)
	       save(source,'w','ou') 
	       if 'def d(_, __):' in source:
	            m='''def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
def e(a):
    exec(a, globals())
c=-128548'''+"\n"
	            save(m+source,'w','ou')
	       if 'exec(base58' in source:
	           try:
	               source=source.split('exec(base58')[1].split("'))")[0]
	               source='import base58\nexec(base58'+source+"'))"
	               save(source,'w','ou')
	               decoder(la,lo)
	           except IndexError:
	               source=source.split('exec(base58')[1].split('"))')[0]
	               source='import base58\nexec(base58'+source+'"))'
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
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"+"\n"
	                    save(m+source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));exec((_)('''+source+'"))'
	               save(m+source,'w','ou')
	               decoder(la,lo)	               
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"+"\n"
	                    save(m+source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1])); exec((_)('''+source+'"))'
	               save(m+source,'w','ou')
	               decoder(la,lo)	               
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('marshal').loads(__import__('zlib').decompress(__import__('base64').b64decode(__[::-1])));"+"\n"
	                    save(m+source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('marshal').loads(__[::-1]);exec((_)('''+source+'"))'
	               save(m+source,'w','ou')
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
	               m='''def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
def e(a):
    exec(a, globals())
c=-128548'''+"\n"
	               save(m+source,'w','ou')
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
	                     if 'exec((_)(' in source:
	                      try:
	                       source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(''')[1].split("'))")[0]
	                       source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)('''+source+"'))"
	                       save(source,'w','ou')
	                       decoder(la,lo)
	                      except IndexError:
	                        source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)('''+source+'"))'
	               save(source,'w','ou')
	               decoder(la,lo)	               	               
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
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));"+"\n"
	                    save(m+source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)('''+source+'"))'
	               save(m+source,'w','ou')
	               decoder(la,lo)	           
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));"+"\n"
	                    save(m+source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b32decode(__[::-1]));exec((_)('''+source+'"))'
	               save(m+source,'w','ou')
	               decoder(la,lo)	         
	               if 'exec((d(' in source:
	                   try:
	                    source=source.split('''def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
def e(a):
    exec(a, globals())
c=-128548''')[1].split("'))")[0]
	                    source='''def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
def e(a):
    exec(a, globals())
c=-128548;exec((d('''+source+"')))"
	                    m =''' def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
def e(a):
    exec(a, globals())
c=-128548'''+"\n"
	                    save(m+source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
def e(a):
    exec(a, globals())
c=-128548exec((d)(''')[1].split('"))')[0]
	               source='''def d(_, __):
    ___ = [chr((ord(char) - __) % 65536) for char in _]
    return ''.join(___)
def e(a):
    exec(a, globals())
c=-128548;exec((d)('''+source+'"))'
	               save(m+source,'w','ou')
	               decoder(la,lo)	          
	               if 'exec(_(' in source:
	                   try:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)(''')[1].split("'))")[0]
	                    source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)('''+source+"'))"
	                    m = "_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));"+"\n"
	                    save(m+source,'w','ou')
	                    decoder(la,lo)
	                   except IndexError:
	                    source=source.split('''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)(''')[1].split('"))')[0]
	               source='''_ = lambda __ : __import__('zlib').decompress(__import__('base64').b16decode(__[::-1]));exec((_)('''+source+'"))'
	               save(m+source,'w','ou')
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
	        m='''
# --> Done Decoded By RDA_Team <\> DecodeV++
# --> Follow us in Telegram as @Team_RDA
# --> Developed By :  Ress'\n''' 
	        save(m+source,'w','ou')
	        decoder(la,lo)
	       	file=open('/storage/emulated/0/TEAM_RDA/Decode_Team-RDA.py','r').read()
	       	open(outo,'w').write(open('/storage/emulated/0/TEAM_RDA/decoded.py','r').read())
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
	       				kill_non('/storage/emulated/0/TEAM_RDA/decoded.py')
	       				open(outo,'w').write(open('/storage/emulated/0/TEAM_RDA/decoded.py','r').read())

	       				       				
	       				la=0
	       				return 1
	       				pass 
	       				pass	       	
	        if '57]).decode():' in source:
	           pass
	           if 'exec(marshal.loads(' in source:
	           	Byto(source).en_marsh()
	           else:
	           	Byto(source).source()
	           
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
		
def main(na,m):
	global file,into,outo, lay,reb,la,outo
	lo=0
	la=layrs
	reb=m
	into=na
	outo='Decode_Team-RDA.py'
	try:
	    file=open(into,'r').read()
	    open(outo,'w')
	    save(file,'w','ou')
	    file=open(outo,'r').read()
	    lay=0
	    while 1 > lay:
	        lay+=1
	        print('\x1b[1;92m\x1b[38;5;46mWait .............')
	        file=open(outo,'r').read()	        
	        decoder(la,lo='anything')
	except UnicodeDecodeError:		
		file=open(into,'rb').read()
		decoder(la,lo)
		
        



layrs=1
args = argv[1: ]
if not args:
    print("select file \nUseng: python3.9 Dump1.py filename")
    exit()
na = args[0]
if not path.isfile(na):
    print("the file not found")
d=1
main(na,d)    
