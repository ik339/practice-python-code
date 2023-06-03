def LongestPw(S):
    S = "test 5 a0A pass007 ?xy1"
    newstring = S.split()
    #print(newstring)

    for i in newstring:
        if i.isalpha() + i.isnumeric(): # is.alnum
            print("true")
        else:
            print("false")
LongestPw(newstring)

len(X)