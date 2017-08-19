def normalize(l1):
	i=0
	l2=[]
	while(i<len(l1)):
		if(type(l1[i])!=list):
			l2.append(l1[i])
		else:	
			ExtendList(l2,l1[i])
		i+=1
	return l2
def ExtendList(l2,l3):
	j=0
	while(j<len(l3)):
		if type(l3[j])!=list:
			l2.append(l3[j])
		else:
			ExtendList(l2,l3[j])
		j+=1
if __name__=="__main__":
	l1=list(input("Enter A List:"))
	l2=normalize(l1)
	print(l2)
	
	
