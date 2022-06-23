import os

if __name__ == "__main__":
    choice = 0
    while choice!=5:
        os.system("clear")
        print(" Welcome To CRM App",)
        print("*------------------*")
        print("1- Get Customer Data.")
        print("2- List Customer Data.")
        print("3- Save Customer Data.")
        print("4- Load Customer Data.")
        print("5- Exit")
        choice=int(input("Please select an option (1-5): "))
        
        if choice==1:
            os.system("clear")
            name = input("Please type your name: ")
            age = input("Please type your age: ")
            input("press enter to continue ...")
            pass
        elif choice ==2:
            os.system("clear")
            print("Welcome {0}, your age is {1} ".format(name,age))
            input("press enter to continue ...")
        elif choice ==3:
            os.system("clear")
            fileHandler = open("data/crmapp.txt","w+")
            fileHandler.write( name +"\n")
            fileHandler.write(age)
            fileHandler.close()
            """
            save_cust_data()"""
            print("Done saving file")
            input("press enter to continue ...")
        elif choice ==4:
            os.system("clear")
            fileHandler=open("data/crmapp.txt","r")
            content=fileHandler.read()
            linelist=content.splitlines()
            name=linelist[0]
            age=linelist[1]
            print("done loading...")
            input("press enter to continue ...")
        else:
            print("Exit")
            pass
        