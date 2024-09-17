print("\n-------Welcome to the World\'s_Trustable_Bank...!-------\n\nThanks for choosing us..!")

accounts=[
    {
        "mail":"loki@gmail.com",
        "password":"Loki@123",
        "amount":200
    },
    {
        "mail":"kala@gmail.com",
        "password":"Kala@123",
        "amount":10000
    },
    {
        "mail":"kunni@gmail.com",
        "password":"Royalking@123",
        "amount":500000
    },
    {
        "mail":"dayyam@gmail.com",
        "password":"Siri@123",
        "amount":100
    },
    {
        "mail":"queen@gmail.com",
        "password":"Queen@143",
        "amount":1000000000000
    },
    {
        "mail":"king@gmail.com",
        "password":"King@143",
        "amount":10000000
    }
]

def mail_seq(para_mail):
    if para_mail[-10::1]=="@gmail.com":
        return True

def lett_dig_symbol(key):
    special_characters = "!@#$%^&*()_+{}\[\]:;<>,.?\'\"\\|`~-="
    spl_char = False
    digit = False
    letter = False
    for x in key:
        if x in special_characters:
            spl_char = True
        elif x.isdigit():
            digit = True
        elif x.isalpha():
            letter = True
    return spl_char and digit and letter

def sign_in():
    email=input("\nplease enter ur email : ").lower()
    for x in accounts:
        if x["mail"]==email:
            key=input("\nenter ur password : ")
            if x["password"]==key:
                step1=int(input("\nchoose the operation u need..!\n1. Deposit\n2. Withdrawal\n3. Balance_enquire\nEnter here :"))
                if step1==1:
                    dep_amo=int(input("Enter the amount you have to deposit : "))
                    x["amount"]+=dep_amo
                    print("\nu r account is credited with Rs.",dep_amo)
                    a=input("\nwould you like to check ur balance..? [yes or no] : ")
                    if a=="yes":
                        print("\nur bank balance is ",x["amount"])
                        print("\nthanks for choosing WTB")
                        return 
                    if a=="no":
                        print("\nthanks for choosing WTB")
                        return
                    else:
                        print("\ninvalid syntax")
                        print("\nthanks for choosing WTB")
                        return
                    
                elif step1==2:
                    wd_amo=int(input("\nEnter the amount u need to withdrawal : "))
                    if wd_amo<=x["amount"]:
                        x["amount"]-=wd_amo
                        print("collect ur cash : ",wd_amo)
                        a=input("\nwould you like to check ur balance..? [yes or no] : ")
                        if a=="yes":
                            print("\nur bank balance is ",x["amount"])
                            print("\nthanks for choosing WTB")
                            return 
                        if a=="no":
                            print("\nthanks for choosing WTB")
                            return
                        else:
                            print("\ninvalid syntax")
                            print("\nthanks for choosing WTB")
                            return
                    else:
                        print("u didn\'t have sufficient money to withdrawal")
                        print("\nthanks for choosing WTB")
                        return
                    
                elif step1==3:
                    print("ur bank balance is ",x["amount"])
                    print("\nthanks for choosing WTB")
                    return
                else:
                    print("wrong syntax")
                    print("\nthanks for choosing WTB")
                    return
            else:
                print("u entered a wrong password")
                print("\nthanks for choosing WTB")
                return
                    
    else: 
        print("u didn't registered yet..!")
        new=input("r u want to continue with sign up [yes/no]: ").lower()
        if new=="yes":
            sign_up()
        else:
            print("thanks for choosing WTB")

def sign_up():
    accounts.append(dict())
    print("\ncreate a mail using\'@gmail.com\' in the end")
    email=input("create a new mail : ")
    turns = 3
    while turns>0:
        if len(email) < 21 and len(email) > 10 and mail_seq(email):
            print("\nEMAIL HAS CREATED SUCCESSFULLY....!")
            print("\n----------------------------->>>>>>>\n")
            break
        else:
            print("\nsorry...!\nchoose an unique mail and the mail must need\'@gmail.com\' in the end\n")
            turns = turns -1
            if turns == 0:
                print("\nsorry...! access denined")
                print("\nthanks for choosing WTB")
                return
            else:
                email = input("\ncreate a new mail : ")

    print("\nu have to create password with below specifications\n1. need alteast one uppercase and lowercase\n2. need alteast one spl symbol and one numeric ")
    key=input("\ncreate a password : ")
    turns = 3
    while turns>0:
        if len(key) >= 6 and len(key) < 63 and lett_dig_symbol(key):
            print("\nPASSWORD HAS CREATED SUCCESSFULLY...!")
            print("\n----------------------------->>>>>>>")
            break 
        else:
            print("sorry...! u have to create password with below specifications\n1. need alteast one uppercase and lowercase\n2. need alteast one spl symbol and one numeric ")
            turns = turns -1
            if turns == 0:
                print("sorry...! access denined")
                print("\nthanks for choosing WTB")
                return
            else:
                key = input("create a password : ")

    deposit=int(input("\nenter the amount u have to deposit : "))
    accounts[-1].update({"mail":email})
    accounts[-1].update({"password":key})
    accounts[-1].update({"amount":deposit})
    print("Your Account is Sucessfully created.....\n\nif u need to access ur account... make sign in..")
    acc_created=input("r u want to sign in..? [yes or no] : ").lower()
    if acc_created=="yes":
        print("\n")
        sign_in()
    elif acc_created=="no":
        print("thanks for choosing WTB")
        return

entering=input("please... login to access ur account [sign in (or) sign up] : ").lower()

if entering=="sign in" or entering=="signin":
    sign_in()
elif entering=="sign up" or entering=="signup":
    sign_up()
else:
    print("invalid input")
    print("thanks for choosing WTB")







