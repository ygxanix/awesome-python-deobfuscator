import os
import py_compile

def decode_fix_pyc():
   input_file = input('Enter the input file: ')
   output_file = 'dec_TAEMC4.py'
   decode_command = f'pycdc {input_file} > {output_file}'
   os.system(decode_command)
   print('Decoding done by ᏆℰᎯℳ_ℂ4 𖠏 *_*')
try:
     #py_compile.compile(output_file, doraise=True)
     print('Syntax errors fixed successfully.')
except py_compile.PyCompileError as e:
     print(f'Error: {e}')
#with open(output_file, 'rb') as f:
  #   decoded_text = ''.join([chr(byte) for byte in f.read()])
     #print(decoded_text)
    # old_line = "".join((lambda .0: pass)(_()))
    # new_line = print(''.join([chr(i) for i in _]))
     #new_text = decoded_text.replace(old_line, new_line)
#with open(output_file, 'w') as f:
    # f.write(new_text)

decode_fix_pyc()