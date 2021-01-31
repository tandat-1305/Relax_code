l = [[1,2,3],[3,4,5],[5,6,7]]
for i in range(3):
	for j in range(3):
		print(l[i][j],end = " ")
	print()


d = int(input("nhap so dong: "))
c = int(input("nhap so cot: "))
A = []
for i in range(d):
	row = []
	for j in range(c):
		x = int(input("Nhập ptu : " ))
		row.append(x)
	A.append(row)
print("Ma tran vua nhap la: ")
for x in A:
	print(x)


m = int(input("Nhập số dòng: "))
n = int(input("Nhập số cột: "))
A = [[int(input("Nhap ptu ")) for j in range(n)] for i in range(m)]
print("Ma tran vua nhap" )
for x in A:
	print(x)