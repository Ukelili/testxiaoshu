#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import urllib
from PIL import Image
from pytesser import *
from pytesseract import *


# 下载样本图片
for i in range(1):
    url = 'http://test.xiaoshushidai.com/verify.php' # 验证码的地址
    print "download", i
    file("./pic/%04d.gif" % i, "wb").write(urllib.urlopen(url).read())
'''方法一：'''
# 图像二值处理
dir="./pic/"
path = "./font/"
for f in os.listdir(dir):
    if f.endswith(".gif"):
        img = Image.open(dir+f) # 读入图片
        img = img.convert("RGBA")
        pixdata = img.load()
        # 二值化
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][0] < 90:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][1] < 136:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)
        img.save(path+f, "GIF")


# 图像分割
j = 0
dir="./font/"
for f in os.listdir(dir):
    if f.endswith(".gif"):
        img = Image.open(dir+f)
        for i in range(4):
            x = 16 + i*15   # 这里的数字参数需要自己
            y = 2           # 根据验证码图片的像素进行
            img.crop((x, y, x+7, y+10)).save("fonts/%d.gif" % j)   # 适当的修改
            print "j=",j
            j += 1
# 图像的二值化处理
def binary(f):
    print f
    img = Image.open(f)
    # img = img.convert('1')
    img = img.convert("RGBA")  # 参考文章中无该行，无该行，我这里会报错
    pixdata = img.load()
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    return img
nume = 0

# 图像的分割，就是验证码按字符分割出来
def division(img):
    global nume
    font=[]
    for i in range(4):
        x=16+i*15		# 该函数中的像素值都需要自己进行微调
        y=2
        temp = img.crop((x,y,x+7,y+10))
        temp.save("./temp/%d.gif" % nume)
        nume=nume+1
        font.append(temp)
    return font
# 分隔出来的字符与预先定义的字体库中的结果逐个像素进行对比找出差别最小的项
def recognize(img):
    fontMods = []
    for i in range(1):
        fontMods.append((str(i), Image.open("./fonts/%d.gif" % i)))
    result = ""
    font = division(img)
    for i in font:
        target=i
        points = []
        for mod in fontMods:
            diffs = 0
            for yi in range(10):
                for xi in range(7):
                    if 0 in target.getpixel((xi, yi)):
                        compare = 0
                    else:
                        compare = 255
                    if mod[1].getpixel((xi, yi)) != compare:
                        diffs += 1
            print "diffs：" + str(diffs)
            points.append((diffs, mod[0]))
        points.sort()
        result += points[0][1]
    return result
if __name__ == '__main__':
    codedir="./pic/"
    for imgfile in os.listdir(codedir):
        if imgfile.endswith(".gif"):
            dir="./result/"
            img=binary(codedir+imgfile)
            num=recognize(img)
            dir += (num+".gif")
            print "save to", dir
            img.save(dir)
            text = image_to_string(img.save(dir))
            print "text:"+text



             #以下多行为自己修改，参考文章中的值对比存在问题
                    #print "mod[1].getpixel((xi, yi)):"+str(mod[1].getpixel((xi, yi)))
                    #print "target.getpixel((xi, yi)):"+str(target.getpixel((xi, yi)))