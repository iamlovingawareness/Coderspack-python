def charcheck(a):
    b={}
    a.lower()
    for i in range(0,len(a)):
        c=a.count(a[i])
        b[a[i]]=c
        a.strip(a[i])
    print("the count for each character is :",b)

a=str(input("enter a string"))
charcheck(a)

