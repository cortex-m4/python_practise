print("输入一个数，计算它的阶乘")
num=input()
_sum=1
#for x in list(range(int(num))):
#    _sum=_sum*(x+1)
x=1
while x<=int(num):
    _sum*=x
    x+=1

print(num,"的阶乘是",_sum)
print(list(range(int(num))))

#range(101)就可以生成0-100的整数序列
#list()函数可以转换为list