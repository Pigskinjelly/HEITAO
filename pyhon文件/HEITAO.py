# print：打印函数
# import math:引用math这个
# math.sqrt(s):是求X的方差的公式
# input:输入函数
# float:浮点型
# 输入一个数求它的平方根
"""
import math
s = float(input("请输入一个数："))
if(s>0):
    s = math.sqrt(s)
    print("平方根是:", s)
if(s<0):
        print("负数没有平方根")
print("the end")
#输入一个数求它的平方根
"""
"""
#求圆的表面积、圆球的体积、圆柱的体积。
import math #数学函数
r = float(input("请输入圆的半径："))#用来让用户从键盘上自己输入圆的半径和高
h = float(input("请输入圆柱的高："))
if r > 0:#用来判断的
    x = 4*math.pi*r*r#算圆的公式
    print("圆的表面积是：%.2f" % x)#%.2f用来保留小数点后两位的
    y = 4*math.pi*r*r*r/3
    print("圆球的体积是：%.2f" % y)
if h > 0:
    z = h*math.pi*r*r
    print("圆柱的体积是：%.2f" % z)
if r < 0:#不满足条件的时候
    print("半径并不能为负数。")
if h < 0:
    print("高不能为负数。")
"""
# 判断一个数是偶数还是奇数
"""
n = input("请输入一个整数：")
n = int(n)
if n % 2 == 0:
    print("这是一个偶数")
else:
    print("这是一个奇数")
"""

# 99乘法表
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print(i, '*', j, '=', (i*j), end='  ')
    print("\n")
"""

# 输入一个实数，并输出该数的绝对值
"""
a = float(input("请输入一个数："))
if a >= 0:
    a = a
else:
    a = -a
print("绝对值是：%0.2f" % a)
"""
"""
import math
a = float(input("请输入a的值："))
b = float(input("请输入b的值："))
c = float(input("请输入c的值："))
if a != 0:
    delta = b**2-4*a*c
    if delta < 0:
        print("无根")
    elif delta == 0:
        s = -b/(2*a)
        print("唯一根x=",s)
    else :
        root = math.sqrt(delta)
        x1 = (-b+root)/(2*a)
        x2 = (-b-root)/(2*a)
        print("x1=",x1,"\t","x2=",x2)
"""
"""
p=int(input('p='))
q=int(input('q='))
n=int(input('请输入你要保留的小数位n='))
num1=0
num2=0
temp=0
num1 = p // q
while n:
    num2=p%q
    num2*=10
    num2=num2//q
    temp=temp*10+num2
    n-=1
print(str(num1)+'.'+str(temp))
"""
"""
n=int(input("n="))
m=int(input("m="))
if n<m:
    b=m
else:
    b=n
while b>=1:
    if n%b==0 and m%b==0:
        break
    b=b-1
print(b)
"""
"""
while True:
    m=input("输入一个0到100的数:")
    m=float(m)
    if m>=0 and m<=100:
        break
print("mark",m)
"""
'''
a=int(input("a="))
b=int(input("b="))
if a>b:
    c=b
else:
    c=a
for c in range(1,c+1):
    if a%c==0 and b%c==0:
        d=c
print("最大公约数:",d)
'''
"""
for n in range(2,101):
    flag=1
    for m in range(2,n):
        if n%m==0:
            flag=0
            break
    if flag==1:
        print("%5d"%n,end="")
        count=count+1
        if count%5==0:
            print()
"""
"""
try:
    name=input("name=")
    if name.strip()=='':
        raise Exception("无效名字")
    Gender=="男" or Gender=="女"
    if
        raise Exception()
    Age=
    if :
        raise Exception()
except Exception as e:
    print(e)
"""
def even(num):
    if num % 2 == 0 and num >= 6:
        return num


def isprime(num):
    if num > 2:
        for x in range(2, num // 2 + 1):
            if num % x == 0:
                return False
        else:
            return True
    return False


def ge_de_ba_he(n):
    if even(n):
        print(f'{n} = ', end='')
        for p in range(1, n // 2 + 1):
            if isprime(p) and isprime(n - p):
                print(f"{p} + {n - p}")
                break
    else:
        print('您传入的不是素数')


ge_de_ba_he(14)
ge_de_ba_he(24)
ge_de_ba_he(32)
ge_de_ba_he(17)