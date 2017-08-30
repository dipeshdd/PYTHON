def Counter(string):
	vcount=0
	ccount=0
	ocount=0
	for x in string:
		if(x in 'aeiou' or x in 'AEIOU'):
			vcount+=1
		elif(x.isalpha()):
			ccount+=1
		else:
			ocount+=1
	return vcount,ccount,ocount
def main():
	string=input("Enter a String :")
	vcount,ccount,ocount=Counter(string)
	print("Count of Vowel is %d "%(vcount))
	print("Count of Consonant is %d "%(ccount))
	print("Count of Other is %d "%(ocount))
if __name__=="__main__":
	main()
