m,n=map(int,input().split())
for val in range(m,n):
	temp=val
	sum=0
	while(temp>0):
		digit=temp%10
		sum=sum+digit**3
		temp=temp//10
	if(sum==val):
		print(val)
	
