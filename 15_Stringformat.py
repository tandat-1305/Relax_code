CURRENT_YEAR = 2021

print("Ten cua ban: ")
ten = input()

print("Ho cua ban: ")
ho = input()


print("ban sinh nam : ")
namsinh = int(input())
tuoi = CURRENT_YEAR - namsinh 
#print("tuoi cua ban la {0} nam {1}".format(tuoi,CURRENT_YEAR)

print("chieu cao (meter) : ")   
chieu_cao = float(input())

print("ho ten cua ban la " +ho +" " +ten)
print("tuoi cua ban la " + str(tuoi) +" nam" + str(CURRENT_YEAR))
print("ban cao " +str(chieu_cao) + " met")


