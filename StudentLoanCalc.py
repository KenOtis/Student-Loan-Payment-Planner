#Student Loan Planner 

def LoanCalc():
    #How many loans do you have?
    NumberOfLoans=int(input("How many loans do you have? "))
    #these lists will append the given loan amounts and intrest rates
    AmountList=[]
    IntrestList=[]
    #this for loop will go through the amount of NumberOfLoans 
    for i in range(NumberOfLoans):
        amount=int(input("What is the loan amount? "))
        AmountList.append(amount)
        intrest=(input("What is the intrest rate? "))
        IntrestList.append(intrest)
    print("AmountList = ",AmountList,"IntrestList = ",IntrestList)
    print("The Amount you owe before intrest: ",sum(AmountList))
    return AmountList, IntrestList

#How many years would you want to pay your loans off in 
def AmountOfTime(AmountList,IntrestList):
    Time=int(input("How many Years would you like to pay off your loans? "))
    year=12 # months
    Payment=(sum(AmountList)/(year*Time))
def DailyIntrest(amount,intrest):
    pass

def WithIntrestPerMonth(amount, intrest):
    pass 

def WithIntrestPerYear(amount, intrest):
    pass 

def main():
    LoanCalc()