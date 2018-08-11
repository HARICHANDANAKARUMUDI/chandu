num1,num2,num3=raw_input().split()
num1,num2,num3=int(num1) , int(num2) , int(num3)
if(num1>num2) and (num1>num3):
	print(num1)
elif(num2>num3):
	print(num2)
else:
	print(num3)
