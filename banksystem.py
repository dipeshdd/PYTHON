class Bank:
	account_num_generator=1
	def __init__(self,name,address,initBal=0):
		self.__AccountNum=Bank.account_num_generator
		Bank.account_num_generator+=1
		self.__AccountName=name
		self.__Address=address
		self.__Balance=initBal
	def Deposit(self,DepositAmount):
		if(DepositAmount>=50000):
			print("PAN NUMBER IS REQUORED AS AMOUNT EXCEED 50000")
		elif(DepositAmount>0):
			self.__Balance=self.__Balance+DepositAmount
		else:
			print("Amount is never negative")
	def Withdrawal(self,WithdrawAmount):
		if(WithdrawAmount<=20000):
			print("WithdrawAmount Greater than 20000")
		elif(self.__Balance>=WithdrawAmount)
			self.__Balance=self.__Balance-WithdrawAmount
		elif(WithdrawAmount<0):
			print("Amount never negative")
		else:
			print("Account Balance is Less than WithdrawAmount")
	def BalanceCheck(self):
		print("Balance : %d"%(self.__Balance))
def main():
	b1=Bank("Dipesh Desadla","Pune",1000)
	while(True):	
		print("1.Deposit")
		print("2.Withdrawal")
		print("3.Account Balance")
		print("4.Exit")
		print("Enter your choice:")
		choice=input()
		if(choice==1):		
			amount=input("Enter the Deposit Amount:")
			b1.Deposit(amount)
		elif(choice==2):
			amount=input("Enter the Withdrawal Amount:")
			b1.Withdrawal(amount)
		elif(choice==3):
			b1.BalanceCheck()
		elif(choice==4):
			exit()
		else:
			print("Invalid Choice")
if __name__=="__main__":
	main()
		
