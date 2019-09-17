#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os

#str = raw_input("请输入raw_input：")
#print "你输入的内容是: ", str    #input和 raw_input函数基本类似，但是 input 可以接收一个Python表达式作为输入
#str = input("请输入input：")
#print "你输入的内容是: ", str
#请输入：[x for x in range(2,10,2)]
#你输入的内容是:  [2, 4, 6, 8]

currentdir = os.getcwd()
dir = currentdir + "\mydir"
files = dir + "\hello.txt"
dd = os.path.exists(dir)
print dir
print files
print dd
if dd == False:
    os.mkdir(dir)
os.remove(files)
fo = open(files,"w+")
fo.write("I MISS U")
fo.close()

try:
    fh = open("filename","w")
    fh.write("hello world!")
except IOError:    #如果发生异常
    print "ERROR：没有找到文件或者读取文件失败"
else:   #如果没有异常
    print "success：内容写入成功"
    fh.close()
try:
    os.rename("filename.txt","file.txt")
except OSError:
    print "文件不存在"
finally:
    print "执行完成"

try:
    fo = open("filename1.txt","w")
    fo.write("I MISS U")
except IOError:
    print "error:没找到文件或者没有写权限"
finally:
    print "关闭文件"
    fo.close()

#import second_file
#emp1 = second_file.Employee("Zara",2000)
#emp2 = second_file.Employee("ZhangSan",1500)
#emp1.age = 10
#print "emp1.age",getattr(emp1,'age')
#setattr(emp1,'age',12)
#print "emp1.age",getattr(emp1,'age')
#emp1.displauEmployee()
#emp2.displauEmployee()
#emp1.displayCount()
#print 'Employee.__doc__',second_file.Employee.__doc__
#print 'Employee.__doc__',second_file.Employee.__module__

import re

line = "Cats are smarter than dogs"

matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"

s = '421087199110154753'
res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<born_year>\d{4})',s)
print(res.groupdict())

print "Content-type:text/html"
print                               # 空行，告诉服务器结束头部
print '<html>'
print '<head>'
print '<meta charset="utf-8">'
print '<title>Hello World - 我的第一个 CGI 程序！</title>'
print '</head>'
print '<body>'
print '<h2>Hello World! 我是来自菜鸟教程的第一CGI程序</h2>'
print '</body>'
print '</html>'


