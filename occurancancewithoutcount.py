def Occuranceof(st,subst):
	occ=0
	start=st.find(subst)
	while(start!=-1):
		occ+=1
		st=st[start+1:]
		start=st.find(subst)
	return occ
def main():
	st=str(input("Enter a String :"))
	subst=str(input("Enter a substring :"))
	occ=Occuranceof(st,subst)
	print("Occurance of %s is %d times..."%(subst,occ))
if __name__=="__main__":
	main()
