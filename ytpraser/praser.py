from email import header
import bs4
import json
import requests



sou = bs4.BeautifulSoup


f = open('versions.json')
versions = json.load(f)
base_url = "https://www.apkmirror.com/apk/"
yt = str(versions["appversions"][0]["youtube"])
reddit = versions["appversions"][0]["reddit"]
twitter = versions["appversions"][0]["twitter"]






def extractyt ():
    url = str(base_url +"google-inc/youtube/youtube-"+ yt + "-release/youtube-" + yt + "-2-android-apk-download/"+ "?key=17ba053d301ba020d1d55b01f02ae98d2c493ff1&forcebaseapk=true")
    
    print(url)
    
extractyt()
