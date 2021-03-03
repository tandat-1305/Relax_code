def ucln(a, b):
    if (b == 0):
        return a;
    return ucln(b, a % b);
 
def bcnn(a, b):
    return int((a * b) / ucln(a, b));
 
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
#tính USCLN của a và b
print("Ước số chung lớn nhất của", a, "và", b, "là:", ucln(a, b));
#tính BSCNN của a và b
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bcnn(a, b));
