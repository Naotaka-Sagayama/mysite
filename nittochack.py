import os

path = './user.txt'
f = open(path, 'w')


import requests
from bs4 import BeautifulSoup

#keyword = 'Pythonスクレイピング'
# url = "https://www.amazon.co.jp/s?k=" + keyword + "&__mk_ja_JP=カタカナ&ref=nb_sb_noss_2"

keywords=["C613","C9786","C612","C9792"]
keywords2=[['S2243','S2244','S2245','S2246','S2247','S2248','S2249','S2250','S2251','S2252'],['S9776','S9777','S9778','S9779','S9780','S9781','S9782','S9783','S9784','S9785']]
m=0
n=0

while n <= 1:
    while m < len(keywords2[n]):
        url = "https://ntec.nito.co.jp/content/ppreview.html?code=C683-C611-"+keywords[n]+"-"+keywords2[n][m]

        response = requests.get(url)
        html =response.text

    #htmlパーサー
        soup = BeautifulSoup(html,'html.parser')

    #soup

        hinmeis = soup.select('.hinmei')
    #hinmeis
        prices = soup.select('.td_r')
    #prices

    #hinmei_list = []

    #for hinmei in hinmeis:
    #    hinmei_list.append(hinmei.txt)

    #print(hinmeis)

        hinmei_list = []
        price_list = []
        i=0
        j=7

    #for price in prices:
    #    if i==7:
    #        price_list.append(price.text)
    #        i=-1
    #        print(price.text)

    #    i=i+1

        for hinmei in hinmeis:
            #hinmei_list.append(hinmei.text)
            #print(hinmei.text)
            for price in prices:
                if i == j:
                    #price_list.append(price.text)
                    #print(hinmei.text,  price.text)
                    f.write(hinmei.text+" "+price.text+"\n")  # 何も書き込まなくてファイルは作成されました
                i = i + 1
            j = j + 8
            i = 0
                    #print(price_list)
                    #print(hinmei_list)
        m = m + 1
    n = n + 1
    m = 0

f.close()
