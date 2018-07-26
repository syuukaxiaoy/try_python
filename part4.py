#part4 列表
#del 语句 删除列表的值
spam = ['cat','bat','rat','elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)

# allmycats.py
catsNames = []
while True:
    print('Enter the name of cat ' + str(len(catsNames) + 1) +
          ' (Or enter nothing to stop.): ')
    name = input()
    if name == '':
        break
    catsNames += [name]

print('The name of cats are :')
for name in catsNames:
    print(' ' + name)

#添加值 append() 和  insert()
#添加到末尾
spam = ['cat','dog','bat']
spam.append('moose')
print(spam)
spam.insert(1,'chicken')
print(spam)

# 删除值 remove()
spam = ['cat','bat','rat','elephant']
spam.remove('bat')
print(spam)

# 排序值 remove()
spam = ['cat','ants','Alice','Cats','badgers','elephants','bat','rat','elephant']
spam.sort()
print(spam)
spam.sort(reverse=True) # 逆序
print(spam)
spam.sort(key=str.lower) # 忽略大小写 按字母顺序排列
print(spam)

# 传递引用
def eggs(someParamater):
    someParamater.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)

# copt模块的 copy() 和 deepcopy()
#复制并指向独立列表
import copy
spam = ['A','B','C','D']
cheese = copy.copy(spam)
cheese[1] = '42'
print(spam)
print(cheese)
apple = ['a','b','c',spam]
bacon = copy.deepcopy(apple) # 复制内置列表
bacon[0] = 'oh'
print(apple)
print(bacon)