
def calc_dist(d, x0, y0, x1, y1):
	if d.x < x0:
		rx = x0 - d.x
	elif d.x > x1 - 1:
		rx = d.x - (x1 - 1)
	else:
		rx = 0
	if d.y < y0:
		ry = y0 - d.y
	elif d.y > y1 - 1:
		ry = d.y - (y1 - 1)
	else:
		ry = 0
	return(rx + ry)

class Driver:
	def __init__(self, x, y, x0, y0, x1, y1):
		self.x = x
		self.y = y
		self.d = calc_dist(self, x0, y0, x1, y1)

def calc(d):
	NM = d[0].split(' ')
	X0Y0X1Y1 = d[1].split(' ')
	KD = d[2].split(' ')
	DP = d[3].split(' ')
	
	N = int(NM[0])
	M = int(NM[1])
	
	X0 = int(X0Y0X1Y1[0])
	Y0 = int(X0Y0X1Y1[1])
	X1 = int(X0Y0X1Y1[2])
	Y1 = int(X0Y0X1Y1[3])
	
	K = int(KD[0])
	D = int(KD[1])
	
	if False:
		if X1 - N > 1:
			return(-1)
		if Y1 - M > 1:
			return(-1)
		if X1 - X0 < 1:
			return(-1)
		if Y1 - Y0 < 1:
			return(-1)
	
	i = 0
	j = 0
	dist = []
	while i < (D * 2):
		Dr = Driver(int(DP[i]), int(DP[i + 1]), X0, Y0, X1, Y1)
		dist.append(Dr.d)
		i += 2
		j += 1
	i = 0
	
	if len(dist) < K:
		return(-1)
	
	dist.sort()
	
	min_dist = dist[0]
	for i in range(K - 1):
		if dist[i + 1] > min_dist:
			min_dist = dist[i + 1]

	return(min_dist)

if __name__ == '__main__':
	NM = input()
	X0Y0X1Y1 = input()
	KD = input()
	DP = input()
	
	print(calc([NM, X0Y0X1Y1, KD, DP]))