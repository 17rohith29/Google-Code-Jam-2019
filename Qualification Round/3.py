import math

def fix(tmp, lst, s, e):
	
	if s > e:
		return
	if s == e and tmp[s] != None:
		return
	else:
		#from last
		
		if e + 1 < len(tmp):
			posDEL = e
			valE = tmp[e + 1]
			valD = lst[posDEL]//valE
			tmp[e] = valD
			e = e - 1
		
		fix(tmp, lst, s, e)
	return 

def removeNone(tmp, lst):
	s = 0
	e = 0
	while s < len(tmp):
	
		if tmp[s] != None:
			
			s +=1 
			e += 1
		else:
			while e < len(tmp):
				if e + 1 < len(tmp) and tmp[e + 1] == None:
					e += 1
				else:
					break

			fix(tmp, lst, s, e)
			
			s = e + 1
			e = e + 1
	return

def getAllValues(lst):
	tmp = []
	for i in range(len(lst) - 1): # from 0 to len(lst) - 2
		cur, nxt = lst[i], lst[i + 1]
		currentValue = math.gcd(cur, nxt)
		if cur == nxt:
			if len(tmp) > 0 and tmp[len(tmp) - 1] is not None:
				currentValue = cur // tmp[len(tmp) - 1]
			else:
				currentValue = None
		# storing
		tmp.append(currentValue)
	removeNone(tmp, lst)
	# getting first element
	first, last = lst[0]//tmp[0], lst[len(lst) - 1]//tmp[len(tmp) - 1]
	# inserting
	tmp.insert(0, first)
	tmp.append(last)
	return tmp

def getPair(tmp): # gets map from no to char
	lst = list(set(tmp))
	lst.sort()
	a = dict()
	cur = "A"
	for i in lst:
		a[i] = cur
		cur = chr(ord(cur) + 1)

	return a


def solve(lst): 
	tmp = getAllValues(lst)
	b = getPair(tmp)

	ans =""
	for i in tmp:
		ans += b[i]

	return ans

for i in range(int(input())):
    n, l = list(map(int, input().split(' ')))
    x = list(map(int, input().split(' ')))
    ans = solve(x)
    print("Case #{}: {}".format(i + 1, ans))