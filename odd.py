m,n=input().split()
m,n=int(m),int(n)
count=0
for i in range(m+1,n):
	if(i%2!=0):
		if i<n-2:
			k=" "
		else:k=""
		print(i,end=k)
