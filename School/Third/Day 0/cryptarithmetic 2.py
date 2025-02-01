# Solution to cryptarithmetic CROSS + ROADS = DANGER

# C and D can’t be 0, because they are the first letters in the CROSS and DANGER (we can’t start a number with 0).
for C in range(1,10):
    for R in range(0,10):
        for O in range(0,10):
            for S in range(0,10):
                for A in range(0,10):
                    for D in range(1,10):
                        for N in range(0,10):
                            for G in range(0,10):
                                for E in range(0,10):
                                    if len({C,R,O,S,A,D,N,G,E}) ==9:
                                        cross = C*10000+ R*1000+ O*100+S*10+S
                                        roads = R*10000+ O*1000+ A*100+ D*10+S
                                        danger = D*100000+ A*10000+ N*1000+ G*100+E*10+ R

                                        if cross + roads == danger:
                                            print("CROSS = ", cross)
                                            print("ROADS = ", roads)
                                            print("DANGER = ", danger)
                                            print("C=", C, "R=", R, "O=", O, "S=", S, "A=", A, "D=", D, "N=", N, "G=", G, "E=", E)
                                            break
