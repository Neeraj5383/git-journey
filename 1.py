cur_bal = 5000
x = "neeraj"
y = "neeraj123"

print("Select option")
print("1: Signup")
print("2: Signin")
user_sign = input("Enter option : ")
match user_sign:
    case "1":
        new_user = input("Enter username : ")
        new_pass = input("Enter password : ")
        print("your username is ",new_user," and passward is ", new_pass)
    case "2":
         user = input("Enter username : ")
         password = input("Enter passward : ")
         if x == user and y == password:
             print("Select option")
             print("1 : Check your balance")
             print("2 : Do your transition")
             print("3 : Apply for loan")
             print("4 : Signout")

             user_input = input("Enter option : ")

             match user_input :
                 case "1":
                     print("Your balance is ", cur_bal)

                 case "2":
                     print("Enter option")
                     print("1 : Debit")
                     print("2 : credit")
                     deb_cre = input("Enter your option : ")

                     match deb_cre:
                         case "1":
                             debit_amount = int(input("Enter your amount : "))
                             if debit_amount <= cur_bal:
                                 cur_bal = cur_bal - debit_amount 
                                 print("Your current balance is ", cur_bal)
                             else:
                                 print("Insufficient balance")
                                 print("Your current balance is ", cur_bal)

                         case "2":
                                credit_amount = int(input("Enter your amount : "))
                                cur_bal = credit_amount + cur_bal
                                print("Your current balance is ", cur_bal)
                         case _:
                                print("Wrong selection!!!")

                  
                 case "3":
                        print("appling for loan")
                        print("Select option")
                        print("1 : Home Loan")
                        print("2 : Personal Loan")
                        opt = input("Enter Option : ")
                        match opt:
                            case "1":
                                print("Home Loan")
                                print("Sanction Loan Amount is ", cur_bal * 30)
                                print("Interest on loan amount is 9%")
                                loan_amount = int(input("Enter loan amount : "))
                                if loan_amount <= cur_bal * 30 and loan_amount > 0:
                                    cur_bal += loan_amount
                                    interest = (9 /100) * loan_amount
                                    mnth = interest / 12
                                    
                                    print("Interest on loan amount : ", interest)
                                    print("Monthly Interest : ", mnth)
                                    print("Total Amount to pay : ", interest + loan_amount)
                                    print("Total balance : ", cur_bal, "\n")
                                    print("Select option")
                                    print("1: yes")
                                    print("2: No")
                                    yes_no = input("Enter Option")
                                    match yes_no:
                                        case "1":
                                            print("Loan Applied Successfully!!!")
                                        case "2":
                                            print("Loan Applied Failed")
                                        case _:
                                            print("Wrong Option")

                                else:
                                    print("Your loan amount more than sanctioned amount")
                                    print("Your Not Eligible For Loan")
                                    
                            case "2":
                                print("Personal Loan")
                                print("Sanction Loan Amount is ", cur_bal * 10)
                                print("Interest on loan amount is 15%")
                                loan_amount = int(input("Enter Loan Amount : "))
                                if loan_amount <= cur_bal * 10 and loan_amount > 0:
                                    cur_bal += loan_amount
                                    interest = (15 /100) * loan_amount
                                    mnth = interest / 12
                                    
                                    print("Interest on loan amount : ", interest)
                                    print("Monthly Interest : ", mnth)
                                    print("Total Amount to pay : ", interest + loan_amount)
                                    print("Total balance : ", cur_bal, "\n")
                                    print("Select option")
                                    print("1: yes")
                                    print("2: No")
                                    yes_no = input("Enter Option")
                                    match yes_no:
                                        case "1":
                                            print("Loan Applied Successfully!!!")
                                        case "2":
                                            print("Loan Applied Failed")
                                        case _:
                                            print("Wrong Option")
                                    
                                else:
                                    print("Not Eligible for loan")   

                                
                            case _:
                                print("Wrong Selection")

                 case "4":
                        print("Signout")
                 case _:
                        print("Wrong selection!!!")
         else:
             print("Wrong username and password")
    case _:
        print("Wrong selection!!!")
