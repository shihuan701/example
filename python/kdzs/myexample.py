list1 = ['Lily','Mary','Jerry']
dic1 = {"name":"Tom","age":18}
print(list1)
print(*list1)
print(dic1)
print('my name is {name},my age is {age}'.format(**dic1))
name = 'waaaaaa'
age = 100
print(f'my name is {name},my age is {age}')
print(f"my name is {list1[1]},my age is {dic1['age']}")

print(f"lambda 表达式：{(lambda x:x+1)(2)}")
f = open('D:\workspace\\readme.txt','r',encoding='utf-8')
print(f.readlines())
f.close()

with open('D:\workspace\\readme.txt','r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break