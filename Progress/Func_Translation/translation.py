# [PAPAGO API로 텍스트 번역]

import urllib.request
import keys as my
import json
client_id = my.PAPAGO_ClientID()
client_secret = my.PAPAGO_ClientSecret()
encText = urllib.parse.quote("apple")
data = "source=en&target=ko&text=" + encText
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    response_data = json.loads(response_body.decode('utf-8'))
    translated_text = response_data['message']['result']['translatedText']
    print(translated_text)
else:
    print("Error Code:" + rescode)