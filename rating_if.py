def rating(rate):
	if(rate>4 and rate<=5):
		print("You Have Rating %f That is 'Excellient'"(rate))
	elif(rate>3 and rate<=4):
		print("You Have Rating %f That is 'Very Good'"%(rate))
	elif(rate>2 and rate<=3):
		print("You Have Rating %f That is 'Good'"%(rate))
	elif(rate>1 and rate<=2):
		print("You Have Rating %f That is 'Average'"%(rate))
	else:
		print("You Have Rating %f That is 'Aweful'"%(rate))
if __name__=='__main__':
	rate=float(input("Rate So and SO between 1 to 5 and get its report :"))
	rating(rate)

