m,n=input().split()
m,n=int(m),int(n)
for i in range(m+1,n):
	c=0
	for j in range(1,i+1):
		if(i%j==0):
			c+=1
		else:
			if(c==2):
				print(i,end=' ')
