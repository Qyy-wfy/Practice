import time
import random
import json
import requests

p=1
for pn in range(1,11):
    base_url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E7%BE%8E%E5%A5%B3%E5%9B%BE&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E7%BE%8E%E5%A5%B3%E5%9B%BE&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&cg=girl&pn='+str(pn*30)+'&rn=30&gsm=5a&1596263600945='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
    }
    response = requests.get(base_url)
    res = response.content.decode('utf-8')
    dic = json.loads(res)

    for i in dic['data']:
        if 'middleURL' in i:
            # time.sleep(random.randint(1,3))
            print (i['middleURL'])

            imgdata = requests.get(i['middleURL'],headers=headers)
            print(imgdata.content)

            f = open('./surprise/'+str(p)+i['middleURL'][-4:],'wb')
            f.write(imgdata.content)
            f.close()
            p += 1

