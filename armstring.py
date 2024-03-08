n=input("Enter any number : ")
size=len(n)
n=int(n)
m=n;
sum=0

while(n>0):
    rmd=n%10;
    pow=rmd**size;
    sum=sum+pow;
    n=n//10;

if(m==sum):
    print("Its an Armstrong number.....");