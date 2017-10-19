def time_validation(hr,mnt,sec):
	if(hr<=12):
		print("Hour is VALID")
	else:
		print("Hour is INVALID")
	if(mnt<=60):
		print("MIN is VALID")
	else:
		print("MIN is INVALID")
	if(sec<=60):
		print("SEC is VALID")
	else:
		print("SEC is INVALID")
if __name__=='__main__':
	hr,mnt,sec=input("Enter TIME in HR,MIN,SEC :")
	time_validation(hr,mnt,sec)
