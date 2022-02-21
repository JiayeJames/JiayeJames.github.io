import requests
from lxml import etree
import json
import time
import random

class Netease_spider:
    # 初始化数据
    def __init__(self):
        self.originURL = 'https://music.163.com/#/discover/playlist'
        self.data = list()

    # 获取网页源代码
    def get_page(self,url):
        headers = {
            'USER-AGENT':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        response = requests.get(url=url,headers=headers)
        html = response.text
        return html

    # 解析网页源代码，获取数据
    def parse4data(self,html):
        html_elem = etree.HTML(html)
        play_num = html_elem.xpath('//ul[@id="m-pl-container"]/li/div/div/span[@class="nb"]/text()')
        song_title = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[1]/a/@title')
        song_href = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[1]/a/@href')
        song_link = ['https://music.163.com/#'+item for item in song_href]
        user_title = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[2]/a/@title')
        user_href = html_elem.xpath('//ul[@id="m-pl-container"]/li/p[2]/a/@href')
        user_link = ['https://music.163.com/#'+item for item in user_href]
        data = list(map(lambda a,b,c,d,e:{'播放量':a,'歌单名称':b,'歌单链接':c,'用户名称':d,'用户链接':e},play_num,song_title,song_link,user_title,user_link))
        return data

    # 解析网页源代码，获取下一页链接
    def parse4link(self,html):
        html_elem = etree.HTML(html)
        href = html_elem.xpath('//div[@id="m-pl-pager"]/div[@class="u-page"]/a[@class="zbtn znxt"]/@href')
        if not href:
            return None
        else:
            return 'https://music.163.com/#' + href[0]

    # 开始爬取网页
    def crawl(self):
        # 爬取数据
        print('爬取数据')
        html = self.get_page(self.originURL)
        data = self.parse4data(html)
        self.data.extend(data)
        link = self.parse4link(html)
        while(link):
            html = self.get_page(link)
            data = self.parse4data(html)
            self.data.extend(data)
            link = self.parse4link(html)
            time.sleep(random.random())
        # 处理数据，按播放量进行排序
        print('处理数据')
        data_after_sort = sorted(self.data,key=lambda item:int(item['播放量'].replace('万','0000')),reverse=True)
        # 写入文件
        print('写入文件')
        with open('netease.json','w',encoding='utf-8') as f:
            for item in data_after_sort:
                json.dump(item,f,ensure_ascii=False)

if __name__ == '__main__':
    spider = Netease_spider()
    spider.crawl()
    print('Finished')