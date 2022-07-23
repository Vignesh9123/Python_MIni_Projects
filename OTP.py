import random,sys,time

name = input("Hello There , Can I know your name: ")
print("Hello" , name ,'Please enter the received OTP')
user_access = False
user_limit = 0
while not user_access and user_limit < 3:
    otp_limit = 0
    otp = random.randint(100000, 999999)
    print('( Your OTP is :' , otp, ')')
    while True:
        try:
            user_entry = int(input('OTP : '))
            break
        except:
            print("Please enter only numbers")
            continue

    if user_entry == otp:
        print("Access granted :)")
        time.sleep(2)
        user_access = True
    else :
        user_access = False
        while not user_access:
            otp_limit += 1
            user_entry = int(input("Please enter the correct OTP: "))
            if user_entry == otp:
                print("Access granted :)")
                time.sleep(2)
                user_access = True
                break
            elif otp_limit >= 2:
                user_limit += 1
                if user_limit >= 3:
                    print("Ohh 3 Wrong Attempts!! We would suggest you to try again after some time.\nSorry for the inconvenience.\nThank You")
                    time.sleep(4)
                    sys.exit()
                again = input("Looks like You have got a problem \nWould you like us to send another OTP ?  ")
                if again == "Yes":
                    user_access = False
                    break
                else:
                    print("Thank You")
                    time.sleep(2)
                    sys.exit()
            else :
                continue


