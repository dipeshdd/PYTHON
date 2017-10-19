def multipleofsix(start,end):
	result=0
	for i in range(start,end+1):	
		if(i%6==0):
			result=result+i
		else:
			continue
	return result
if __name__=='__main__':
	start,end=input("Enter the start and end range:")
	result=multipleofsix(start,end)
	print("Sum of Multiples of 6 in range %d to %d is: %d"%(start,end,result))
