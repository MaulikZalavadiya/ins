
def fun(n,s):
    result=" "

    for i in range(len(n)):
        c=n[i]
        if(c.isupper()):
            result +=chr((ord(c) + s-65)%26 + 65)

        else:
            result +=chr((ord(c) + s-97)%26 + 97)

    return result
n=input("enter text:")
s=int(input("enter the key:"))
print("cipher:"+fun(n,s))

#decryption
def fun(n,s):
    result=" "

    for i in range(len(n)):
        c=n[i]
        if(c.isupper()):
            result +=chr((ord(c) + s - 65) % 26 + 65)

        else:
            result +=chr((ord(c)+ s - 97) % 26+ 97)
    return result
n=input("enter text:")
s=(26-int(input("enter key:")))
print("cipher:" + fun(n,s))