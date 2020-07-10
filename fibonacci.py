n=int(input("enter number of elements for fibbonaci:"))
a=0
b=0
c=1
for i in range(0,n):
    print (a)
    a=b+c
    c=b
    b=a
