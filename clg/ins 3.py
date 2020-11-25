letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
key=input("enter key:")
def enc(str):
    text = ''
    for ch in str:
        if ch.isupper():
            A= key[letters.find(ch)]
            print(ch,"=",A)
            text +=A

        elif ch.islower():
            a= key.lower()[letters.find(ch.upper())]
            print (ch,"=",a)
            text +=a
        else:
            text += ch
    return text


def dec(str):
    text = ''
    for ch in str:
        if ch.isupper():
            text += letters[key.find(ch)]
        elif ch.islower():
            text += letters.lower()[key.find(ch.upper())]
        else:
            text += ch
    return text


plain_txt = input('Enter a plain text:')
ciper_txt = enc(plain_txt)

key.isupper()
print('Ciper Text:', ciper_txt)


ciper_txt = input('Enter a ciper text:')
plain_txt = dec(ciper_txt)

key.isupper()
print('Plain Text:', plain_txt)
