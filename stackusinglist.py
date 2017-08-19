def push(l1,data):
	if(isFull(l1)==False):
		data=int(input("Enter the data to PUSH:"))
		l1.append(data)
	else:
		print("Pop Some data as Stack is FULL")
def pop(l1):
	if(isEmpty(l1)==False):
		l1.pop(-1)
	else:
		print("Push Some data as Stack is EMPTY")
def isFull(l1):
	return len(l1)==10
def isEmpty(l1):
	return l1==[] or l1=='NULL'
def peep(l1):
	top=l1[-1]
	print("Top of Stack is :%d"%(top))
if __name__=="__main__":
	l1=[]
	while True:
		print("++++++ STACK OPERATIONS ++++++")
		print("1.PUSH in Stack.")
		print("2.POP from Stack.")
		print("3.PEEP in Stack.")
		print("4.Diplay Stack.")
		print("5.Exit")
		ch=int(input("Enter your choice :"))			
		if ch==1:
			push(l1)
			continue;
		if ch==2:
			pop(l1)
			continue;
		if ch==3:
			print("PEEP operation gives top of Stack...")
			peep(l1)
			continue;
		if ch==4:
			print("Displaying the Stack...")
			print(l1)
		if ch==5:
			print("Thank you for using Stack...")
			break;
		if ch<1 or ch>6:
			print("Please read the Menu Properly...")
			continue;

		
