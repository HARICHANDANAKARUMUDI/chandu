def median(s,m):
	s.sort()
	if m%2==0:
		return s[m/2]
	else:
		return (s[m/2-1]+s[m/2])/2
n=int(raw_input())
s=[int(x) for x in raw_input().split()]
print(median(s,m-1))
