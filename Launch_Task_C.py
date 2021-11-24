import Task_C

if __name__ == '__main__':
	d = []
	d.append(['1', 'a 2 2 + *', '2', ['2', '3']])
	d.append(['2', 'a b < 5 14 ?', '2', ['10 5', '5 10']])
	d.append(['2', 'c c > -5 14 ? f +', '2', ['-10 5', '10 5']])
	d.append(['2', 'c 12 -125 f 456 ? + = -5 14 ? f +', '2', ['-10 5', '1000000000 5', ]])
	d.append(['1', 'a b + ! +', '1', ['22', '3']])
	for i in range(len(d)):
		for value_set in d[i][3]:
			print(value_set)
			print(d[i], Task_C.calc([d[i][0], d[i][1], d[i][2], value_set]))