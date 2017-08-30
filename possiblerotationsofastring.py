l1=[]
def CreateRotaion(string):
	size=len(string)
	string2=string+string
	for i in range(len(string)): 
		l1.append(string2[i:(size+i)])
	print(l1)	
if __name__=="__main__":
	string=input("Enter a string :")
	CreateRotaion(string)
