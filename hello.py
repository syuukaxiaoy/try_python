# THis proggram says hello and asks for my name.
print('Hello world!')
print('What is your name?') # ask for their name
myName = input()
print('It is good to meet you,' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') # ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

# if
#1
if name =='Mary':
    print('Hello Mary')
if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password.')

#2
if name =='Alice':
    print('Hi, Alice')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')

# while
'''if vs while'''
#if
spam = 0
if spam < 5:
    print('Hello, world.')
    spam = spam + 1
#just print 'Hello, world.' once


#while
spam = 0
while spam < 5:
    print('Hello, world.')
    spam = spam + 1
#print 'Hello, world.' 5 times!!!

#yourName
name = ''
while name != 'your name':
    print('Please type your name.')
    name = input()
print('Thank you!')

#continue & break
#yourName2
while True: # 无限循环
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
'''只能在for 和 while 循环内部使用，否则报错哟'''

#for & range() 循环 迭代
#打印5次 Jimy
print('My name is ')
for i in range(5):
    print('Jimy 5 times (' + str(i) + ')')

# a same sample in while
print("My name is ")
i = 0
while i < 5:
    print('Jimy 5 times (' + str(i) + ')')
    i = i + 1

# 速算1~10000相加！
total = 0
for num in range(10001):
    total = total + num
print(total)

#range 开始，停止，步长
for i in range(1,5,2):
    print(i)

for a in range(5,-1,-1):
    print(a)

#导入模块
#import random, sys, os, math
#from random inport randint
import random
for i in range(5):
    print(random.randint(1,10))

# sys.exit() 提前结束程序
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')

