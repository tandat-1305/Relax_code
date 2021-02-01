from random import randint


n = int(input(("Nhập số phần tử : ")))
A = [randint(0,1000000) for i in range(n)]
print(A," ")
list1 = [0 for i in range(1000001)]

for x in A:
    list1[x] +=1

print("Kết quả thống kê là : ")
for i in range(1000001):
    if list1[i] > 0:
        print("Phần tử ",i," xuất hiện ", list1[i]," lần")


