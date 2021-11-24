import re

def get_sec_rec(a,b,r):
	c = b.copy()
	for i in c:
		a[len(a)-len(b)]=i
		if len(b)>1:
			b.remove(i)	
			get_sec_rec(a,b,r)
			b.append(i)
		else:
			r.append(a.copy())

def get_sec(n):
	a = []
	b = []
	for i in range(n):
		a.append(0)
		b.append(i+1)
	r = []
	get_sec_rec(a,b,r)
	return(r)

def subs_present_in_key(subs, key):
	for i in range(len(subs)):
		if key.find(subs[i]) < 0:
			return(False)
	return(True)

def calc(d):
	ry = 'YES'
	rn = 'NO'
	promo = d[0]
	key = d[1]
	subs_l = d[2]
	
	promo_l = len(promo)
	key_l = len(key)
	
	if False:
		if subs_l <= 1:
			return(rn)
		if (promo_l < 6 or promo_l > 30):
			return(rn)
		if (key_l < 6 or key_l > 30):
			return(rn)
		if promo_l % subs_l > 0:
			return(rn)
		if subs_l >= key_l:
			return(rn)
		promo_check = re.search('[A-Z0-9]*', promo)
		if promo_check.group() != promo:
			return(rn)
		
	subs = []
	i = 0
	while i < promo_l:
		subs.append(promo[i:i + subs_l])
		i += subs_l
	#print(subs)
	
	if not subs_present_in_key(subs, key):
		return(rn)
		
	r = rn
	for a in get_sec(len(subs)):
		#print(a)
		k = [key]
		for i in a:
			s = subs[i-1]
			#print(k)
			#print(k.find(s), end=' ')
			for j in range(len(k)):
				p = k[j].find(s)
				if p > -1:
					tmp = k[j]
					k.pop(j)
					k.append(tmp[:p])
					k.append(tmp[p + subs_l:])
					break
			else:
				break
		else:
			r = ry
			break
	return(r)
	
if __name__ == '__main__':
	promo_l = int(input())
	promo = input()
	key_l = int(input())
	key = input()
	subs_l = int (input())
	print(calc([promo, key, subs_l]))