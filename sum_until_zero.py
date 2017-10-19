def termination():
	total=0
	num=1	
	while(num!=0):
		num=int(input("Enter the Element to add,0 to stop:"))
		total=total+num
	return total
	'''else:
		print("Total Addition :%d"%(total))
		exit(0)'''
if __name__=='__main__':	
	total=termination()
	print("Total Addition : %d"%(total))		
	
