'''
I/P String: I Am not that bad in python than C
O/P String: I Am good in python than C
'''
def ReplaceSubString(string,start,end,replaceby):
	output_string=""
	start_index=string.find(start)				
	if(start_index!=-1):
		end_index=string[start_index:].find(end)	
		if(end_index!=-1):
			print("Pattern Found")
			output_string=string[:start_index]	# add the string till we find the start pattern
			output_string+=replaceby			# replacepattern is added to string
			output_string+=string[start_index+end_index+len(end):]	#add the remaing after endpattern
	if output_string=="":						
		print("Pattern NOT FOUND")
		return string							#if pattern is not found the the input string is returned
	return output_string	
if __name__=="__main__":
	string=str(input("Enter a String:"))
	start,end=str(input("Enter start and end of the pattern to be replaced :"))
	replaceby=str(input("Enter the String to be replaced with:"))
	output_return=ReplaceSubString(string,start,end,replaceby)
	print("The replace string is :")	
	print(output_return)
		
