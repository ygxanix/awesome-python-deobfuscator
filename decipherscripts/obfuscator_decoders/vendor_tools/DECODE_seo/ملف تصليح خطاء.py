import telebot
from autopep8 import fix_code
import os
from time import sleep

API_TOKEN = ''#توكن
bot = telebot.TeleBot(API_TOKEN)

users_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    users_data[user_id] = {'file_path': '', 'HUSSElN_file_path': ''}
    welcome_message = "ارسل ملف اتريد تصلح خطاء\n\nPython   "

    
    markup = telebot.types.InlineKeyboardMarkup()
    python_button = telebot.types.InlineKeyboardButton("Python ", callback_data='python')

 

    
    developer_button = telebot.types.InlineKeyboardButton("مصدر", url="https://t.me/SX_9O")
    markup.add(developer_button)

    bot.send_message(message.chat.id, welcome_message, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    user_id = call.from_user.id
    if call.data == 'python':
        bot.send_message(call.message.chat.id, "حسنًا، أرسل ملف حته تم تصليح خطاء Python (.py) .")
    
       
       
       

@bot.message_handler(content_types=['document'])
def handle_document(message):
    user_id = message.from_user.id
    file_path = f"temp/{user_id}_{message.document.file_name}"
    corrected_file_path = f"temp/{user_id}_{message.document.file_name.replace('.py', '').replace('.', 'HUSSElN.')}"

    try:
        if message.document.file_name.endswith('.py') or message.document.file_name.endswith('.php'):
            
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            with open(file_path, 'wb') as new_file:
                new_file.write(downloaded_file)

            
            
            for i in range(29, 0, -1):
                sleep(1)
  
  

            with open(file_path, 'r') as code_file:
                code_content = code_file.read()

            corrected_code = fix_code(code_content)

            if code_content == corrected_code:
                final_message = "✅ ملف ما بيه مشاكل "
            else:
                with open(corrected_file_path, 'w') as corrected_file:
                    corrected_file.write(corrected_code)
                corrected_file = open(corrected_file_path, 'rb')
                bot.send_document(message.chat.id, corrected_file, caption=f"تم تصحيح خطاء بل ملف : {message.document.file_name.replace('.py', '').replace('.', 'HUSSElN.')}")
                
                
                
                
        else:
            choose_file_type_message = "راسل ملف حته تم تصليح خطاء:\n\nPython "
            markup = telebot.types.InlineKeyboardMarkup()
            python_button = telebot.types.InlineKeyboardButton("Python ", callback_data='python')
            
            

            
            developer_button = telebot.types.InlineKeyboardButton("القناه", url="https://t.me/SX_9O")
            markup.add(developer_button)

            bot.send_message(message.chat.id, choose_file_type_message, reply_markup=markup)
    except Exception as e:
        error_message = f"صار خطاء بل بوت: {e}"
        bot.reply_to(message, error_message)
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
        if os.path.exists(HUSSElN_file_path):
            os.remove(HUSSElN_file_path)

if __name__ == '__main__':
    if not os.path.exists("temp"):
        os.makedirs("temp")

    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"An error occurred: {e}")
            sleep(5)