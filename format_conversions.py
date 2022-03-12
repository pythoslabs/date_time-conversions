'''
converts 2 to '02' for FEB ,
converts 10 to '10' for OCT
in : 8  ( int )
out : '08'  ( str )
'''

def get_month_format(int_month):
    if int_month < 10:
        mm = '0'+str(int_month)
    else :
        mm = str(int_month)    
    return mm
