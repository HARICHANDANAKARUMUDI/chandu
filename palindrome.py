pal=int(input(" "))
rev=0
temp=pal
while(pal>0):
	val=pal%10
	rev=rev*10+val
	pal=pal//10
if(temp==rev):
	print("yes")
else:
	print("no")
