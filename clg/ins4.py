# def matrix(key):
#     ls = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
#     [ls.remove(ch) for ch in key.upper()]
#     m = list(key.upper()) + ls
#     return [[m.pop(0) for j in range(6)] for i in range(6)]
#
# def m_print(m):
#     for i in range(6):
#         for j in range(6):
#             print(m[i][j], end=' ')
#         print()
#
# def getaxis(matrix, ch):
#     for i in range(6):
#         for j in range(6):
#             if matrix[i][j] == str(ch).upper(): return i, j
#
# def proplaintxt(plain_txt):
#     txt = list(plain_txt.upper())
#     [txt.remove(' ') for i in range(txt.count(' '))]
#     i = 0
#     while i < int(len(txt)/2)*2:
#         if txt[i]==txt[i+1] : txt.insert(i+1, 'X')
#         i += 2
#     if len(txt)%2 != 0 : txt.append('X')
#     return txt
#
# def settxt(txt):
#     if len(txt)%2 == 0 and txt[-1]=='X': txt.pop()
#     i=0
#     while i < len(txt):
#         try:
#             if txt[i]==txt[i+2] and txt[i+1]=='X' : txt.pop(i+1)
#         except: ''
#         i += 1
#     return txt
#
#
# def encdec(m, txt, k):
#     ctxt = []
#     i, n = 0, len(txt)
#     while (i < n):
#         a, b = getaxis(m, txt[i])
#         c, d = getaxis(m, txt[i + 1])
#         if a == c:
#             ctxt.append(m[a][(b + k) % 6])
#             ctxt.append(m[c][(d + k) % 6])
#         elif b == d:
#             ctxt.append(m[(a + k) % 6][b])
#             ctxt.append(m[(c + k) % 6][d])
#         else:
#             ctxt.append(m[a][d])
#             ctxt.append(m[c][b])
#         i += 2
#     return ctxt
#
#
# def enc(key, str):
#     m = matrix(key)
#     txt = proplaintxt(str)
#     m_print(m)
#     return ''.join(encdec(m, txt, 1))
#
# def dec(key, str):
#     m = matrix(key)
#     txt = proplaintxt(str)
#     m_print(m)
#     return ''.join(settxt(encdec(m, txt, -1)))
#
# plain_txt = input('Enter a plain text:')
# key = input('Enter a Key:')
# cipher_txt = enc(key, plain_txt)
# print('cipher Text:', cipher_txt)
#
# cipher_txt = input('Enter a cipher text:')
# key = input('Enter a Key:')
# plain_txt = dec(key, cipher_txt)
# print('Plain Text:', plain_txt)
##################################################################################################
def generateKey(string, key):
    key = list(key)

    if len(string) == len(key):

        return key

    else:

        for i in range(len(string) - len(key)):
            key.append(key[i % len(key)])

    return "".join(key)


def cipherText(string, key):
    cipher_text = []

    for i in range(len(string)):
        x = (ord(string[i]) + ord(key[i])) % 26

        x += ord('A')

        cipher_text.append(chr(x))

    return "".join(cipher_text)


def originalText(cipher_text, key):
    orig_text = []

    for i in range(len(cipher_text)):
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26

        x += ord('A')

        orig_text.append(chr(x))

    return "".join(orig_text)


string = input("Enter the string: ").upper().replace(" ", "")

keyword = input("Enter the key: ").upper().replace(" ", "")

key = generateKey(string, keyword)

cipher_text = cipherText(string, key)

print("Ciphertext :", cipher_text)

cipher_text = input("Enter the cipher text: ").upper().replace(" ", "")

keyword = input("Enter the key: ").upper().replace(" ", "")

key = generateKey(string, keyword)

print("Original/Decrypted Text :", originalText(cipher_text, key))