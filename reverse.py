number=int(input("enter number : "))
print(str(number)[::-1])
# logic
N=str(input(" enter number : "))
rev_n=0
while N>0:
    remainder=N%10
    rev_n=(rev_n*10)+remainder
    N=N//10
print("The reverse number is : {}"+(rev_n))  

