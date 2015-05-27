#-*-encoding:utf-8-*-
import csv
import random
import math

def create_database(database0):#读入数据，进行归一化处理，生成适合的数据集。
    database=[]
    for line in database0:
        database.append(line)
    for i in range(1,len(database)):
        for j in range(5,12):
            if database[i][j]=='YES':database[i][j]=0.5
            if database[i][j]=='NO':database[i][j]=0.0
        if database[i][2]=='MALE':database[i][2]=0.5
        else:database[i][2]=0.0
        if database[i][3]=='INNER_CITY':database[i][3]=1.0
        elif database[i][3]=='TOWN':database[i][3]=2.0
        elif database[i][3]=='RURAL':database[i][3]=3.0
        else:database[i][3]=4.0
        database[i][1],database[i][4],database[i][6]=float(database[i][1]),float(database[i][4]),float(database[i][6])
    maxline,minline=database[1][:],database[1][:]
    for i in range(1,len(maxline)):
        for j in range(1,len(database)):
            if database[j][i]>maxline[i]:maxline[i]=database[j][i]
            if database[j][i]<minline[i]:minline[i]=database[j][i]
        for n in range(1,len(database)):
            database[n][i]=(database[n][i]-minline[i])/(maxline[i]-minline[i])
    return database

def distance(n,m,database):#计算欧式距离。
    dis=0
    for i in range(1,12):
        dis=dis+(database[n][i]-database[m][i])**2
        print math.sqrt(dis)
    return math.sqrt(dis)


#______________________________main__________________________________#
csvfile = file('F:\\bank-data.csv', 'rb')
database0 = csv.reader(csvfile)#读入EXCEL中数据
database=[]
database=create_database(database0)
r=1.8#阈值r
clusters=[[1]]
for i in range(2,len(database)):#通过对下标操作，进行一趟聚类，
    for j in range(len(clusters)):
        if(distance(i,clusters[j][0],database)<=r and j<len(clusters)):
            clusters[j].append(i)
            break
        elif(distance(i,clusters[j][0],database)>r and j<len(clusters)-1):
            continue
        elif(distance(i,clusters[j][0],database)>r and j==len(clusters)-1):
            clusters.append([int(i)])
            break
#____________________数据写入_________________________#
database=[]
csvfile = file('F:\\bank-data.csv', 'rb')
database1=csv.reader(csvfile)
for line in database1:
    database.append(line)
for i in range(len(clusters)):
    file=open('F:\\clusters\\'+'cluster'+str((i+1))+'.text','w')
    print 'cluster'+str((i))
    for j in range(len(clusters[i])):
        print database[clusters[i][j]]
        for n in database[clusters[i][j]]:
            file.write(str(n)+'     ')
        file.write('\n')

