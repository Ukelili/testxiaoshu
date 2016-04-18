#!/usr/bin/env python
# -*- coding: gb2312 -*-
import os
import urllib
from PIL import Image
from pytesser import *
from pytesseract import *


# ��������ͼƬ
for i in range(1):
    url = 'http://test.xiaoshushidai.com/verify.php' # ��֤��ĵ�ַ
    print "download", i
    file("./pic/%04d.gif" % i, "wb").write(urllib.urlopen(url).read())
'''����һ��'''
# ͼ���ֵ����
dir="./pic/"
path = "./font/"
for f in os.listdir(dir):
    if f.endswith(".gif"):
        img = Image.open(dir+f) # ����ͼƬ
        img = img.convert("RGBA")
        pixdata = img.load()
        # ��ֵ��
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


# ͼ��ָ�
j = 0
dir="./font/"
for f in os.listdir(dir):
    if f.endswith(".gif"):
        img = Image.open(dir+f)
        for i in range(4):
            x = 4 + i*10   # ��������ֲ�����Ҫ�Լ�
            y = 6           # ������֤��ͼƬ�����ؽ���
            img.crop((x, y, x+13, y+17)).save("fonts/%d.gif" % j)   # �ʵ����޸�
            print "j=",j
            j += 1
# ͼ��Ķ�ֵ������
def binary(f):
    print f
    img = Image.open(f)
    # img = img.convert('1')
    img = img.convert("RGBA")  # �ο��������޸��У��޸��У�������ᱨ��
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

# ͼ��ķָ������֤�밴�ַ��ָ����
def division(img):
    global nume
    font=[]
    for i in range(4):
        x=4+i*10		# �ú����е�����ֵ����Ҫ�Լ�����΢��
        y=5
        temp = img.crop((x,y,x+13,y+17))
        temp.save("./temp/%d.gif" % nume)
        nume=nume+1
        font.append(temp)
    return font
# �ָ��������ַ���Ԥ�ȶ����������еĽ��������ؽ��жԱ��ҳ������С����
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
            print "diffs��" + str(diffs)
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
            images = Image.open("./result/0000.gif")
            text = image_to_string(images)
            print "text:" + text



             #���¶���Ϊ�Լ��޸ģ��ο������е�ֵ�Աȴ�������
                    #print "mod[1].getpixel((xi, yi)):"+str(mod[1].getpixel((xi, yi)))
                    #print "target.getpixel((xi, yi)):"+str(target.getpixel((xi, yi)))