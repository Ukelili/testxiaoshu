#!/usr/bin/env python
#-*- encoding: utf-8 -*-
import sys
import httplib2
import HTMLParser
def getPageContent(url):
    '''''
    使用httplib2用编程的方式根据url获取网页内容
    将bytes形式的内容转换成utf-8的字符串
    '''
    #使用ie9的user-agent，如果不设置user-agent将会得到403禁止访问
    headers={'user-agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
            'cache-control':'no-cache'}
    if url:
         response,content = httplib2.Http().request(url,headers=headers)

         if response.status == 200 :
            return content

class stack:
    def __init__(self,size=100,list=None):
        self.contain=[]
        self.msize=size;
        self.top = 0;
    def getTop(self):
        if(self.top>0):
            return self.contain[self.top-1]
        else:
            return None
    def getLength(self):
        return len(self.contain);
    def push(self,data):
        if(self.top==self.msize):
            return -1
        self.contain.append(data)
        self.top=self.top +1
    def pop(self):
        try:
            res=self.contain.pop()
            if(self.top>0):
                self.top=self.top-1
            return res;
        except IndexError:
            return None


class ParserOschinaNew(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.st=stack(size=1000)
        self.st.push('over')

    def handle_starttag(self,tag,attrs):
        stack_size = self.st.getLength()
        if stack_size==1 and tag=='ul':
            for name,value in attrs:
                if (name=='class' and value=='BlogList'):
                    self.st.push('ul')
                    break;
        if (stack_size==2 and tag=='li' ):
            self.st.push('li')
        if (stack_size==3 and tag=='h3' ):
            self.st.push('h3')
            text = '博客标题：'.decode('utf-8').encode('gb2312','ignore')
            print '%s'%text
        if (stack_size==3 and tag=='p' ):
            self.st.push('p')
            text = '正文部分：'.decode('utf-8').encode('gb2312','ignore')
            print '%s'%text

        if (stack_size==3 and tag=='div' ):
            for name,value in attrs:
                if (name=='class' and value=='date'):
                    self.st.push('div')
                    text = '作者：'.decode('utf-8').encode('gb2312','ignore')
                    print '%s'%text


    def handle_data(self ,data):
        stack_size = self.st.getLength()
        if (stack_size==4):
            print data.decode('utf-8').encode('gb2312','ignore')

    def handle_endtag(self,tag):
        stack_size = self.st.getLength()
        stack_tag = self.st.getTop()
        if ('h3'==tag and 'h3'==stack_tag):
            self.st.pop()
        if ('p'==tag and 'p'==stack_tag):
            self.st.pop()
        if ('div'==tag and 'div'==stack_tag):
            self.st.pop()

        if ('li'==tag and 'li'==stack_tag):
            self.st.pop()
        if ('ul'==tag and 'ul'==stack_tag):
            self.st.pop()
            if('over'==self.st.getTop()):
                print "this is end!"



if __name__ == '__main__':
    pageC = getPageContent('http://www.oschina.net/blog/more?p=1')
 #   pageC = pageC.decode('utf-8').encode('gb2312','ignore')
    my = ParserOschinaNew()
    my.feed(pageC)

'''
# file: GetImage.py
import Tkinter
import urllib
import HTMLParser
# 第二个示例程序：找图片链接
class MyHTMLParser(HTMLParser.HTMLParser):                                              # 创建HTML解析类
        def __init__(self):
                HTMLParser.HTMLParser.__init__(self)
                self.gifs = []                                                          # 创建列表，保存gif
                self.jpgs = []                                                          # 创建列表，保存jpg
        def handle_starttag(self, tags, attrs):                                         # 处理起始标记
                if tags == 'img':                                                       # 处理图片
                        for attr in attrs:
                                for t in attr:
                                        if 'gif' in t:
                                                self.gifs.append(t)                     # 添加到gif列表
                                        elif 'jpg' in t:
                                                self.jpgs.append(t)                     # 添加到jpg列表
                                        else:
                                                pass
        def get_gifs(self):                                                             # 返回gif列表
                return self.gifs
        def get_jpgs(self):                                                             # 返回jpg列表
                return self.jpgs
class Window:
        def __init__(self, root):
                self.root = root                                                        # 创建组件
                self.label = Tkinter.Label(root, text = '输入URL:')
                self.label.place(x = 5, y = 15)
                self.entryUrl = Tkinter.Entry(root,width = 30)
                self.entryUrl.place(x = 65, y = 15)
                self.get = Tkinter.Button(root,
                                text = '获取图片', command = self.Get)
                self.get.place(x = 280, y = 15)
                self.edit = Tkinter.Text(root,width = 470,height = 600)
                self.edit.place(y = 50)
        def Get(self):
                url = self.entryUrl.get()                                               # 获取URL
                page = urllib.urlopen(url)                                              # 打开URL
                data = page.read()                                                      # 读取URL内容
                parser = MyHTMLParser()                                                 # 生成实例对象
                parser.feed(data)                                                       # 处理HTML数据
                self.edit.insert(Tkinter.END, '====GIF====\n')                          # 输出数据
                gifs = parser.get_gifs()
                for gif in gifs:
                        self.edit.insert(Tkinter.END, gif + '\n')
                self.edit.insert(Tkinter.END, '===========\n')
                self.edit.insert(Tkinter.END, '====JPG====\n')
                jpgs = parser.get_jpgs()
                for jpg in jpgs:
                        self.edit.insert(Tkinter.END, jpg + '\n')
                self.edit.insert(Tkinter.END, '===========\n')
                page.close()
root = Tkinter.Tk()
window = Window(root)
root.minsize(600,480)
root.mainloop()
'''


'''
import HTMLParser

class MyParser(HTMLParser.HTMLParser):
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        # 这里重新定义了处理开始标签的函数
        if tag == 'a':
            # 判断标签<a>的属性
            for name,value in attrs:
                if name == 'href':
                    print value


if __name__ == '__main__':
    a = '<html><head><title>test</title><body><a href="http://test.xiaoshushidai.com">抢先贷</a></body></html>'

    my = MyParser()
    # 传入要分析的数据，是html的。
    my.feed(a)
'''
