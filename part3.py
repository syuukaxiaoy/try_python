#函数
#消除重复，更短，易读，易修改
# 3次调用
def hello():
    print('Howdy!')
    print('Howdy!!')
    print('Hello there.')

hello()
hello()
hello()

#def 语句和参数
def hello(name):
    print('Hello ' + name)

hello('Alice')
hello('Bob')

#返回值和return
#返回表达式或值
import random

def getAnswer(num):
    if num == 1:
        return 'It is certain.'
    elif num == 2:
        return 'It is decidedly so.'
    elif num == 3:
        return 'Yes'
    elif num == 4:
        return 'Oh my god!'
    elif num == 5:
        return 'ask again latter'

print(getAnswer(random.randint(1,5)))

#参数和print()
#打印不换行
print('apple',end='')
print ('pie')
#以！隔开
print('cat','dog','fish',sep='!')

#局部和全局
#局部不能在全局中使用
#局部不能用其他局部内的变量
#全局变量可在局部内读取
#名称相同的局部变量和全局变量
def spam():
    eggs = 'Spam local'
    print(eggs) # prints 'Spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'

