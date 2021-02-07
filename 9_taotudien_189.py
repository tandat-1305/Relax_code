n = int(input("Nhap so phan tu :"))
print("Danh sach ",n," so khac nhau")
lst1 = [int(input()) for i in range(n)]
print("Danh sach ",n," ten ")
lst2 = [input() for i in range(n)]
dict = {}
for i in range(n):
    dict[lst1[i]] = lst2[i]
print("danh sach la:")
for x,y in dict.items():
    print(x,":",y)