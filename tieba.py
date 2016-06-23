
#-*-coding:utf-8-*-
__author__='axe.xu xwx213960'
__date__ ='$2014-9-23 0:22:31$'
import urllib2
import re
import os
import time
import codecs
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

#UI
print '='*30+'贴吧爬虫V1.0'+'='*30+'\n'
print '版本:V1.0\n'
print '使用时请注意地址格式！'
print '例:http://tieba.baidu.com/p/2196794546\n'
print '='*50+'作者:Axeprpr'+'='*10
url = raw_input('请输入帖子地址:')+'?see_lz=1&pn='

#处理URL并爬去第一页，获得标题和page数
page1 = urllib2.urlopen(url+'1').read().decode('utf-8')
title = re.findall('<h1.*?>(.*?)</h1>',page1,re.S)[0]
page_count = re.findall('class="red">(\d+)</span>',page1,re.S)[0]
print '开始读取帖子:'
print '标题:\n',title
str(title)
print '页数:',page_count
pause= raw_input('输入任意值开始下载:')
if pause != None:
   print '开始下载...'
else:
    print '输入任意值开始下载:'

#保存文件函数,使用时间来给文件夹命名
folder_name=time.ctime().replace(':','').replace(' ','')
folder_path=os.path.join(os.path.abspath('.'),folder_name)
file_name=str(title)+'.txt'
os.mkdir(folder_path)
file_path=os.path.join(folder_path,file_name)
def save(data):    
    f=codecs.open(file_path,'a+','utf-8')
    f.write(data)
    f.close

#格式化函数，处理爬取的内容
def format(list):
    newlist=[]
    rule1=re.compile(r'<.*?>')
    rule2=re.compile(r'[\(.*\)\'.*\': {}"_"$/=?&0=9<>a-zA-Z]') 
    for i in range(len(list)):
        result = rule2.sub('',rule1.sub('',list[i]))
        newlist.append(result)
    return newlist

#从每一页中读取，并且写入文件
page_count= int(page_count)
for i in range(1,page_count+1):
    page =urllib2.urlopen(url+str(i)).read().decode('utf-8')
    contend =re.findall('id="post_content.*?>(.*?)</div>',page,re.S)
    #列表格式化后，转化为字符串
    contend = format(contend)
    data='\n'.join(contend)
    print '正在读取并存储第%d页,请稍候...'%(int(i))
    save(data)
print '下载完成!'+'文件被存储在:%s'%(file_path)
print '谢谢使用!'
