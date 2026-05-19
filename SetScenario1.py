Scenario 1:

age=int(input("Enter your age:"))
if (age >=18):
    print("You are Eligible")
else:
    print("Your are not Eligible")


Scenario 2:

items=list(map(int,input("Enter the numbers with a space:").split()))
large=max(items)
print("Largest value in list is:",large)

Scenario 3:

sal=int(input("Enter your salary:"))
if(sal>50000):
   bon=((sal*0.1)+sal)
   print("YOUR SALARY AFTER BONUS:",bon)
else:
   print("You are not eligible for bonus")

Scenario 4:

num=int(input("Enter a number:"))
if(num%2 == 0):
    print(num,"is a Even number")
else:
    print(num."is a Odd number")


Scenario 5:

word=input("Enter a sentence:")
res=''.join(word.split()[::-1])
print(res)



Scenario 6:

mark=int(input("Enter your mark:")
if (mark>=40):
    print("You passed the exam")
else:
    print("you failed the exam")


Scenario 7:

TotOrder=int(input("Enter your total order amount:"))
if (TotOrder>100):
    finAmt=(TotOrder - (TotOrder*0.2))
    print("Your final amount:",finAmt)
else:
    print("Your are not eligible for discount")


Scenario 8:
#check the bank balance of user once card swipped
#it is stored as BalAmt

WthReq=int(input("Enter your amount:"))
if(WthReq<BalAmt):
   les= BalAtmt - WthReq
   print("Your balance:",les)
elif(WthReq==BalAmt):
   print("Your balance is zero")
else:
   print("You don't have sufficient balance")

Scenario 9:

lep=int(input("Enter the year:"))
if(lep%4==0 and lep%100!=0) or (lep%400==0):
   print(lep,"is a leap year")
else:
   print(lep,"is not a leap year")

Scenario 10:

items = list(map(int,input("Enter the items with a space:).split()))
for i in items:
    if (i%2==0):
        print(i)
    else:
       print("No even numbers in lists")






