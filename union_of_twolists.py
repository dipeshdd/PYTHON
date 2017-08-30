def union(l1,l2):
	unionlist=[]
	unionlist=l1
	for x in l2:
		if x not in l1:
			unionlist.append(x)
	return unionlist
if __name__=="__main__":
	l1=list(input("Enter the First List :"))
	l2=list(input("Enter the Second List :"))
	unionlist=union(l1,l2)
	print("Union OF two List is :")
	print(unionlist)
