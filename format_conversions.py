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


'''
converts 20-07-2002  to 200207
in : 20-07-2002  ( str )
out : '200207'  ( str )
'''

def get_yyyymm_format(str_date):
    yyyy = str_date.split('-')[2]
    mm =  str_date.split('-')[1]
    dt_new_format = yyyy + mm
    return dt_new_format 

# Hint : Incase you want to use it in a dataframe of many rows , use apply function like shown below 
# df_SO['yyyymm'] = df_SO['Month Starting'].apply(lambda x : get_yyyymm_format(x))
