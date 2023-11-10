


name = input("enter your name:")
email = input("enter your email:")
city = input("enter your city:")
mobile = input("enter your mobile:")

if len(name)>1:
    if'@' in email and len(email)> 11:
        if len(mobile) == 10 and mobile.isnumeric():
            if city in ["lucknow","delhi", "noida"]:
                print("your data is saved,Shukriya")
            else:
                print("we are not available in your city😢")
        else:
            print("ivalid mobile number😢")
    else:
        print("invalid email address😢")
else:
    print("nice to meet you❤️")
