# import numpy as np
#
# def encrypt(msg):
#     # Replace spaces with nothing
#     msg = msg.replace(" ", "")
#     # Ask for keyword and get encryption matrix
#     C = key()
#     # Append zero if the messsage isn't divisble by 2
#     len_check = len(msg) % 2 == 0
#     if not len_check:
#         msg += "0"
#     # Populate message matrix
#     P = matrix(msg)
#     # Calculate length of the message
#     msg_len = int(len(msg) / 2)
#     # Calculate P * C
#     msg = ""
#     for i in range(msg_len):
#         # Dot product
#         row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]
#         # Modulate and add 65 to get back to the A-Z range in ascii
#         integer = int(row_0 % 26 + 65)
#         # Change back to chr type and add to text
#         msg += chr(integer)
#         # Repeat for the second column
#         row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
#         integer = int(row_1 % 26 + 65)
#         msg += chr(integer)
#     return msg
#
# def decrypt(msg):
#     # Ask for keyword and get encryption matrix
#     C = key()
#     # Inverse matrix
#     deter = C[0][0] * C[1][1] - C[0][1] * C[1][0]
#     deter = deter % 26
#     mult_inv = mul_inv(deter)
#     C_inverse = C
#     # Swap a <-> d
#     C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
#     # Replace
#     C[0][1] *= -1
#     C[1][0] *= -1
#     for row in range(2):
#         for column in range(2):
#             C_inverse[row][column] *= mult_inv
#             C_inverse[row][column] = C_inverse[row][column] % 26
#
#     P = matrix(msg)
#     msg_len = int(len(msg) / 2)
#     msg2d = ""
#     for i in range(msg_len):
#         # Dot product
#         column_0 = P[0][i] * C_inverse[0][0] + P[1][i] * C_inverse[0][1]
#         # Modulate and add 65 to get back to the A-Z range in ascii
#         integer = int(column_0 % 26 + 65)
#         # Change back to chr type and add to text
#         msg2d += chr(integer)
#         # Repeat for the second column
#         column_1 = P[0][i] * C_inverse[1][0] + P[1][i] * C_inverse[1][1]
#         integer = int(column_1 % 26 + 65)
#         msg2d += chr(integer)
#     if msg2d[-1] == "0":
#         msg2d = msg2d[:-1]
#     return msg2d
#
# def mul_inv(deter):
#     mult_inv = -1
#     for i in range(26):
#         inverse = deter * i
#         if inverse % 26 == 1:
#             mult_inv = i
#             break
#     return mult_inv
#
#
# def key():
#      # Make sure cipher determinant is relatively prime to 26 and only a/A - z/Z are given
#     deter = 0
#     C = None
#     while True:
#         cipher = input("Input 4 letter cipher: ")
#         C = matrix(cipher)
#         deter = C[0][0] * C[1][1] - C[0][1] * C[1][0]
#         deter = deter % 26
#         inverse_element = mul_inv(deter)
#         if inverse_element == -1:
#             print("Determinant is not relatively prime to 26, uninvertible key")
#         elif np.amax(C) > 26 and np.amin(C) < 0:
#             print("Only a-z characters are accepted")
#             print(np.amax(C), np.amin(C))
#         else:
#             break
#     return C
#
# def matrix(string):
#     # Map string to a list of integers a/A <-> 0, b/B <-> 1 ... z/Z <-> 25
#     integers = [chr_to_int(c) for c in string]
#     length = len(integers)
#     M = np.zeros((2, int(length / 2)), dtype=np.int32)
#     iterator = 0
#     for column in range(int(length / 2)):
#         for row in range(2):
#             M[row][column] = integers[iterator]
#             iterator += 1
#     return M
#
# def chr_to_int(char):
#     # Uppercase the char to get into range 65-90 in ascii table
#     char = char.upper()
#     # Cast chr to int and subtract 65 to get 0-25
#     integer = ord(char) - 65
#     return integer
#
# if __name__ == "__main__":
#     msg = input("Message: ")
#     msg = encrypt(msg)
#     print(msg)
#     msg2d = decrypt(
#         msg)
#     print(msg2d)
import numpy as np


def find_multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse


def inverse(C):
    determinant = (C[0][0] * C[1][1]) - (C[0][1] * C[1][0])
    determinant = determinant % 26
    multiplicative_inverse = find_multiplicative_inverse(determinant)
    C_inverse = C
    C_inverse[0][0], C_inverse[1][1] = C_inverse[1, 1], C_inverse[0, 0]
    C[0][1] *= -1
    C[1][0] *= -1
    for row in range(2):
        for column in range(2):
            C_inverse[row][column] *= multiplicative_inverse
            C_inverse[row][column] = C_inverse[row][column] % 26
    return C


def encdec(key, str, t):
    str = ''.join([(ch if ch.isalpha() else '') for ch in str.upper()])
    str += '' if len(str)%2==0 else 'X'
    key = ''.join([(ch if ch.isalpha() else '') for ch in key.upper()])
    key = [key[i % len(key)] for i in range(4)]
    str = [ord(ch) - 65 for ch in str]
    key = [ord(ch) - 65 for ch in key]
    mkey = np.array([[key.pop(0) for j in range(2)] for i in range(2)])
    mstr = []
    while len(str)>0:
        mstr.append([str.pop(0) for j in range(2)])
    mstr = np.array(mstr)

    if t==-1:
        mkey = inverse(mkey)

    mtxt = np.array(mstr).dot(np.array(mkey))

    txt = ''
    for i in mtxt:
        for j in i:
            txt += chr((j%26)+65)
    return txt


plain_txt = input('Enter a plain text:')
key = input('Enter a key:')
cipher_txt = encdec(key, plain_txt, 1)
print('Cipher text:', cipher_txt)

cipher_txt = input('Enter a cipher text:')
key = input('Enter a key:')
plain_txt = encdec(key, cipher_txt, -1)
print('Plain text:', plain_txt)