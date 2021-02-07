Dict = {1:"Toán",2:"Lý",3:"Hóa",4:1999}

print("\n Các khóa")
for x in Dict:
    print(x,end = ", ")

print("\n Các giá trị: ",)
for x in Dict.values():
    print(x,end = ", ")

print("\n Khóa và giá trị: ")
for x in Dict.items():
    print(x,end = ", ")

print("\n Số phần tử ",len(Dict))

#Trả giá trị của biến
print(Dict.get(2,"Không tồn tại"))
print(Dict.get(8,"Không tồn tại"))

Dict[4] = "Sinh"
print("\nDict đã thêm ",Dict)

Dict[2] = "Tin"
print("\nDict đã thay đổi",Dict)

Dict.pop(1)
print("\nDict đã xóa",Dict)

# Dict.popitem() "Xóa phần tử được đưa vào dict sau cùng."

del Dict[3]
print("\nDict sau khi xóa",Dict)

#Xóa cả từ điển 
Dict.clear()
print("\nXóa Dict",Dict)

