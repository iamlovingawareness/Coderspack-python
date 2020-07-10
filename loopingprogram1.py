list1=[]
n=int(input("Enter the number of elemts for list 1:"))
l=n-1
for i in range(0,n):
    x=int(input("Enter element number :"))
    list1.append(x)
    
list2=[]
for i in range(0,n):
    if list1[i]>0:
        list2.append(list1[i])
    else:
        continue

print("The output is",list2)

