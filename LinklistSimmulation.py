class Linklist:
	def __init__(self,size):
		self.__mLinklist=[]
		self.__mSize=size
	def Insertatpos(self,pos,data):
		if(pos<=self.__mSize and pos>=0):
			self.__mLinklist.insert(pos,data)
	def Deletebypos(self,pos):
		self.__mLinklist.remove(self.__mLinklist[pos])
	def Deletebydata(self,data):
		self.__mLinklist.remove(data)
	def DisplayLinklist(self):
		print(self.__mLinklist)
	def Occurance(self,data):
		x=0
		count=0
		while(x!=len(self.__mLinklist)):
			if(self.__mLinklist[x]==data):
				count+=1
			x+=1
		return count
	def Searchdata(self,data):
		x=0
		flag=0
		while(x!=len(self.__mLinklist)):
			if(self.__mLinklist[x]==data):
				print("Element %d Found at Position %d"%(data,x))
				flag=1
				break
			x+=1
		if(flag==0):
			print("Element %d Not Found."%(data))
def main():
	size=input("Enter the Size of LinkList: ")
	intLink=Linklist(size)
	while(True):
		print("=== MENU ===")		
		print("1.Insert at pos")
		print("2.Delete by pos")
		print("3.Delete by data")
		print("4.Occurance of a data")
		print("5.Search the element")
		print("6.DISPLAY Linklist")
		print("7.EXIT")
		choice=input("Enter your Choice :")
		if(choice==1):
			pos,data=input("Enter position and data:")
			intLink.Insertatpos(pos,data)
		elif(choice==2):
			pos=input("Enter the position:")
			intLink.Deletebypos(pos)
		elif(choice==3):
			data=input("Enter the data:")
			intLink.Deletebydata(data)
		elif(choice==4):
			data=input("Enter the data to find its Occurance :")
			count=intLink.Occurance(data)
			print("Count = %d"%(count))
		elif(choice==5):
			data=input("Enter Element to search:")
			intLink.Searchdata(data)	
		elif(choice==6):
			intLink.DisplayLinklist()
		elif(choice==7):
			exit();	
		else:
			print("Invalid Choice");
if __name__=="__main__":
	main()
