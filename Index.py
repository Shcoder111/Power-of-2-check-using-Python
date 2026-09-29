input("n & (n-1) clears the rightmost set bit. Press Enter ")
print(" 12 & 11 = ",12 & 11, " binary - ", bin( 12 & 11)[2:1])
print(" 8 & 7 =", 8 & 7)

n = int(input("Enter a no. (try 4 or 6)"))
Guess = input("Is " + str(n) + "a power of 2 ??? (Y/Yes/N/No) - ")
input("Power of 2 - n & (n-1) == 0 means only one bit is ON. Press Enter - ")
if n > 0 and (n & (n - 1)) == 0:
    print(" ", n, " binary : ", bin(n)[2:], " power of 2 : yes \n Your Guess - ", Guess)
else:
    print(" ", n, " binary : ", bin(n)[2:], " power of 2 : no \n Your Guess - ", Guess)