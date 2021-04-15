import math
# mang = []
# a = int(input("Số phần tử : "))
# for x in range(a):
# 	k = input("Nhập phần tử : \n")
# 	mang.append(k)
# print(mang)

# Giá trị trung bình
def mean(list_of_nums):
	giatri_dau = 0
	for num in list_of_nums:
		giatri_dau = giatri_dau + num
	return giatri_dau / len(list_of_nums)

# Giá trị chung nhất
def mode(list_of_nums):
	giatri_max = (0,0)
	for num in list_of_nums:
		so_bien  = list_of_nums.count(num)
		if so_bien > giatri_max[0]:
			giatri_max = (so_bien, num)
	return giatri_max[1]

# Phuơng sai 
def variance(list_of_nums):
    n = len(list_of_nums)
    #Trung bình
    mean = sum(list_of_nums) / n
    deviations = [(x - mean) ** 2 for x in list_of_nums]
    variance = sum(deviations) / n
    return variance	

#Độ lệch chuẩn
def standard_deviation(variance):
	result = math.sqrt(variance)
	return result
# print(mean(mang))
# print(mode(mang))

print(mean([13,13,15,13,14,14,16,15]))
print(mode([13,13,15,13,14,14,16,15]))
var = variance([13,13,15,13,14,14,16,15])
print(var)
print(standard_deviation(var))


