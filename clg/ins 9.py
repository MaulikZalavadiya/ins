# def modulo_multiplicative_inverse(A, M):
#     gcd, x, y = extended_euclid_gcd(A, M)
#     if x < 0:
#         x += M
#     return x
# def extended_euclid_gcd(a, b):
#     b1 = 0; a1 = 1
#     b2 = 1; a2 = 0
#     b3 = b; a3 = a
#     while b3 != 0:
#         q = a3//b3
#         a3, b3 = b3, a3 - q*b3
#         a1, b1 = b1, a1 - q*b1
#         a2, b2 = b2, a2 - q*b2
#         print ("A1, A2, A3 :",a1 ,a2 ,a3)
#         print("B1, B2, B3 :",b1 ,b2 ,b3)
#         print("\n")
#     return [a3, a1, a2]
# print(modulo_multiplicative_inverse(int(input("Enter value of A: ")), int(input("Enter value of M: "))))
m = int(input("enter value of m :"))
b = int(input("enter value of b :"))

a1, a2, a3 = 1, 0, m
b1, b2, b3 = 0, 1, b

q = int(a3 / b3)

t1, t2, t3 = a1 - q * b1, a2 - q * b2, a3 - q * b3

print("q\ta1\ta2\ta3\tb1\tb2\tb3\tc1\tc2\tc3")

def my_fun():
    print(str(q) + "\t\t" + str(a1) + "\t\t" + str(a2) + "\t\t" + str(a3) + "\t\t" + str(b1) + "\t\t" + str(
        b2) + "\t\t" + str(
        b3) + "\t\t" + str(t1) + "\t\t" + str(t2) + "\t\t" + str(t3))
my_fun()


# a1, a2, a3 = b1, b2, b3
# b1, b2, b3 = t1, t2, t3

while b3 != 0 or b3 != 1:
    a1, a2, a3 = b1, b2, b3
    b1, b2, b3 = t1, t2, t3
    q = int(a3 / b3)
    t1, t2, t3 = a1 - q * b1, a2 - q * b2, a3 - q * b3

    my_fun()

    if b3 == 0:
        print("no inverse")
    elif b3 == 1:
        print("inverse = "+str(b2%26))



