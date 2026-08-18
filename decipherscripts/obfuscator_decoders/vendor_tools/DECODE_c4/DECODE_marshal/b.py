#!/usr/bin/python3
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


def show_code(source: str, temp):
    if not temp:
        p = Process(target=show_code, args=(source, 1))
        p.start()
        p.join(5)
        if p.is_alive():
            p.kill()
            console.print("# [yellow]can't show the code because the file is too big![/yellow]")
    else:
        syntax = Syntax(source, "python", line_numbers=True)
        console.print(syntax)


def show_info(file_type: str, layers: int):
    console.print(f"# [green]filename:[/green] {filename}")
    console.print(f"# [green]file-type:[/green] {file_type}")
    file_size_data = " ".join(os.popen(f"size '{filename}'").read().strip().split('\n')[-1].rsplit(" ", 2)[1:])
    console.print(f"# [green]file-size:[/green] ", end="")
    print(file_size_data)
    console.print(f"# [green]layers:[/green] {layers}")


def no_support():
    console.print("# No support currently! please wait for the new updates.")


def save_file(source, write_type="w"):
    os.system("clear")
    with open(output_file or filename, write_type) as out:
        out.write(source)
    if write_type == "wb":
        console.print("# [green]Decoded as pyc. Can't show bytes.[/green]")
    else:
        show_code(source, 0)


def decode_handler(layers=0):
    source = open_python_file(filename)
    file_type = get_file_type(filename)
    if file_type == "zip":
        pass
    elif type(source) == str:
        source: Union[str, None, CodeType] = FakeFunction(source, filename).get_source()
    elif type(source) == bytes:
        source: str = DecompilePyc(filename).get_source()
    else:
        no_support()

    if type(source) == str:
        layers += 1
        save_file(source)

    elif type(source) == CodeType:
        source: bytes = DecompileMarshal(source).get_source()
        layers += 1
        save_file(source, write_type="wb")
    else:
        no_support()

    show_info(file_type, layers)
    if input("# stop? [y/enter]: ").strip() != "y":
        decode_handler(layers=layers)



def get_arg_value(arg):
    try:
        _index = sys.argv.index(arg)
        value = sys.argv[_index + 1]
        del sys.argv[_index]
        del sys.argv[_index]
        return value
    except ValueError:
        pass
    except IndexError:
        os.system("readme decode")
        exit(0)

    return None


def main():
    global filename, output_file, py_version
    filename=input("entre file name:  ")
    with open(filename, 'r') as file:
        filename = file.read()
   # del sys.argv[0]
  #  if not sys.argv:
       # os.system("readme decode")
   #     output_file = get_arg_value("-o")
   #     py_version = get_arg_value("-pyV")
 #   for filename in sys.argv:
    #    if not os.path.isfile(filename):
      #      print(f"# File '{filename}' not found!")
  #          continue
    #    if not check(filename):
           # decode_handler()

if __name__ == "__main__":
    main()

