#notes to instructor. please ignore the comments. they are for personal-refferencing only. thank you.

class Bank :

    def __init__ (self): #as amra chai alada alada object er jonno alada alada sob db thakuk #ar constructor er moddhe declare korle, self. diyei declare kora lagbe :)
        #database
        #0th index is not used 
        self.useriddb = [0] #as index tai userid hisebe thakbe... #yet eta lagbe cz ekhane ith index e i pawa gele, bujha jabe user exist kore, delte hoye jai ni. keu delete korle -1 set kore dibo.  
        self.topuserid = 1 #1st user is not created yet. so it is in advanced
        self.passworddb = ['djfh3dsdkf']
        self.namedb = ['0']
        self.phonedb = ['0']
        self.logintokendb = [0] #ith index = 1 means ith userID is logged in. =0 means logged out
        self.amountdb = [0]
        self.loandb = [0] #-100 mane 100 taka loan ache
        self.totalbankbalance = 0 
        self.totalloan = 0
        self.transactionhistory = [['0']] #2D list aka lists of lists
        self.adminiddb = [0]
        self.adminpostdb = ['0']
        self.adminpassworddb = ['dfh398hd']
        self.topadminid = 1
        self.adminlogintokendb = [0]
        self.loanfeature = 1
        



    def UserLogInMenu (self):
        print()
        print("\n==========<<<< BANKING SERVICES : MAIN MENU >>>>==========")
        print("1. Create A New User Account ")
        print("2. Log in To A User Account ")
        print("3. Create An Admin Account")
        print("4. Log in To An Admin Account")        
        print("0. Exit")
        
        print("Choose Your Option: ")
        option = (input())
        return option
    
    def CreateANewAccount (self): #useriddb, logintokendb, amountdb, loandb te append kore dewa lagbe
        print("Enter Your Email: ")
        accholdername = input()
        self.namedb.append(accholdername)
        #print("Enter Your Phone Number:")
        #phone = input()
        #self.phonedb.append(phone) #idea: later phone number checker implement 
        print("Create A Password:")
        password = input()
        self.passworddb.append(password) #idea: later password checker implement
        self.useriddb.append(self.topuserid)
        self.logintokendb.append(0)
        self.amountdb.append(0)
        self.loandb.append(0)
        self.transactionhistory.append([])
        self.transactionhistory[self.topuserid].append("Account Created")
        print("Your Account Creation is Successful! Your UserID is", self.topuserid, ". Please Remember Your userID and Password." ) #topuserid dile hobe na. self.topuserid dite hobe
        self.topuserid += 1 #account creation successfull

    def userDashBoard(self):
        print()
        print("======== User Dash Board ========")
        print("1. Deposite Amount ")
        print("2. Withdraw Amount ")
        print("3. Check Balance")
        print("4. Transfer Balance to Another Account")
        print("5. Check Transaction History")
        print("6. Apply for Loan")
        print("7. Log Out and Go Back to Main Menu")
        print("Choose Your Option: ")
        option = (input())
        return option
    
    def adminDashBoard(self):
        print()
        print("======== Admin Dash Board ========")
        print("1. Check Total Avaiable Balance of Bank ")
        print("2. Check Total Loan Amount ")
        print("3. Turn on/off loan feature")
        print("0. Log Out and Go Back to Main Menu")
        print("Choose Your Option: ")
        option = (input())
        return option

    def UserLogIn (self) -> int: 
        passwordmatched = 0
        while (passwordmatched == 0):
        
            try: 
                print("Enter Your userID. Enter 'x' to go back to main menu.")
                id = (input()) 
                if (id == 'x'):
                    return -1
                if (int(id)>=self.topuserid):
                    print("userID not found!")
                    continue
                elif (self.useriddb[int(id)]==-1):
                    print("User has closed this account!")
                    continue  
                elif (self.useriddb[int(id)]== int(id)): #not === id #this is now it was implemented #useriddb te ith userid wala person exist korle i value hisebe thake, 1 na
                    print("Enter Your Password. Press 'x' to go back to main menu.")
                    password = input()
                    if (password == 'x'):
                        return -1
                    if (password == self.passworddb[int(id)]):
                        passwordmatched = 1
                        print("We are logging you in. Hold tight!")
                        self.logintokendb[int(id)] = 1
                        print("Yaa! You are successfully logged in!")
                        return int(id)
                        #self.userDashBoard() #self. diyei userDashBoard ke call dite hobe
                    else:
                        print("Password didn't Matched!")
                else:
                    print("Something Went Wrong : SWW911")
            except:
                print("Invalid Input")
                


    def depositeAmount (self, id):
        print("How much you wanna deposite?")
        try:
            amount = float(input())
            self.amountdb[id] += amount
            self.totalbankbalance+=amount
            self.transactionhistory[id].append(f"{amount} BDT deposited")
            print("Amount deposited successfully")
        except:
            print("Invalid Input")
            
         

    def checkAmount (self, id):
        print(f"Hey {self.namedb[id]}! Your userID is {self.useriddb[id]}. Your current balance is {self.amountdb[id]} BDT only. You have a loan of BDT {self.loandb[id]*-1}")

    def withdrawAmount (self, id):
        print("How much do you want to withdraw?")
        try: 
            amount = float(input())
            if (amount <= self.amountdb[id]):
                if (amount<=self.totalbankbalance):
                    self.amountdb[id] -= amount
                    self.totalbankbalance-=amount
                    self.transactionhistory[id].append(f"{amount} BDT withdrawn")
                    print(f"{amount} BDT withdrawn successfully from your account")
                else:
                    print("Unfortunately bank does not have enough balance. Withdrawn failed due to bankrupcy!")
            else:
                print("You do not have enough balance.")   
        except:
            print("Invalid Input")

    def transferAmount (self, id):
        print("How much do you want to transfer?")
        try:
            amount = float(input())
            if (amount > self.amountdb[id]):
                print("Transfer failed! You do not have enough balance.")
            else:
                print(f"Which account you want {amount} BDT to transfer? Enter userID:")
                receiverID = int(input())
                if (receiverID<self.topuserid and id != receiverID):
                    if (self.useriddb[receiverID] != -1):
                        self.amountdb[id] -= amount
                        self.amountdb[receiverID] += amount
                        self.transactionhistory[id].append(f"{amount} BDT transferred to userID: {receiverID}")
                        self.transactionhistory[receiverID].append(f"{amount} BDT received from userID: {id}")
                        print(f"{amount} BDT transferred to userID:{receiverID} successfully.") 
                    else:
                        print("The receiver has closed his/her account. Transfer failed.")
                        return
                else:
                    print("Either the Receiver userID is not found or you are trying to transfer money to your own account. Transfer failed.")
        except:
            print("Invalid Input")


    def takeLoan (self, id):
        try:
            if (self.loanfeature == 1):
                print("How much you want to take loan?")
                loanamount = float(input())
                if ((self.loandb[id]*-1 + loanamount) > 2*(self.amountdb[id]+self.loandb[id])):
                    print(f"You can only take loan upto {2*(self.amountdb[id]+self.loandb[id])} BDT. You already have a loan of {self.loandb[id]*-1} BDT. Loan request failed.")
                elif (loanamount>self.totalbankbalance):
                    print("Loan request failed. Bank does not have enough balance.")
                else:
                    self.loandb[id] -= loanamount
                    self.amountdb[id] += loanamount 
                    self.totalbankbalance-=loanamount
                    self.totalloan+=loanamount
                    self.transactionhistory[id].append(f"{loanamount} BDT loan taken")
                    print("Loan successfully granted. Loaned amount is added to your account.")
            else:
                print("Currently Bank is Not Accepting Any Loan Request. Loan Featured Is Turned Off.")
        except:
            print("Invalid Input")


    def history (self, id):
        print(self.transactionhistory[id])
        
    def createadminacc (self): #useriddb, logintokendb, amountdb, loandb te append kore dewa lagbe
        print("Enter Your Email: ")
        adminpost = input()
        self.adminpostdb.append(adminpost)
        #print("Enter Your Phone Number:")
        #phone = input()
        #self.phonedb.append(phone) #idea: later phone number checker implement 
        print("Create A Password:")
        password = input()
        self.adminpassworddb.append(password) #idea: later password checker implement
        self.adminiddb.append(self.topadminid)
        self.adminlogintokendb.append(0)
        #self.amountdb.append(0)
        #self.loandb.append(0)
        #self.transactionhistory.append([])
        #self.transactionhistory[self.topuserid].append("Account Created")
        print(f"Admin Account Creation Successful for {adminpost}. Your AdminID is", self.topadminid, ". Please Remember Your AdminID and Password." ) #topuserid dile hobe na. self.topuserid dite hobe
        self.topadminid += 1 #account creation successfull
        
    
    def loginadminacc (self):
        passwordmatched = 0
        while (passwordmatched == 0):
            try:
                print("Enter Your AdminID. Enter '-1' to go back to main menu.")
                id = int(input()) 
                if (id == -1):
                    return -1
                if (id>=self.topadminid):
                    print("AdminID not found!")
                    continue
                elif (self.adminiddb[id]==-1):
                    print("Admin ID deactivated.")
                    continue       
                print("Enter Your Password. Press 'x' to go back to main menu.")
                password = input()
                if (password == 'x'):
                    return -1
                if (password == self.adminpassworddb[id]):
                    passwordmatched = 1
                    print("We are logging you in. Hold tight!")
                    self.adminlogintokendb[id] = 1
                    print("Yaa! You are successfully logged in!")
                    return id
                    #self.userDashBoard() #self. diyei userDashBoard ke call dite hobe
                else:
                    print("Password didn't Matched!")
            except:
                print("Invalid Input")
                
    def loanfeaturecontrol (self):
        status = None
        opposite = None
        oppositenumber = None #function scope
        
        if (self.loanfeature == 1):
            status = "ON"
            opposite = "OFF"
            oppositenumber = 0
        else:
            status = "OFF"
            opposite = "ON"
            oppositenumber = 1
        
        print(f"Currently loan feature of your bank is turned {status}.")
        print("Press 1 to change it. Press 0 to keep it as it is.") 
        opt = (input())
        if (opt == '1'): #taken in character to avoid program crash for hijibiji input
            self.loanfeature = oppositenumber
            print(f"Loan feature is turned {opposite} successfully")
        elif (opt == '0'):
            print(f"Loan feature is turned {status} as it was. No changes have been made.")
        else:
            print("Invalid Input")
            
        
        


