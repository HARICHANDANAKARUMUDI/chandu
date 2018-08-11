val1=input()
if val1>='a' and val1<='z' or val1>='A' and val1<='Z':
	if val1=='a' or val1=='e' or val1=='i' or val1=='o' or val1=='u' or val1=='A' or val1=='E' or val1=='I' or val1=='O' or val1=='U':
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid")
