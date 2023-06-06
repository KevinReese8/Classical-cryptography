# -*- coding:utf-8 -*-
from easygui import *
global a,nt,n,n0
n0=list('abcdefghijklmnopqrstuvwxyz')
nt=[[list('bdfhjlcprtxvznyeiwgakmusqo'),'v'],            #默认三转子
    [list('ajdksiruxblhwtmcqgznpyfvoe'),'e'],
    [list('ekmflgdqvzntowyhxuspaibrcj'),'q']]
def engimaize(s):
    s0=''
    for i in range(len(s)):
        roll(1,0)
        tem=s[i]
        if tem==' ':
            s0+=tem
            continue
        for j in range(n):
            tem = nt[j][0][n0.index(tem)]
        tem = list('yruhqsldpxngokmiebfzcwvjat')[n0.index(tem)]
        for j in range(n - 1, -1, -1):
            tem = n0[nt[j][0].index(tem)]
        s0+=tem
    return s0
def roll(x, y):
    nt[y][0] = nt[y][0][x:] + nt[y][0][:x]
    if y + 1 < n and nt[y][1] in nt[y][0][:x]:
        roll(1,y+1)
def begin():
    for i in range(n-1):
        a[i+1]+=a[i]//26
        a[i]%=26
        roll(a[i], i)
    roll(a[n-1],n-1)
def reply(x):
    from random import choice
    replying=['总是输入不合法的话，你只会度过一个相对失败的人生',
              '能不能好好看看要求？你行不行呀细狗',
              '你的输入就像蔡徐坤打篮球',
              '输入不合法，就像玩游戏不玩原神',
              '很遗憾，你收到了南京大学退学通知书']
    if x==1:
        return replying[choice([0,0,0,0,0,0,0,1,1,1,1,1,1,2,3,4])]
    else:
        return '输入不合法，请重新输入'
def checkint(x,i):
    try:
        x = int(x)
    except:
        return False
    return  x>=i
def checkin(x,i):  #检查程序
    if not checkint(x,i):
        x=enterbox(reply(0))
        br(x)
        while not checkint(x,i) :
            x = enterbox(reply(1),image='你有毛病吧.jpeg')
            br(x)
    x=int(x)
    return x
def checkstr(x): #对密文的处理
    for i in range(len(x)):
        if ord('a')<=ord(x[i])<=ord('z') or x[i]==' ':
            continue
        else:
            return False
    return True
def checkz(s): #对新转子的检查
    for i in range(26):
        if s.count(chr(i+ord('a')))!=1:
            return False
    return len(s)==26
def br(x):
    if x==None:
        exit()
def kaisa(s, b):
    s0=''
    for i in range(len(s)):
        if s[i]==' ':
            s0+=s[i]
            continue
        if ord(s[i])+b>ord('z'):
            s0 += chr(ord(s[i]) + b - 26)
        else:
            s0 += chr(ord(s[i]) + b)
    return s0
def taptap(s):
    d = {}
    d['a'] = '11'
    d['b'] = '12'
    d['c'] = '13'
    d['k'] = '13'
    d[' '] = ' '
    m = 3
    n = 1
    s0 = ''
    for i in range(3, 10):
        m += 1
        d[chr(i + ord('a'))] = str(n) + str(m)
        if m == 5:
            m = 0
            n += 1
    for i in range(11, 26):
        m += 1
        d[chr(i + ord('a'))] = str(n) + str(m)
        if m == 5:
            m = 0
            n += 1
    for i in range(len(s)):
        s0 += d.get(s[i])
    return s0
def distap(s):
    s=str(s).split()
    s0=''
    for i in range(len(s)):
        for j in range(0,len(s[i]),2):
            tem=int(s[i][j])*5+int(s[i][j+1])
            if tem<=15:
                if tem!=8:
                    s0+=chr(ord('a')+tem-6)
                else:
                    s0+='c/k'
            if tem>15:
                s0+=chr(ord('a')+tem-5)
        s0+=' '
    return s0
def ba(s):
    d = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
         13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
         18: 'S', 19: 'T', 20: "U", 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd',
         30: 'e', 31: 'f', 32: 'g', 33: 'h',
         34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
         46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y',
         51: 'z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+',
         63: '/'}
    s0 = ''
    ap = len(s) % 3
    for i in range(len(s) - ap):
        s0 += '0' * (10 - len(bin(ord(s[i]))))
        s0 += bin(ord(s[i]))[2:]
    x = ''
    for i in range(len(s0) - 5)[::6]:
        tem = int(s0[i:i + 6], 2)
        x += d[tem]
    s1 = s[-ap:]
    if ap == 1:
        s0 = '0' * (10 - len(bin(ord(s1))))
        s0 += bin(ord(s1))[2:] + '0' * 4
        x += d[int(s0[:6], 2)] + d[int(s0[6:], 2)]
        x += '=='
    if ap == 2:
        s2 = ''
        for i in range(2):
            s2 += '0' * (10 - len(bin(ord(s1[i]))))
            s2 += bin(ord(s1[i]))[2:]
        s2 += '00'
        x += d[int(s2[:6], 2)] + d[int(s2[6:12], 2)] + d[int(s2[12:], 2)]
        x += '='
    return x
