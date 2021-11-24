def find_next_min(start, r):
	n = 0
	for i in range(start, len(r)-1):
		if r[i] > r[i+1]:
			n += 1 
		elif r[i] <= r[i + 1]:
			return(n)
def calc(N,r):
	bonus_sum = 0
	
	for i in range(N):
		if i==0:
			w = 1
			#cur_bonus = 500
			w += find_next_min(i, r)
			cur_bonus = w * 500
		elif i==N-1:
			if r[i-1] < r[i]:
				cur_bonus = cur_bonus + 500
			elif r[i-1] >= r[i]:
				cur_bonus = 500
		else:
			if r[i-1] < r[i]:
				cur_bonus = cur_bonus + 500
				tmp_bonus = 500
				for j in range(i,N-1):
					if r[j]>r[j+1]:
						tmp_bonus = tmp_bonus + 500 
					elif r[j]<=r[j+1]:
						break
				if cur_bonus < tmp_bonus:
					cur_bonus = tmp_bonus
			elif r[i-1] > r[i]:
				cur_bonus = cur_bonus - 500
				tmp_bonus = 500
				for j in range(i,N-1):
					if r[j]>r[j+1]:
						tmp_bonus = tmp_bonus + 500 
					elif r[j]<=r[j+1]:
						break
				if cur_bonus > tmp_bonus:
					cur_bonus = tmp_bonus
			elif r[i-1]==r[i]:
				cur_bonus = 500
				for j in range(i,N-1):
					if r[j]>r[j+1]:
						cur_bonus = cur_bonus + 500 
					elif r[j]<=r[j+1]:
						break
		bonus_sum = bonus_sum + cur_bonus
		#print(str(cur_bonus) + ' ' + str(r[i]) + ' ' + str(bonus_sum))
	return(bonus_sum)

if __name__ == '__main__':
	#print('Enter drivers number')
	N=int(input())
	r=[]
	for i in range(N):
		#print('enter a rating of driver ' + str(i+1))
		r.append(int(input()))
	print(calc(N,r))