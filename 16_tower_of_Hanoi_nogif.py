def tower(n, start, end, middle):
	if n==1:
		print("Move %i from tower %s to tower %s" %(n,start,end))
	else:
		tower(n-1, start, middle, end)
		print("Move %i from tower %s to tower %s" %(n,start,end))
		tower(n-1, middle, end, start)

tower(4, "A", "B", "C")	