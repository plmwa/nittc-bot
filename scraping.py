import requests
from bs4 import BeautifulSoup
import json
import codecs
import tweet

def jsonnone():
    #jsonが空だった場合
    load_url = "https://www.toyota-ct.ac.jp/information/"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    widget=soup.find(class_="widget_list")
    values=[]
    values2=[]
    test={}
    test2={}
    name_list = ["key1","key2","key3","key4","key5","key6","key7","key8","key9","key10","key11","key12"]

    for element in widget.select('li > a'):
    
        values.append(element.text)
        values2.append(element.get('href'))
    #13回読み込み処理
    for i in range(12):
        #辞書型に変換
        key=name_list[i]
        test[key]=values[i]
        test2[key]=values2[i]
    #jsonファイルに辞書型を書き込み
    f=codecs.open('value.json','w','utf-8')
    json.dump(test,f,ensure_ascii=False,indent=4)
    f=open('value2.json','w')
    json.dump(test2,f,ensure_ascii=False,indent=4)
    
def jsonin():
    load_url = "https://www.toyota-ct.ac.jp/information/"
    html = requests.get(load_url)
    soup = BeautifulSoup(html.content, "html.parser")
    widget=soup.find(class_="widget_list")
    values=[]
    values2=[]
    test={}
    test2={}
    name_list = ["key1","key2","key3","key4","key5","key6","key7","key8","key9","key10","key11","key12"]
    #jsonにデータがある場合は比較させる
    #読み込み
    for element in widget.select('li > a'):
    
        values.append(element.text)
        values2.append(element.get('href'))
    
    #比較処理
    json_open=codecs.open('value.json','r','utf-8')
    json_data = json.load(json_open)
    if values[0]==json_data["key1"]:
        pass
    else:

        #13回読み込み処理
        for i in range(12):
            #辞書型に変換
            key=name_list[i]
            test[key]=values[i]
            test2[key]=values2[i]
        #jsonファイルに辞書型を書き込み
        f=codecs.open('value.json','w','utf-8')
        json.dump(test,f,ensure_ascii=False,indent=4)
        f=open('value2.json','w')
        json.dump(test2,f,ensure_ascii=False,indent=4)
        #ツイートさせる
        tweet.tweet(values[0],values2[0])
    

