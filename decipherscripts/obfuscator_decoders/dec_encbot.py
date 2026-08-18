#Decoded by @cr_dex
import webbrowser,time,base64,marshal,zlib,py_compile,os,sys
webbrowser.open('https://t.me/mt_4_4')

try:
    import requests
finally:
    pass
os.system('pip install telebot')
os.system('pip install Pytelegrambotapi==3.7.7')
os.system('pip install requests')
token = input('token ')
bot = telebot.TeleBot(token)

def start(message):
    bot.send_message(message.chat.id, '<strong>الان ارسل ملف بايثون ليتم التشفير  \nـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ\n• مميزات التشفير الذي تشفره\n• يتم الحمايه بأكثر من طبقه\nـ marshal,base46,zlib ـ\n ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ\nقناه  المبرمج : @cr_dex </strong>', 'html', **('parse_mode',))
    
    def send(message):
        bot.get_file(message.document.file_id)
        file_info = bot.get_file(message.document.file_id)
        use = bot.download_file(file_info.file_path)
        bot.send_message(message.chat.id, '<strong> ⏱️ Wait a little please …</strong>', 'html', **('parse_mode',))
        cv = str('# CODE BY : cr_dex › \n# Tele : @cr_dex')
        sa = compile(use, 'dg', 'exec')
        sb = marshal.dumps(sa)
        sc = zlib.compress(sb)
        sd = base64.b85encode(sc)
        b = '#https://t.me/cr_dex\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'
        d = open('enc_cr_dex.py', 'w')
        d.write(b + '\n' + cv)
        d.close()
        file = {
            'document': open('enc_cr_dex.py', 'rb') }
        tex = '✅ Done Encryption File 🥀.'
        requests.post(f'''https://api.telegram.org/bot{token}/sendDocument?chat_id={message.chat.id}&caption={tex}''', file, **('files',))

    send = bot.message_handler([
        'document'], **('content_types',))(send)

start = bot.message_handler([
    'greet',
    'start'], **('commands',))(start)
bot.polling(True)



