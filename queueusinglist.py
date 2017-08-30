def enqueue(l1):
	if(not isFull(l1)):
		data=int(input("Enter the data :"))
		l1.append(data)
	else:
		print("QUEUE IS FULL DEQUEUE FIRST...")	
def dequeue(l1):
	if(not isEmpty(l1)):
		l1.pop(0)
	else:
		print("QUEUE IS EMPTY ENQUEUE FIRST...")
def isFull(l1):
	return len(l1)==10
def isEmpty(l1):
	return l1==[] or l1=="NULL"
if __name__=="__main__":
	l1=[]
	while True:
		print("++++++ QUEUE OPERATIONS ++++++")
		print("1.ENQUEUE.")
		print("2.DEQUEUE.")
		print("3.Diplay QUEUE.")
		print("4.Exit")
		ch=int(input("Enter your choice :"))			
		if ch==1:
			enqueue(l1)
		if ch==2:
			dequeue(l1)
		if ch==3:
			print("Displaying the QUEUE...")
			print(l1)
		if ch==4:
			print("Thank you for using Stack...")
			break;
		if ch<1 or ch>4:
			print("Please read the Menu Properly...")
