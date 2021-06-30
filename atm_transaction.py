ac_no= int(input('Your A/C No.: '))
index= data['acc'].index(ac_no)
print('Welcome',data['name'][index])
print('Your Available Balance Is: ',data['bal'][index])
print('\n\n')

choose= ''.join(input('choose a value: Debit / Credit / Change Password: ').split()).lower()

def credit():
    cr= int(input('Your Credit Amount Is: '))
    data['bal'][index] = data['bal'][index] + cr
    print('Your Current Balance Is: ',data['bal'][index])
    
def debit():
    dr= int(input('Your Debit Amount Is: '))
    data['bal'][index] = data['bal'][index] - dr
    print('Your Current Balance Is: ',data['bal'][index])    
    
def change_password():
    data['password'][index]= input('Your New Password Is: ')
    print('Password Succesfuly change')

if choose=='credit':
    credit()
    
elif choose=='debit':
    debit()
        
elif choose=='password':
    change_password()
    
else:
    print('please enter only Credit / Debit / Change Pasword value')


    
print('\n\n')
