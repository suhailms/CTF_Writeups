# WEB


## Script_Reward

Every thousandth visitor gets a prize!! Can u grab the prize??

URL :http://ctf.infosecians.tech:81/about.php


```
from bs4 import BeautifulSoup
import urllib.request

url = "http://ctf.infosecians.tech:81/about.php"

while 1:
    send_url = url
    req = urllib.request.Request(send_url)
    response = urllib.request.urlopen(req)
    page = response.read()
    soup = BeautifulSoup(page,features="html.parser")

    out = str(soup.findAll('p')[2]).split()[3].split("th")[0]
    
    print(out)
    
    if int(out)%1000 == 0:
        
        print(page)
        break

```
py
python script: [reward.py](data/reward.py) credit- sigkill

---------


