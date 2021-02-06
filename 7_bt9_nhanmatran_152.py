m = int(input("Nhập m = "))
n = int(input("Nhập n = "))
k = int(input("Nhập k = "))

print("Nhập ma trận A ",m," dòng ",n," cột")
A = [[int(input()) for i in range(n)] for j in range(m)]
print("Nhập ma trận B ",n," dòng ",k," cột")
B = [[int(input()) for i in range(k)] for j in range(n)]
C = [[0 for i in range(k)] for j in range(m)]

for i in range(m):
    for j in range(k):
        for t in range(n):
            C[i][j] += A[i][t]*B[t][j]

print("Ma trận A là : ")
for x in A:
    print(x)
print("Ma trận B là : ")
for x in B:
    print(x)
print("Ma trận C là : ")
for x in C:
    print(x)
