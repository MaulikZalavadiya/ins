def enc(key, str):
    key = ''.join([key.upper()[i % len(key)] for i in range(len(str))])
    str = list(str.upper())
    [str.remove(' ') for i in range(str.count(' '))]
    return ''.join([chr(((ord(str[i])+ord(key[i])-130)%26)+65) for i in range(len(str))])


def dec(key, str):
    key = ''.join([key.upper()[i % len(key)] for i in range(len(str))])
    return ''.join([chr(((ord(str[i])-ord(key[i]))%26)+65) for i in range(len(str))])

plain_txt = input('Enter a plain text:')
key = input('Enter a Key:')
cipher_txt = enc(key, plain_txt)
print('cipher Text:', cipher_txt)

cipher_txt = input('Enter a cipher text:')
key = input('Enter a Key:')
plain_txt = dec(key, cipher_txt)
print('Plain Text:', plain_txt)