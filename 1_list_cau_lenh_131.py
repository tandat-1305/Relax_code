list1 = [1,2,3,4,5,6]
list1.remove(1)				#xóa phần tử đầu
print(list1)


list1.pop()					#xóa phần tử cuối
print(list1)


list2 = [1,2,3,4,5,6,7,8,9]
del list2[1]				#xóa phần tử thứ 2
del list2[0:3]				#xóa phần tử đầu đến 2
list3 = [0,2,4,6,8]
del list3[0:2:4]			#del list[i,j,t] =>  xóa ptu có chỉ số i,i+t,i+2t,... (i+nt<j)
print(list3)


list4 = [1,2,3,4,5,6]		#chèn 3 vào vị trí thứ 2
list4.insert(1,3)
print(list4)


list5 = [4,2,6,1,7,6,2,1]
list5.sort()				#Sx tăng dần
print(list5)
list5.sort(reverse = True)	#Sx giàm dần
print(list5)


list6 = [1,3,2,4,6,5,7,2,4,1,8,9,6,4]
list7 = sorted(list6)
list8 = sorted(list6,reverse = True)
print(list7)
print(list8)


list9 = [1,2,3,4,5]			#Đảo ngc list
list10 = list9[::-1]
list9.reverse()
print(list9)
print(list10)