obj = Bank()
while (1):
    optionchosen = obj.UserLogInMenu()
    if (optionchosen == '1'):
        obj.CreateANewAccount()
    elif (optionchosen == '2'):
        id = obj.UserLogIn()
        if (id == -1):
            continue
        while (1): 
            if (obj.logintokendb[id] == 1):
                optionfromdashboard = obj.userDashBoard()  
                if (optionfromdashboard == '1'):
                    obj.depositeAmount(id)
                elif (optionfromdashboard == '2'):
                    obj.withdrawAmount(id)
                elif (optionfromdashboard == '3'):
                    obj.checkAmount(id)
                elif (optionfromdashboard == '4'):
                    obj.transferAmount(id)
                elif (optionfromdashboard == '5'):
                    obj.history(id)
                elif (optionfromdashboard == '6'):
                    obj.takeLoan(id)
                elif (optionfromdashboard == '7'):
                    print("We are logging you out. Hold on.")
                    obj.logintokendb[id] = '0'
                    print("You are logged out successfully.")
                    break
                else :
                    print("Invalid Input. Check and try again.")


    elif (optionchosen == '0'):
        break
    elif (optionchosen == '3'):
        obj.createadminacc()
        
        
    #admin control 
    elif (optionchosen == '4'):
        id = obj.loginadminacc()
        if (id == -1):
            continue
        while (1): 
            if (obj.adminlogintokendb[id] == 1):
                optionfromdashboard = obj.adminDashBoard()  
                if (optionfromdashboard == '1'):
                    print(f"Currently Total Avaiable Balance of Your Bank is {obj.totalbankbalance} BDT")
                elif (optionfromdashboard == '2'):
                    print(f"Total Loan Amount from Your Bank is {obj.totalloan} BDT")
                elif (optionfromdashboard == '3'):
                    obj.loanfeaturecontrol()
                elif (optionfromdashboard == '0'):
                    print("We are logging you out. Hold on.")
                    obj.adminlogintokendb[id] = '0'
                    print("You are logged out successfully.")
                    break
                else :
                    print("Invalid Input. Check and try again.")
        
        
        
        
        
    else :
        print("Invalid Input!") #character input dile crash korche. invalid aste hobe. ejonno maybe string e ene check korte hoeb. eta sob gula option er kkhetreo true


#else block like admintoken failed etc
#implement: check je kon user er koto balance or loan ache from admin panel. or kon kon user loan niyeche etc
#implement: repay loan opiton from user panel 
#update: coming back from account creation like press x to go to main menu
#implement: admin dekhte cai ke ke kototaka withdraw/deposite/loan koreche tahole? bankalltransactionhistory()
#SOLVED: userlogin, adminlogin e keu jodi userID er jaigai character input dey, error khabe...
#fix: 0 userID/adminID wala lok password diye aceess korte parbe!
#SOLVED: deposite, withdraw er moddhe character taka input dile error khave
#implement: deleteID , deactivateadminID not implemented
#update: empty email and password dileo create account kora jacche
