import Task_B

if __name__ == '__main__':
	r = []
	r.append([1,2,3,4])
	r.append([5,5,5,5])
	r.append([4,2,3,3])
	r.append([1,2,2,3,1,2,2])
	for i in range(len(r)):
		print(r[i], Task_B.calc(len(r[i]), r[i]))