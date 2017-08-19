def ReplaceChar(string,replaceby):
	output=""
	replace=string[:1]
	string=string[1:]
	index=string.find(replace)
	output+=replace	
	while(index!=-1):			
		output+=string[:index]
		string=string[index+len(replace):]
		index=string.find(replace)
		output+=replaceby
	output+=string[index+len(replace):]		
	return output
if __name__=="__main__":
	string=input("Enter a string:")
	replaceby=input("Enter the character to replace by :")
	output=ReplaceChar(string,replaceby)
	print("OUTPUT String : %s"%(output))	

'''
OUTPUT:

dipeshdd@dipesh-dd:~/python/string$ python replacecharacter.py 
Enter a string:"bubble"
Enter the character to replace by :"*"
OUTPUT String : bu**le

'''		
