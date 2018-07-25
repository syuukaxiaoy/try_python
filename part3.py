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

# 异常处理 try 和 except
def spam(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#注意和上面的区别
def spam(divideBy):
    return 42/divideBy
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.')

# 游戏  猜数字~~~
#This is a guess the number game.
import random
secretNum = random.randint(1,20)
print('I am thinking of a number between 1 and 20.')

#Ask the player to guess 6 times.
for guesstakens in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')

    else:
        break # correct guess
if guess == secretNum:
    print('Good job! You guessed my number in ' + str(guesstakens) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNum))


# 考拉兹猜想--最简单的，不可能数学游戏
def collatz(number):
    if number == 1:
        return 1
    elif number % 2 == 0:
        print(number // 2)
        new = number // 2
        collatz(new) # 反复调用部分！！！
    else:
        print(3 * number + 1)
        new = 3 * number + 1
        collatz(new) # 反复调用部分！！！

try:
    print("Please type a number.")
    number = int(input())
    collatz(number)
except ValueError:
    print('Please input a integer number.')
    number = int(input())
    collatz(number)
