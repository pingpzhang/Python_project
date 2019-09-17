#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    str1 = raw_input('input_string1:\n')
    str2 = raw_input('input_string2:\n')
    str3 = raw_input('input_string3:\n')
    print 'before stored'
    print str1,str2,str3

    if str1 > str2: str1,str2 = str2,str1
    if str2 > str3: str2,str3 = str3,str2
    if str1 > str3: str1,str3 = str3,str1

    print 'after being srored'
    print str1,str2,str3