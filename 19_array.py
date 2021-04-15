		
def mean(list_of_nums):
	giatri_dau = 0
	for num in list_of_nums:
		giatri_dau = giatri_dau + num
	return giatri_dau / len(list_of_nums)

def mode(list_of_nums):
	giatri_max = (0,0)
	for num in list_of_nums:
		bienthe  = list_of_nums.count(num)
		if bienthe > giatri_max[0]:
			giatri_max = (bienthe, num)
	return giatri_max[1]

def median(list_of_nums):
	list_of_nums.sort()
	if len(list_of_nums) % 2 != 0:
		giatri_giua = int((len(list_of_nums) - 1) /2)
		return list_of_nums[giatri_giua]
	elif len(list_of_nums) % 2 ==0:
		giatri_giua_1 = int(len(list_of_nums) /2)
		giatri_giua_2 = int(len(list_of_nums) /2) -1
		return mean([list_of_nums[giatri_giua_1], list_of_nums[giatri_giua_2]])


print(mean([13,13,13,13,14,14,16,18]))
print(median([13,13,13,13,14,14,16,18]))
print(mode([13,13,13,13,14,14,16,18]))
