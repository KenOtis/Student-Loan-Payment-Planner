#Student Loan Planner 

def AmountLST(NumberOfLoans):
    #This function gathers the information from the user 
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

def LoanCalc():
    #find out how many Loans they have 
    NumberOfLoans=int(input("How many Loans do you have? "))
    #call the AmountLST fucntion using the number of loans 
    AmountList=AmountLST(NumberOfLoans)
    #using the sum of the loans, this will then divide it by the amount of time they would like to pay it off in 
    AmountOfTime(AmountList) #The output will be the amount that the user has to pay every month

LoanCalc()