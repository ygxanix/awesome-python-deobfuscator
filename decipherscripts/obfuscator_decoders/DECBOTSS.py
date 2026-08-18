import telebot
import os
import shutil
import re
import base64
import zlib
import time
from termcolor import colored
API_TOKEN = input('YOUR TOKEN :')
bot = telebot.TeleBot(API_TOKEN)
DOWNLOAD_DIR = "/sdcard/Download"
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
            exec(code, globals(), {'print': lambda x: output_file.write(str(x) + '\n')})
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
        print("Done!.")
def handle_file(file_path):
    original_file_name = os.path.basename(file_path)
    output_file_name = f"dec_{original_file_name}"
    output_file_path = os.path.join(DOWNLOAD_DIR, output_file_name)
    shutil.copy(file_path, file_path + "_temp")
    remove_key_from_file(file_path + "_temp")
    replace_exec_with_print(file_path + "_temp")
    try:
        run_code_and_save_output(file_path + "_temp", output_file_path)
        clean_output_file(output_file_path)
        decode_and_save_code(output_file_path)
        return output_file_path
    except Exception as e:
        raise e
    finally:
        try:
            os.remove(file_path + "_temp")
        except FileNotFoundError:
            pass
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Send me an encoded Python file to decode it.")
@bot.message_handler(content_types=['document'])
def handle_document(message):
    try:
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        file_path = os.path.join(DOWNLOAD_DIR, message.document.file_name)
        with open(file_path, 'wb') as new_file:
            new_file.write(downloaded_file)
        decoded_file_path = handle_file(file_path)
        with open(decoded_file_path, 'rb') as doc:
            bot.send_document(message.chat.id, doc)
        os.remove(file_path)
        os.remove(decoded_file_path)
    except Exception as e:
        bot.reply_to(message, f"Error occurred: {str(e)}")
def neon_text():
    colors = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
    text = "BY SALAR"
    for i, char in enumerate(text):
        print(colored(char, colors[i % len(colors)]), end='', flush=True)
        time.sleep(1)
    print()
neon_text()
bot.infinity_polling()