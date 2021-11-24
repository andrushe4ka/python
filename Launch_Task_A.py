import Task_A

if __name__ == '__main__':
	d = []
	d.append(['2 2', '1 1 2 2', '1 1', '0 0'])
	d.append(['2 1', '1 0 2 1', '1 1', '0 0'])
	for i in range(len(d)):
		print(d[i], Task_A.calc(d[i]))