# Original author: Unknown

import requests

headers = {
    'authority': 'domains.yougetsignal.com',
    'accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.yougetsignal.com',
    'referer': 'https://www.yougetsignal.com/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
    'x-prototype-version': '1.6.0',
    'x-requested-with': 'XMLHttpRequest',
}

response = requests.post('https://viewdns.info/reverseip/?host=49.40.9.180&t=1', headers=headers).text

print(response)
