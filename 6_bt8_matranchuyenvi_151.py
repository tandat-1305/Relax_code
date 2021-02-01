m = int(input("Nhap m = "))
n = int(input("Nhap n = "))
print("Nhap ma tran A ",m," dong ",n," cot")

A = [[int(input()) for i in range(n)] for j in range(m)]
AT=[]

for i in range(n):
	row=[]
	for j in range(m):
		row.append(0)
	AT.append(row)

for i in range(n):
	for j in range(m):
		AT[i][j] = A[j][i]
print("Ma tran A: ")

print("Ma trận đã nhập:")
for x in A:
	print(x)

print("Ma trận chuyển vị:")
for x in AT:
	print(x)