#Student Loan Planner 

def LoanCalc():
    pass
def AmountLST(NumberOfLoans):
    AmountList=[]
    intrestList=[]
    for i in range (NumberOfLoans):
        amount=float(input("What is the loan amount? "))
        AmountList.append(amount)
        intrest=float(input("What is the intrest rate? "))
        intrestList.append(intrest)
    return AmountList
#How many years would you want to pay your loans off in 
def AmountOfTime(AmountList):
    Time=int(input("How many Years would you like to pay off your loans? "))
    year=12 # months
    Payment=(sum(AmountList)/(year*Time))
    print("Your Monthly payment would be: $",round(Payment,2), "A Month")
def DailyIntrest(amount,intrest):
    pass

def WithIntrestPerMonth(amount, intrest):
    pass 

def WithIntrestPerYear(amount, intrest):
    pass 

def main():
    #First find out how many Loans they have 
    NumberOfLoans=int(input("How many Loans do you have? "))
    AmountList=AmountLST(NumberOfLoans)
    AmountOfTime(AmountList)

main()