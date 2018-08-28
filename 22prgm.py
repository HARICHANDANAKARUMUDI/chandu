s,p=map(int,input().split())
count1=0
for j in range(s,p):
	le=len(str(i))
	sum2=0
	temp=j
	while j>0:
		y=j%10
		sum2=sum2+(y**le)
		j=j//10
	if(sum2==temp):
		if(count1==0):
			print(temp,end="")
		else:
			print("",end=" ")
			print(temp,end="")
		count1=count1+1
