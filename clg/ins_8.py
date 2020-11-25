p=int(input("Enter a prime number:"))
flag=1
for i in range(2,p):
    if p%i==0:
        flag=0
if flag==0:
    print(p," is not a prime number")

if flag==1:
    g=int(input("primitive root of 'p':"))
    if 2<=g<=p-2:
        x = int(input("Secret key for sender:"))
        y = int(input("Secret key of receiver:"))
        R1=(g**x)%p
        R2=(g**y)%p
        Ks=(R2**x)%p
        Kr=(R1**y)%p
        key=(g**(x*y))%p
        print("Public key of Sender:", R1)
        print("Public key of receiver:", R2)
        print("public key sender:",Ks)
        print("public key receiver:",Kr)
        print("Key",key)
    else:
        print(g, " is not primitive root of ", p)




