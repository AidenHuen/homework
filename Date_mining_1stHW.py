
f=open(r'e:\trainingset.txt')
list=f.readlines()
m=len(list)
x1=[]
x2=[]
y=[]
for i in range(m):
    list[i]=list[i].strip().split(",")
    x1.append(int(list[i][0]))
    x2.append(int(list[i][1]))
    y.append(int(list[i][2]))

theta0,theta1,theta2=500.24,22000.52,5000.55
sum1,sum2=float(sum(x1)),float(sum(x2))
max1,max2,min1,min2=max(x1),max(x2),min(x1),min(x2)
ex1,ex2=sum1/m,sum2/m
for i in range(m):
    x1[i]=((x1[i])-ex1)/(max1-min1)
    x2[i]=((x2[i])-ex2)/(max2-min2)

LR=float(raw_input("input your Learning Rate:"))
J=0.0
for i in range(m):
    J=J+((theta0+x1[i]*theta1+x2[i]*theta2)-y[i])**2
J=J/(2*m)
LX=2150000000
while(J>=LX):
    PastJ=J
    J=0.0
    suma,sumb,sumc=0.0,0.0,0.0
    for i in range(m):
        suma=suma+((theta0+x1[i]*theta1+x2[i]*theta2)-y[i])/m
        sumb=sumb+((theta0+x1[i]*theta1+x2[i]*theta2)-y[i])*x1[i]/m
        sumc=sumc+((theta0+x1[i]*theta1+x2[i]*theta2)-y[i])*x2[i]/m
    theta0=theta0-LR*suma
    theta1=theta1-LR*sumb
    theta2=theta2-LR*sumc
    for i in range(m):
        J=J+((theta0+x1[i]*theta1+x2[i]*theta2)-y[i])*((theta0+x1[i]*theta1+x2[i]*theta2)-y[i])
    J=J/(2*m)
    if(PastJ<J):LR=LR/2
    print 'Cost Function:'+str(J)
