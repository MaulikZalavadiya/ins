p=int(input("Enter a prime number:"))
q=int(input("Enter distinct prime number from first:"))
flag=1
def gcd(a,b):
    while(b):
        a,b=b,a%b
    return a
for i in range(2,p):
    if p%i==0:
        flag=0
if flag==0:
    print(p," is not a prime number")
if flag==1:
    for i in range(2, q):
        if q % i == 0:
            flag = 0
    if flag == 0:
        print(q, " is not a prime number")
    elif flag==1:
        n,x=p*q,(p-1)*(q-1)
        e=int(input("Enter encryption key:"))
        if gcd(e,x)==1:
            d="Decryption key"
            y=1%x, e * d
            for i in range(10000):
                a=i*e
                if a%x==1:
                    d=i
                    print("Decryption key is:",d)
                    break
            z=input("Do you want to encrypt or decrypt:")
            if z=="encrypt":
                Pt=int(input("Enter plain text:"))
                Ct=((Pt)**e)%n
                print("Cipher text:",Ct)
            elif z=="decrypt":
                Ct = int(input("Enter cipher text:"))
                Pt=((Ct)**d)%n
                print("Plain text:",Pt)
        else:
            print("GCD of",e,"and",x,"is not 1.So Encryption is not possible")



