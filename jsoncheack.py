import json
import codecs
import scraping
def main():
    json_open=codecs.open('value.json','r','utf-8')

    json_data = json.load(json_open)
    if json_data["key1"]==None:
        
        scraping.jsonnone()
    else:
        #読み込みと書き込み
        scraping.jsonin()