def unba(s):
    d = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M',
         13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R',
         18: 'S', 19: 'T', 20: "U", 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z', 26: 'a', 27: 'b', 28: 'c', 29: 'd',
         30: 'e', 31: 'f', 32: 'g', 33: 'h',
         34: 'i', 35: 'j', 36: 'k', 37: 'l', 38: 'm', 39: 'n', 40: 'o', 41: 'p', 42: 'q', 43: 'r', 44: 's', 45: 't',
         46: 'u', 47: 'v', 48: 'w', 49: 'x', 50: 'y',
         51: 'z', 52: '0', 53: '1', 54: '2', 55: '3', 56: '4', 57: '5', 58: '6', 59: '7', 60: '8', 61: '9', 62: '+',
         63: '/'}
    s0 = ''
    s1 = ''
    d1 = dict(zip(d.values(), d.keys()))  # 字典的互换
    ap = 0
    for i in range(len(s)):
        if s[i] == '=':
            ap = len(s) - i
            break
        if d1.get(s[i])==None:
            enterbox(reply(1),image='你有毛病吧.jpeg')
            exit()
        tem = '0' * (8 - len(bin(d1.get(s[i]))))
        tem += bin(d1.get(s[i]))[2:]
        s0 += tem
    if ap == 1:
        s1 = s0[:-2]
    if ap == 2:
        s1 = s0[:-4]
    if ap==0:
        s1 = s0
    s2 = ''
    for i in range(len(s1))[::8]:
        s2 += chr(int(s1[i:i+8].strip(), 2))
    return s2


msg = "选择你的加密或解密类型"
title = "加密或解密"
choices = ["凯撒加密", "凯撒解密","敲击加密", "敲击解密",'base64加密','base64解密', "恩尼格码密码机(古典密码学巅峰之作)"]
type = choicebox(msg, title, choices)
br(type)
if type!='恩尼格码密码机(古典密码学巅峰之作)':
    ss= passwordbox("密文")
    br(ss)
if type == '凯撒加密':
    ss=ss.lower()
    b= enterbox("位数")
    b= checkin(b,1)
    b%=26
    textbox(kaisa(ss, b),title='outcome')
    exit()
if type == "凯撒解密":
    ss = ss.lower()
    tem=''
    for i in range(1, 26):
        tem+=kaisa(ss, i)+'\n'
    textbox(tem,title='outcome')
    exit()
if type == "敲击加密":
    ss = ss.lower()
    if checkstr(ss):
        textbox(taptap(ss),title='outcome')
    exit()
if type== "敲击解密" and ss.count('0')==0:
    ss = ss.lower()
    textbox(distap(ss),title='outcome')
    exit()
if type=='base64加密':
    textbox(ba(ss),title='outcome')
    exit()
if type=='base64解密':
    textbox(unba(ss),title='outcome')
    exit()
n=enterbox('请输入转子数(>0)')                             #转子
br(n)
n=checkin(n,1)
a=[]
t,t1='',''
b=enterbox("是否自定义转子，否则使用内置转子，输入Y或N")
br(b)
if b=='Y':
    nt=[]
    for i in range(n):
        tem=enterbox('请输入转子，请连续输入26个字母的任意排列，转子和转子之间用回车分隔\n').strip().lower()
        br(tem)
        while not checkz(tem):
            tem=enterbox(reply(1),image='你有毛病吧.jpeg').strip().lower()
            br(tem)
        t=tem
        tem=enterbox('输入转子进位符，单个字母\n').strip()
        br(tem)
        while not(len(tem)==1 and checkstr(tem)):
            tem=enterbox(reply(1),image='你有毛病吧.jpeg').strip()
            br(tem)
        t1=tem
        nt.append([list(t),t1])
tem=enterbox('请输入转子初位(>0且计算进位),\n中间用空格分隔').split()   #转子初始化
br(tem)
while len(tem)!=n:
    tem=(enterbox(reply(1),image='你有毛病吧.jpeg')).split()
    br(tem)
for i in range(n):
    a.append(checkin(tem[i],0))
begin()
m=enterbox('请输入接线板线条个数')
br(m) #插线板替换
m=checkin(m,0)
d={}
for i in range(m):
    tem = enterbox('输入字母，每个插线板之间用回车，插线板中的字母用空格隔开').strip().lower()
    br(tem)
    while len(tem) != 3 or tem[1] != ' ' or tem[0] in d.values() or tem[2] in d.values():
        tem = enterbox(reply(1),image='你有毛病吧.jpeg').strip().lower()
        br(tem)
    tem=tem.split()
    d[tem[0]]=tem[1]
    d[tem[1]]=tem[0]
s=passwordbox('请输入密文,全英文,可包含空格').strip()                                #密文的输入
br(s)
t=[0]*len(s)
for i in range(len(s)):
    if 'A'<=s[i]<='Z':
        t[i]=1
s=s.lower()
if not checkstr(s):
    s=enterbox(reply(0),image='你有毛病吧.jpeg')
    while not checkstr(s):
        s=enterbox(reply(1),image='你有毛病吧.jpeg')
ts=''
for i in range(len(s)):
    if s[i] in d.keys():
        ts+=d.get(s[i])
    else:
        ts+=s[i]
ts=engimaize(ts[:])
s1=''
for i in range(len(ts)):
    if ts[i] in d.keys():
        s1+=d.get(ts[i])
    else:
        s1+=ts[i]
ts=''
for i in range(len(s1)):
    if t[i]==1:
        ts+=s1[i].upper()
    else:
        ts+=s1[i]
textbox(ts,title='outcome')
exit()
