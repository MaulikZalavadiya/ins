
text = input("entre your message :")
# key_e = int(input("enter key for encrypt:"))
# key_d = int(input("enter key for encrypt:"))
# result_encrypt = ""
result_decrypt = ""

for key_d in range(-1,-26,-1):

    result_decrypt=""

    for i in range(len(text)):
        char = text[i]

        # Encrypt & Decrypt uppercase characters
        if (char.isupper()):
            # result_encrypt += chr((ord(char) + key_e - 65) % 26 + 65)
            result_decrypt += chr((ord(char) - key_d - 65) % 26 + 65)


            # Encrypt & Decrypt lowercase characters
        else:
            # result_encrypt += chr((ord(char) + key_e - 97) % 26 + 97)
            result_decrypt += chr((ord(char) - key_d - 97) % 26 + 97)

    # print("Encrypt Text %d : %s" %(key_e,result_encrypt))
    print("Decrypt Text %d : %s" % (key_d,result_decrypt))

# print("Encrypt Text: " + result_encrypt)
# print("Decrypt Text: " + result_decrypt)

