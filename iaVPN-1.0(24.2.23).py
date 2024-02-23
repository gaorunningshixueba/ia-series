import lxml
import requests
from bs4 import BeautifulSoup
from lxml import etree
import os
import json
title("iaVPN")
 
#如果当前目录下不存在'vpn.txt'这个文件,则创建'vpn.txt'这个目录
if os.path.exists('vpn.txt'):
    os.mkdir('vpn.txt')
 
if __name__=='__main__':
    #github上一个免费vpn获取项目,可以根据日期自行设置url
    url='https://github.com/sharkDoor/vpn-free-nodes/blob/master/node-list/2023-04/19%E6%97%A512%E6%97%B600%E5%88%86.md'
    head={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
        'AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/112.0.0.0 Safari/537.36'
        }
    #发送请求获取页面内容
    response=requests.get(url=url,headers=head)
    response.encoding=response.apparent_encoding
    page_text=response.text
    #创建一个列表存储获取的vpn数据
    vpn_list=[]
 
    ##页面解析
    #创建etree对象
    tree=etree.HTML(page_text)
    #获取包含所有vpn的列表
    tbody_li=tree.xpath('//*[@id="readme"]/article/table/tbody/tr')
    #遍历并将vpn数据存入文件中
 
    with open('./vpn.txt','w') as f:
        for li in tbody_li:
                #对每个vpn的属性进行处理
            vpn=li.xpath('./td/text()')
            agreement=vpn[0]
            Region=vpn[1]
            ip=vpn[2]
            port=vpn[3]
            password=vpn[4]
            link=vpn[5]
            vpn_list.append(ip+':'+port)#存储vpn到列表中
            f.write(ip+':'+port+',')
        f.close()
        # #2.
        # #创建beautifulsoup对象
        # soup=BeautifulSoup(page_text,'lxml')
        # tbody_li=soup.select('#readme > article > table > tbody >tr ')
        # with open('./vpn.txt','w') as f:
        #     for li in tbody_li:
        #         #对每个vpn的属性进行处理
        #         agreement=li.select('td')[0].string
        #         Region=li.select('td')[1].string
        #         ip=li.select('td')[2].string
        #         port=li.select('td')[3].string
        #         password=li.select('td')[4].string
        #         link=li.select('td')[5].string
        #         f.write(ip+':'+port+',')
        # f.close()
