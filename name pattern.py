# str=input("enter the string")
# lenth=len(str)
# for i in range (lenth):
#     for j in range(i+1):
#         print(str[i],end=" ")
#     print()
# 
n=int(input("enter the rows"))
k=1
i=1
while i<=n:
    b=1
    while (b<=n-i):
        print(" ", end=" ")
        b=b+1
    j=1
    while j<=k:
        print((i),end=" ")
        j=j+1
    k=k+2
    print()
    i=i+1
i=1
while n>0:
    a=1
    while (a<i):
        a+=1
        print(" ", end=" ")
    j=1
    while (j<=(n*2)-1):
        print((i),end=" ")
        j=j+1
    print()
    n-=1
    i=i+1