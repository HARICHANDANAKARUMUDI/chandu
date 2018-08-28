lower,upper=map(int,input().split())
for i in range(lower,upper+1):
	count=0;a=0;b=0
	for j in range(1,i+1):
		if(i%j==0):
			count+=1
	if(count==2):
		if(b==0):
			print(i,end=" ")
		else:
			print("",end=" ")
			print(i,end="")
		a+=1
			
