print("tra cuu so bao danh ")
n = int(input("nhap so hoc sinh : "))
print("nhap SBD,Ten,Diem thi : ")
dict = {}


for x in range(n):
    sbd = int(input("SBD : "))
    ten = input("Ten : ")
    diemthi = int(input("Diem thi : "))
    dict[sbd] = [ten,diemthi]

sbd = int(input("Nhap so bao danh can tra cuu: "  ))
print(dict.get(sbd,"Khong co sbd")) 