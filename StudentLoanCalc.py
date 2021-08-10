#Student Loan Planner 

def LoanCalc():
    #find out how many Loans they have 
    NumberOfLoans=int(input("How many Loans do you have? "))
    AmountList=[]
    intrestList=[]
    for i in range (NumberOfLoans):
        amount=float(input("What is the loan amount? "))
        AmountList.append(amount)
        intrest=float(input("What is the intrest rate? "))
        intrestList.append(intrest)
    #print(AmountList)
    #print(intrestList)
    #Ordering the amount list by intrest rate list 
    ziplist= list(zip(AmountList,intrestList)) #combining both lists and going to order them by intrest rate
    #determining the payment order, Paying off the highest intrest rate off first 
    InOrder=sorted(ziplist,key = lambda x:x[1],reverse=True)
    #print(InOrder)
    newAL,newIntrest=zip(*InOrder)
    print("The most effiecnt way to pay off your student loans is to pay off the loans with the highest intrest rates first.")
    print("Your recommended payment order is: ")
    count=0
    for i in range(NumberOfLoans):
        count+=1
        print("{}.".format(count),"Pay off the loan in the amount of: ", newAL[i], "with the intrest rate of: ", newIntrest[i],"%")
        time=float(input("How long would you like to pay off this loan in months? "))
        P=newAL[i]
        r=float(newIntrest[i]/100)
        n=time
        t=time
        Intrest=(P*(1+r/n)**(n*t))
        Finalin=Intrest
        Payment=Finalin/time
        print("Your monthly payment will be: ", round(Payment,2)) 
        

LoanCalc() 

