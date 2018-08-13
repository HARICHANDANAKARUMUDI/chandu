val=int(input(" "))
count=0
for i in range(1,val+1):
	if((val%i)==0):
	         count+=1
if(count==2):
     print("yes")
else:
     print("no")
