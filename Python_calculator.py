class calculaor:
    def add(self,n1,n2):
        print(f"{n1} + {n2} = {n1+n2}")
    def sub(self,n1,n2):
        print(f"{n1} - {n2} = {n1-n2}")
    def mul(self,n1,n2):
        print(f"{n1} * {n2} = {n1*n2}")
    def div(self,n1,n2):
        print(f"{n1} / {n2} = {n1/n2}") 

num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
opp=input("Enter your choice(+,-,*,/):")

cal=calculaor()

if opp=="+":
    cal.add(num1,num2)
elif opp=="-":
    cal.sub(num1,num2)
elif opp=="*":
    cal.mul(num1,num2)
elif opp=="/":
    cal.div(num1,num2)
else:
    print("Invalid Operator...Please try agian!")