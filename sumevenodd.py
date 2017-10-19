#!/usr/bin/python
def evenoddsum(start,end):
	evensum=0
	oddsum=0	
	for i in range(start,end+1):
		if(i&1):
			oddsum=oddsum+i	
		else:
			evensum=evensum+i	
	return evensum,oddsum
print("Its An Even ODD ADDtion Example",__name__)
def main():
	start,end=eval(input("Enter the Range i.e start,end :"))
	if(start<=end):	
		evensum,oddsum=evenoddsum(start,end)		
		print("Even SuM iS :%d"%(evensum))
		print("Odd SuM iS :%d"%(oddsum))
	else:
		print("Lower Bound Is NEver Greater than Upper Bound...")
if __name__=="sumevenodd":
	main()
