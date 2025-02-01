#Solution to the cryptarithmetic SEND + MORE = MONEY

#S and M can’t be 0, because they are the first letters in the numbers (we can’t start a number with 0).
for S in range(1, 10):
    for E in range(0,10):
        for N in range(0,10):
            for D in range(0,10):
                for M in range(1,10):
                    for O in range(0,10):
                        for R in range(0,10):
                            for Y in range(0, 10):
                                #{S, E, N, D, M, O, R, Y} creates a set with the letters S, E, N, D, M, O, R, Y.
                                #A set in Python is a collection of unique elements. 
                                #If the set has 8 elements, it means that all the letters are different.
                                if len({S,E,N,D,M,O,R,Y})==8:
                                    send = S*1000+ E*100 + N*10 + D
                                    more = M*1000 + O*100 + R*10 + E
                                    money = M*10000 + O*1000 + N*100 + E*10 + Y

                                    #Check if SEND + MORE = MONEY
                                    if send + more == money:
                                        print("SEND = ", send)
                                        print("MORE = ", more)
                                        print("MONEY = ", money)
                                        print("S=", S, "E=", E, "N=", N, "D=", D, "M=", M, "O=", O, "R=", R, "Y=", Y)
                                        break