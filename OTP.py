import random

name = input("Hello There , Can I know your name: ")
print("Hello" , name ,'Please enter the received OTP')
user_access = False
while not user_access:
    otp_limit = 0
    otp = random.randint(100000, 999999)
    print('( Your OTP is :' , otp, ')')
    try :
       user_entry = int(input('OTP : '))
    except ValueError:
       user_entry = int(input("Invalid OTP \nTry Again : "))
       if user_entry == otp:
            print("Access granted :)")
            user_access = True
       else :
            user_access = False
            while not user_access:
                otp_limit += 1
                user_entry = int(input("Please enter the correct OTP: "))
                if user_entry == otp:
                    print("Access granted :)")
                    user_access = True
                    break
                elif otp_limit >= 2:
                    again = input("Looks like You have got a problem \nWould you like us to send another OTP ?  ")
                    if again == "Yes":
                        user_access = False
                        break
                    else:
                        break
                else :
                    continue


