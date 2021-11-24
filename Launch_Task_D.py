import Task_D

if __name__ == '__main__':
	d = []
	d.append(['ABCDEA','EAABCD',2])
	d.append(['MARS1234MARS','ASDGRV12MARSS1234VRCMARS',4])
	d.append(['ABC123123ABC','ABC123123',3])
	d.append(['MARS1234MARS','ASDGRV12MARSS1234VRCMARS',4])
	d.append(['MARSS123','MARSS123', 8])
	d.append(['ABCDAA','EAABCDAB',2])
	for i in range(len(d)):
		print(d[i], Task_D.calc(d[i]))