def evenoddsum(start,end):
	evensum=0
	oddsum=0	
	while start<=end:	
		if(start&1):
			oddsum=oddsum+start
		else:
			evensum=evensum+start
		start+=1
	return evensum,oddsum
if __name__=='__main__':
	start,end=input("Enter the Range i.e start,end :")	
	evensum,oddsum=evenoddsum(start,end)		
	print("Even SuM iS :%d"%(evensum))
	print("Odd SuM iS :%d"%(oddsum))

