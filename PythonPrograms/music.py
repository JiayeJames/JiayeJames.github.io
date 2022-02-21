
import requests
import re
import time
 
 
songIDs=[] #存放歌曲的sid
songNames=[] #存放歌曲的名称
 
 
url="http://www.htqyy.com/top/hot" #歌曲列表的url
 
#获取音乐榜单的网页信息
html=requests.get(url)
 
strr=html.text
 
pat1=r'sid="(.*?)"' #用于解析sid的正则
pat2=r'title="(.*?)" sid' #用于解析歌曲名称的正则
 
idList=re.findall(pat1,strr) #从爬取到的网页内容中获取sid
titleList=re.findall(pat2,strr) #从爬取到的网页内容中获取歌曲名称
 
songIDs.extend(idList) #将sid追加到列表
songNames.extend(titleList) #将歌曲名称追加到列表
 
#开始下载音频文件
for i in range(0,len(songIDs)):
	songUrl="http://f2.htqyy.com/play8/"+songIDs[i]+"/mp3/6"
	songName=songNames[i]
 
	#请求文件地址,获取文件资源
	referer='http://www.htqyy.com/play/{}'.format(songIDs[i])
	headers={'Referer':referer,'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}
 
	data=requests.get(songUrl,params="",headers=headers)
 
	print("正在下载第",i+1,"首")
 
	#将文件保存到指定目录
	with open("C:\\music\\{}.mp3".format(songName),"wb") as f:
		f.write(data.content)
 
	time.sleep(0.5)
