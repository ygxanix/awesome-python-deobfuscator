import marshal
b=input("entre file marshal: ")
a=open(b).read()
m=False
k=""
n=0
for x in a:
	if x=="'" and a[n-1]=="b":
		m=True
		continue
	if x=="'" and not  a[n-1]=="\\":
		break
	if m:
		k=k+a[n+1]
	n+=1
k+="'"
k="b'"+k
a=f'''e=(marshal.loads({k}))'''
exec(a)
e=e.co_consts
while True:
 try:
  for x in range(len(e)):
   if "b'"in str(e[x]):
   	break
  if "b'"in str(e[x]):
   a=f'''e=(marshal.loads({e[x]}))'''
   mm=str(e[x])
   exec(a)
   e=e.co_consts
  else:
   break
 except:
 	break
byt= b'a\r\r\n\x00\x00\x00\x00\xf6\x971a\x00\x00\x00\x00'
a=b.replace(".py","_dec.py")
aa=b.replace(".py","_dec.pyc")
e=f'''import marshal as m\nexec(m.loads({mm}))'''
ee=f'''import dis\nimport marshal\nmarshal_c=marshal.loads({mm})\nbyte_string = {byt}\nwith open('{aa}', 'wb') as pyc:\n pyc.write(byte_string )\n marshal.dump(dis.Bytecode(marshal_c).codeobj, pyc)'''
f=open(a,"w");f.write(e)
exec(ee)
print(a)
print(aa)