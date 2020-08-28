from decorator import decorator
from datetime import datetime
import wrapt
# a= [0,1,2,3,4,5,6,7,8,9]
# for index,value in enumerate(a):
#     a[index]+=1
# print(a)
#
# b = map(lambda x:x+1,a)
# print(b)
# for i in b:
#     print(i)
#
#
# c = [i+1 for i in range(10)]
# print('type:',type(c))
# print(c)
#
# d= (i+1 for i in range(10))
# print('type:',type(d))
# for i in d:
#     print(i)

def create_gen(n):
    print('%s 开始' %n)
    while True:
        yield n
        print('增加',n)
        n+=1
gen = create_gen(6)
print(gen)
print(next(gen))
print(next(gen))
print(next(gen))

from collections import Iterable
from collections import Iterator
print('集合是否是可迭代对象:',isinstance([],Iterable))
print('集合是否是迭代器:',isinstance([],Iterator))
print('集合转换为迭代器:',isinstance(iter([]),Iterator))
print('生成器是否是可迭代对象:',isinstance((i*i for i in range(10)),Iterable))
print('生成器是否是迭代器:',isinstance((i*i for i in range(10)),Iterator))

def a():
    print('aaa')
    p1 = yield '123'
    print('bbb')
    if (p1 == 'hello'):
        print('p1是send传过来的')
    p2= yield '234'
    print(p2)

r = a()
next(r)
r.send('hello')

def outfun(a,b):
    def innner():
        c = a+b
        print(c)
    return innner

show = outfun(a=10,b=23)
show()



def use_logging(func):
    def mydo():
        print('%s is running' %func.__name__)
        return func()
    return  mydo

@use_logging
def bar():
    print('this is bar')

def logging(level):
    def mydo(func):
        def inner_mydo():
            print(level, func.__name__,': is running')
            return func()
        return inner_mydo
    return  mydo
@logging(level='debug')
def bar():
    print('this is bar')
bar()

@decorator
def logging_(func,*args,**kwargs):
    print('【debug】{}:调用{} 函数'.format(datetime.now(),func.__name__))
    return func(*args,**kwargs)

@logging_
def bar_():
    print('this is bar_')
bar_()

@wrapt.decorator
def wrapt_logging(wrapped, instance, args, kwargs):
    print('【debug-------】{}:调用{} 函数'.format(datetime.now(), wrapped.__name__))
    return wrapped(*args, **kwargs)
@wrapt_logging
def my_bar():
    pass
my_bar()



@property
def x(fget='aaa', fset='bbbb', fdel='cccc'):
    print('1111')

@classmethod
@staticmethod
def y():
    pass

def html_tag(tag_name):
    print('outer function begin')
    def wapper(func):

        print('wapper function begin')
        def inner_wapper(*args, **kwargs):
            print('inner function begin')
            content = func(*args, **kwargs)
            print('--------',content)
            print ("<{tag}>{content}</{tag}>".format(tag=tag_name, content=content))
            print('inner function end')
        return inner_wapper
    print ('end of outer function')
    return wapper

@html_tag(tag_name='p')
def hello(name='石一'):
    return 'hello,{}!'.format(name)
hello()


