import requests

url = "https://upos-sz-mirrorali02.bilivideo.com/upgcxcode/20/17/573651720/573651720-1-30080.m4s?e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=&uipk=5&nbs=1&deadline=1660817115&gen=playurlv2&os=ali02bv&oi=0&trid=ed0c18ce719f4ed0a586d175860d06b6u&mid=307109760&platform=pc&upsig=44f920f341adb1a418193e26674be972&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,mid,platform&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=328976&logo=80000000"

payload={}
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54',
  'Referer': 'https://www.bilibili.com/video/av255501837'
}

response = requests.request("GET", url, headers=headers, data=payload)

with open('a.mp4','wb') as f:
  f.write(response.content)
