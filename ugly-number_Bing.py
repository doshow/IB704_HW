def ugly_No(u_No):
    final_num = u_No
    gogo = 1
    while gogo:
        if (final_num%2 == 0):
            final_num=final_num/2
        elif(final_num%3 == 0):
            final_num=final_num/3
        elif(final_num%5 == 0):
            final_num=final_num/5
        else:
            gogo=0
    
    if (final_num ==1):
        return True
    else:
        return False


assert ugly_No(6) is True, 'Fail'
assert ugly_No(8) is True, 'Fail'
assert ugly_No(14) is False, 'Fail'
assert ugly_No(-2147483648) is False, 'Fail'
assert ugly_No(-1000) is False, 'Fail'