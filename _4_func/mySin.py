PI=3.1415956535897932
def factorial(x):
    sum=1
    for i in list(range(x)):
        sum*=(i+1)
    return sum

def my_sin(x):
    i=0
    ret=0
    while i<50:
        ret=ret+(pow(-1,i)*(pow(x,i*2+1)))/factorial(i*2+1)
        i+=1
    return ret

print("请选择输入角度的模式:\n1:Π分式\n2:度数")
mod=input()

print("请输入一个角度:")
ange=input()
if int(mod)==2:
    ret=my_sin((float(ange)/180)*PI)
    print("sin(",ange,")=",ret)
elif int(mod)==1:
    ret=my_sin(float(ange))
    print("sin(",ange,")=",ret)
else:
    print("非法输入")


print("请输入一个数用来计算阶乘:")
num=input()

print("!",num,"=",factorial(int(num)))


