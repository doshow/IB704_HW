def RomanToINT(RomanNo):
    Roman_list = list(RomanNo)
    # print (Roman_list)
    Roman_list.reverse()
    # print (Roman_list)
    count = 1
    No1=0
    No2=0
    total=0
    pass2=0
    num=0
    pass1=len(Roman_list)
    if (pass1%2 != 0 ):
        pass2=1
    for Eng in Roman_list:
        if ("M" == Eng):
            No=1000
        elif ("D" == Eng):
            No=500
        elif ("C" == Eng):
            No=100
        elif ("L" == Eng):
            No=50
        elif ("X" == Eng):
            No=10
        elif ("V" == Eng):
            No=5
        elif ("I" == Eng):
            No=1
        # print (No)
        # print ("count",count)
        if (count ==1 ):
            No1 = No
            count = 2
        elif (count ==2):
            No2 = No
            count = 1
            if (No1 > No2):
                total = total + No1 - No2
                # print ("totoal",total)
            elif (No1 <= No2):
                total = total + No1 + No2
                # print ("totoal",total)
        num=num+1
        if (pass2 and num == pass1):
            total = total + No1
            # print ("totoala",total)
    return total


assert RomanToINT("MMMCCCXXXIII") == 3333, 'Fail'
assert RomanToINT("MCDXXXVII") == 1437, 'Fail'
assert RomanToINT("I") == 1, 'Fail'