from random import randint


n = int(input("Số phần tử: "))
a=[]
for i in range(n):
    x=randint(0,1)
    a.append(x)
print("Các phần tử random là: ",a)


m=n=0
for x in a:
    if x == 0:
        n += 1
        m=max(m,n)
    else:
        n=0
print("Dãy 0 dài nhất là :" ,m)




