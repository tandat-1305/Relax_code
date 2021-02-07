n = int(input("Nhap so hoc sinh : "))
dict = {}

#có danh sách điểm từ 1->10,chọn range(11)
for i in range(11):
    dict[i] = []
print("Nhap ten va diem cua hoc sinh ")

for i in range(n):
    name = input("Nhap ten hoc sinh : ")
    mark = int(input("Nhap diem : "))
    dict[mark].append(name)

print("Danh sach da thong ke")

for i in range(11):
    print("hoc sinh co so diem ",i," la : ")
    print(dict[i])

