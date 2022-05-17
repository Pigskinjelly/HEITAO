#布尔运算符
a,b=1,2
print('---------------and 并且----------------')
print(a==1 and b==2) #True    true and true--->true
print(a==1 and b<2) #False    true and false--->false
print(a!=1 and b==2) #False   false and true--->false
print(a!=1 and b!=2) #False   false and true--->false

print('---------------or 或者----------------')
print(a==1 or b==2) #True or True--->True
print(a==1 or b<2) #True or False--->True
print(a!=1 or b==2) #False or True--->True
print(a!=1 or b!=2) #False or False--->False

print('---------------not 对运算数取反----------------')
f=True
f2=False
print(not f)
print(not f2)

print('---------------in 与not in----------------')
s='helloworld'
print('w' in s)
print('k' in s)
print('w' not in s)
print('k' not in s)
