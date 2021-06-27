for n in range (2, 10):  # A
    print("Looping in A")
    for x in range (2, n): # B
        if n % x == 0:
            print("Looping in B")
            print(n,"equals",x,"*",n/x)
            print("Breaking out of A and B")
            break
    else:
# loop fell through without finding a factor
        print("Broken out of A and B, and Entered the else block")
        print(n, "is a prime number "),

