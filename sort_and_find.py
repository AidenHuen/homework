# MY_work
class SortAndSeek:
    def SelectionSort(self,list):
        m=len(list)
        for i in range(m):
            Min=i
            for j in range(i,m):
                if list[j]<list[Min]:
                    Min=j
            list[i],list[Min]=list[Min],list[i]
    def InsertionSort(self,list):
        newlist=[list[0]]
        m=len(list)
        for i in range(1,m):
            for j in range(0,i):
                if list[i]<newlist[j]:
                    newlist.insert(j,list[i])
                    break
                if j==i-1:
                    newlist.append(list[i])
        list[:]=newlist[:]
    def BubbleSort(self,list):
        m=len(list)-1
        for i in range(m,0,-1):
            for j in range(i):
                if list[j]>list[j+1]:
                    list[j],list[j+1]=list[j+1],list[j]
    def MergeSort(self,list):
        if len(list) <=1:
            return list
        num = len(list)/2
        left = self.MergeSort(list[:num])
        right = self.MergeSort(list[num:])
        return self.Merge(left,right)

    def Merge(self,left,right):
        r,l=0,0
        reslut=[]
        while l<len(left) and r<len(right):
            if left[l] < right[r]:
                reslut.append(left[l])
                l+=1
            else:
                reslut.append(right[r])
                r+=1
        reslut+= right[r:]
        reslut+= left[l:]
        return reslut
    def OrderFind(self,list,a):
        m=len(list)
        for i in range(m):
            if a==list[i]:
                return i
        return -1

    def TwoyuanFind(self,list,a):
        last=len(list)-1
        top=0
        if list[last]==a:return last
        while True:
            middle=(last+top)/2
            if list[middle]==a:return middle
            elif list[middle]>a:last=middle
            elif list[middle]<a:top=middle

n=input('The amount of the values in the list:')
list=[]
for i in range(n):
    a=input(str(i+1)+':')
    list.append(a)
list0,list1,list2=[],[],[]
list0[:]=list1[:]=list2[:]=list[:]
Sort=SortAndSeek()
print '__________MergeSort__________:'
print 'before sort:'+str(list)
print 'after sort:'+str(Sort.MergeSort(list))

print '__________SelectionSort__________:'
print 'before sort:'+str(list)
Sort.SelectionSort(list)
print 'after sort:'+str(list)

print '__________InsertionSort__________:'
print 'before sort:'+str(list0)
Sort.InsertionSort(list0)
print 'after sort:'+str(list0)

print '__________BubbleSort__________:'
print 'before sort:'+str(list1)
Sort.BubbleSort(list1)
print 'after sort:'+str(list1)
print '__________OrderFind__________:'
print list2
a=int(raw_input("input the value your want to find:"))
s=Sort.OrderFind(list2,a)
if s==-1:
    print 'Not Find.'
else:
    print 'The Position is '+str(s)
print '__________OrderFind__________:'
print list2
b=int(raw_input("input the value your want to find:"))
s=Sort.OrderFind(list2,b)
if s==-1:
    print 'Not Find.'
else:
    print 'The Position is '+str(s)
