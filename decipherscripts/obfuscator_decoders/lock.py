import os
import shutil
import re
import base64
import zlib
def remove_key_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    for i, line in enumerate(lines):
        if 'key =' in line:
            lines.pop(i)
            lines.pop(i)
    with open(file_path, 'w') as file:
        file.writelines(lines)
def replace_exec_with_print(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    file_content = file_content.replace("exec", "print")
    with open(file_path, 'w') as file:
        file.write(file_content)
def run_code_and_save_output(file_path, output_file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    try:
        with open(output_file_path, 'w') as output_file:
            exec(code, globals(), {'print': lambda x: output_file.write(str(x))})
    except Exception as e:
        output = f"Error during code execution: {str(e)}"
        with open(output_file_path, 'w') as output_file:
            output_file.write(output)
        raise e
    finally:
        os.remove(file_path)

def clean_output_file(output_file_path):
    with open(output_file_path, 'r') as file:
        content = file.read()
    content = re.sub(r'signature\s*=\s*".*?"', '', content)
    code_start = 'code = '
    code_end = '"""'
    start_index = content.find(code_start)
    end_index = content.find(code_end, start_index + len(code_start))
    content = content[:start_index] + content[end_index + len(code_end):]
    content = content.rstrip('"""\n')
    content = content.lstrip('\n')
    with open(output_file_path, 'w') as file:
        file.write(content)
def decode_and_save_code(encoded_code_path):
    with open(encoded_code_path, "r") as file:
        encoded_code = file.read()
    decoded_code = base64.b64decode(encoded_code)
    decompressed_code = zlib.decompress(decoded_code)
    with open(encoded_code_path, "w") as file:
        file.write("import marshal\nexec(marshal.loads(" + repr(decompressed_code) + "))")
        print("Done! The code has been decoded and saved to the same file.")

def handle_file(file_path):
    original_file_name = os.path.basename(file_path)
    user_id = hash(file_path)

    output_file_name = f"dec_{original_file_name}"
    output_file_path = os.path.join(os.path.dirname(file_path), output_file_name)

    shutil.copy(file_path, file_path + "_temp")
    remove_key_from_file(file_path + "_temp")
    replace_exec_with_print(file_path + "_temp")

    try:
        run_code_and_save_output(file_path + "_temp", output_file_path)
        clean_output_file(output_file_path)
        decode_and_save_code(output_file_path)

        print(f"تم الفك وحفظه في نفس المسار\n {output_file_path}")
    except Exception as e:
        pass
    finally:
        try:
            os.remove(file_path + "_temp")
            os.remove(output_file_path)
        except FileNotFoundError as e:
            pass

if __name__ == "__main__":
    file_path = input("قم بإدخال مسار الملف: ")
    handle_file(file_path)