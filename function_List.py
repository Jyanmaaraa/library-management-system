#importing sys, datetime module from python
import sys
import datetime #improting  datetime module

#-----------------------main function of program----------------------------------------------------------------------------

def main_Function():
    '''displays  book list table and keep asking for  integer value 1,2,3 from user unless and until valid value is given '''
    
    print("***************************************************************************************************************")
    print("\t\t\t\tWelcome to College Library Management System. ")
    print("***************************************************************************************************************\n")
    dict_display()
    continue_1 = True
    while continue_1 == True:#creating a loop to keep asking a value to user if invalid input is given
        print("\nPlease, Enter '1' to borrow a book.")
        print("Please, Enter '2' to return a book.")
        print("Please, Enter '3' to add a new book.")
        print("Please, Enter '4' to exit.")
        user_Input = input("\nPlease, Enter a value as 1 or 2 or 3 or 4 : ")#asking value 1,2,3 from user which is string datatype 
        if user_Input == str(1):#converting 1 interger to string and comparing wth user input value
            print("\n\n---------------------------------------------------------------------------------------------------------------")
            print("You will now borrow the book :")
            print("---------------------------------------------------------------------------------------------------------------")
            borrow_Function()#borrow_Function method will be invoked if user input value is 1
        elif user_Input == str(2):
            print("\n\n---------------------------------------------------------------------------------------------------------------")
            print("You will now return the book :")
            print("---------------------------------------------------------------------------------------------------------------")
            return_Function()#return_Function method will be invoked if user input value is 2

        elif user_Input == str(3):
            print("\n\n---------------------------------------------------------------------------------------------------------------")
            print("You will now add new books to book stock List :")
            print("---------------------------------------------------------------------------------------------------------------")
            dict_display()
            add_Books()#add_Books method will be invoked if user input value is 3

        elif user_Input == str(4):
            print("\n***************************************************************************************************************")
            print("\t\t\t\tThank you for using our library management system.")
            print("***************************************************************************************************************")
            break#exits the program and loop
        else:
            print("\n\n---------------------------------------------------------------------------------------------------------------")
            print("\t\t\t\tInvalid input!!! Please, provide input value as 1, 2,3 or 4.")
            print("---------------------------------------------------------------------------------------------------------------")
            

#---------------------------------making dictionay data collection form txt file------------------------------------------------------------------
            
def dict_Function():
    ''' creates dictionary collection data type from bookStock txt file'''
    
    file = open("bookStock_list.txt","r")#opening txt file in read mode
    dictionary = {}#creating empty dictionary
    book_ID = 0
    for line in file:#iterates all line as string from txt file one line by line
        book_ID += 1#increment by 1 each time
        line = line.replace("\n","").split(',')#replace next line with empty space in string word and split the string word on the basis of commas
        dictionary[str(book_ID)] = line # adding book ID as key and  value list of sting as to dictionary
    file.close()#closing file
    return dictionary

#------------------------------------making list of book id--------------------------------------------------------------- 
def allKey_List():
    '''creates a list collection data type which stores all book ID as keys of dictionary'''
    
    key_List = []#creating empty lsit
    dictionary = dict_Function()#assiging return value of method to dictionary variable
    for key in dictionary.keys():#iterates all key from dictionary one by one
        key_List.append(key)# adding key to list
    return key_List#returns list

#------------------------------------making list of book name--------------------------------------------------------------- 
def list_BookName():
    '''creates a list collection data type which stores all book name value from dictionary'''
    
    bookName_List = []#creating empty lsit
    dictionary = dict_Function()#assiging return value of method to dictionary variable
    for value in dictionary.values():#iterates all book name from dictionary one by one
        bookName_List.append(value[0].lower())# adding book name from dictionary to list
    return bookName_List#returns list



#--------------------------------displaying book table------------------------------------------------------------------- 
def dict_display():
    '''diplays list of book in a table'''
    
    print("---------------------------------------------------------------------------------------------------------------")
    print("Book ID\t\t|" + " \tBook Name \t\t|"  + " \tAuthor \t\t|" + "\tQuantity \t| " + "\tPrice" )
    print("---------------------------------------------------------------------------------------------------------------")
    display_dictioanry = dict_Function()
    for key,value in display_dictioanry.items():#iterates all key,value from dictionary one by one
        print(key + "\t\t|\t" + value[0] + "\t\t|\t" + value[1] + "\t|\t" + value[2] + "\t\t|\t" + value[3])
    print("---------------------------------------------------------------------------------------------------------------\n")


#------------------------borrow function of program----------------------------------------------------------------------------

def borrow_Function():
    '''handles all operation for browwing book by integrating all methods for borrow'''
    
    global costumerName,borrowedBook_ID_List#declaring variable as global
    dict_display()#calling method to display booklist table
    borrowedBook_ID_List = []#creating empty list
    borrow = True#assigning boolean value to variable
    continuty = False
    while continuty  == False:#giving condition for execuation of while loop
        costumerName = input("Please, Enter the borrower's name : ").replace(":","")#asking costumer name and replacing colon to empty string
        if costumerName == "" : #checking value of costumer name is empty
            print("----------------------------------------------------------------------------------------------------------------------------")
            print("\t\t\tName cannot be left empty!!! Please, Enter the borrower's name. ")
            print("----------------------------------------------------------------------------------------------------------------------------\n")
        else:
            continuty  = True
            validation_BorrowedbookID()#calling validation_BorrowedbookID 
            while borrow == True:
                print("\nDo you want to borrow more books ?")
                continuty = input("If you want then Please, Enter 'Y' for YES and 'N' for NO to borrow more books : ").lower()
                print("\n")
                if continuty == "y" :
                    validation_BorrowedbookID()#validation_BorrowedbookID method will be invoked if user input  is y
                elif continuty == "n":
                     borrow = False
                     print("\n----------------------------------------------------------------------------------------------------------------------------")
                     print("\tUpdated books list in library after borrowing books :  ")
                     print("----------------------------------------------------------------------------------------------------------------------------")
                     dict_display()
                     borrowDetails_Write_ReadOp()#borrowDetails_Write_ReadOp method will be invoked if user input  is n
                     print("\n***************************************************************************************************************")
                     print("\t\t\t\tThank you for using our library management system.")
                     print("***************************************************************************************************************")     
                else:
                    print("\n---------------------------------------------------------------------------------------------------------------")
                    print("\t\tInvalid Input!!! Please, Provide 'Y' for YES and 'N' for NO to borrow more books. ")
                    print("---------------------------------------------------------------------------------------------------------------")


def validation_BorrowedbookID():
    '''Handels validation operation of borrowed book ID provided by user'''
    date_Borrow = datetime.datetime.now().strftime("%y-%m-%d,%a")
    time_Borrow = datetime.datetime.now().strftime("%H:%M")
    
    bookID_List = allKey_List()#assiging return value of allKey_List method to variable
    dictionary = dict_Function()#assiging return value of dict_Function method to variable
    userInput_BookID = input("Enter book ID you want to borrow : ")
    if userInput_BookID in bookID_List:##checking condition to allow execution if user input book id is in list 
        if userInput_BookID not in borrowedBook_ID_List:#checking condition to allow execution if user input book id is not in list 
            if(int(dictionary[userInput_BookID][2]) > 0):#checking in quantity of book is greater than 0 
                print("\n***************************************************************************************************************")
                print(" \t\t\t\t\tThis Book is avilable for borrow.")
                print("***************************************************************************************************************")
                print("Book Name\t\t|" + " \tPrice \t\t|"  + " \tDate of Borrow \t\t|" + "\tTime of Borrow ")
                print("---------------------------------------------------------------------------------------------------------------")
                #prints book name,price,date,weekdays and time of borrow
                print(dictionary[userInput_BookID][0] + "\t\t|\t" + dictionary[userInput_BookID][3] + "\t\t|\t" + str(date_Borrow) + "\t\t|\t" + str(time_Borrow) )
                borrowedBook_ID_List.append(userInput_BookID)#adding user input book id in list
                updateBorrow_File()#calling updateBorrow_File method
            else:
                print("\n---------------------------------------------------------------------------------------------------------------")
                print(" \t\t\tBook is not available for now. Please, Select another book from the stock.")
                print("---------------------------------------------------------------------------------------------------------------\n")
                validation_BorrowedbookID()#calling validation_BorrowedbookID method
        else:
            print("\n---------------------------------------------------------------------------------------------------------------")
            print(" \t\tThis book is already borrowed by you. Please, select another book from the stock.")
            print("---------------------------------------------------------------------------------------------------------------\n")
            validation_BorrowedbookID()#calling validation_BorrowedbookID method      
    else:
        print("\n---------------------------------------------------------------------------------------------------------------")
        print("\t\t\tInvalid book Id!!! Please, provide valid Book ID from above book table.")
        print("---------------------------------------------------------------------------------------------------------------\n")
        validation_BorrowedbookID()


def updateBorrow_File():
     '''handles writing update of borrowing books detais with updated quantitiy in txt file '''
     bookID_List = allKey_List()
     dictionary = dict_Function()
     file = open("bookStock_list.txt","w")#opening txt file in write mode
     for key,value in dictionary.items():#iterates all key,value from dictionary one by one
          if key in borrowedBook_ID_List[-1]:#checking if value in last index of list matches key value
               newQuantity = int(value[2]) - 1#converting string value of value at index 2 in to integer, subtacting 1 from it and assingin to variable
               if key == bookID_List[-1]:
                   file.write(value[0] + "," + value[1] + "," + str(newQuantity)+ "," + value[3])# writing in to txt file with update quantity value
               else:
                   file.write(value[0] + "," + value[1] + "," + str(newQuantity)+ "," + value[3] + "\n")
          else:
              if key == bookID_List[-1]:
                  file.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3])#writing same old value to txt file
              else:
                  file.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n")            
     file.close()#closing file

     
def costBorrow_book():
    '''calculates the total amount to be paid for borrowing books'''
    
    dictionary = dict_Function()
    totalcost = 0
    for key in borrowedBook_ID_List: #iterates all key from list one by one 
        rate = float(dictionary[key][3].replace("$",""))#replacing $ sign of value at index 3 in dictionary value list(price)and assing to varaible as float datatype
        totalcost += rate # adding rate for calculating total        
    total_cost = "$" + str(totalcost)#converting total cost value to string and adding $ sign to sting value
    return total_cost#returns the value of total_cost


def borrowDetails_Write_ReadOp():
    '''handles writing operation for generating bill as txt file and reading operation of same txt file '''
    
    dictionary = dict_Function()
    date_Borrow = datetime.datetime.now().strftime("%y-%m-%d,%a")
    time_Borrow = datetime.datetime.now().strftime("%H:%M")
    minute_Value = str(datetime.datetime.now().minute)#getting only minute from datetime module and converting it in to string
    microsec_Value = str(datetime.datetime.now().microsecond)#getting only microsecond from datetime module and converting it in to string
    unique_fileName = costumerName + minute_Value + microsec_Value #creating unique file name by concatenating name,minute and microsecond value
    borrow_File = open(str(unique_fileName) + "B" + ".txt","w") #creating a txt fle with unique file name 
    borrow_File.write("***************************************************************************************************************\n")
    borrow_File.write(" \t\t\t\t\t\tCustumer Borrow Books Details\n")
    borrow_File.write("***************************************************************************************************************\n")
    borrow_File.write("\n---------------------------------------------------------------------------------------------------------------\n")
    borrow_File.write("Costumer Name  \t\t|" + "\tBook Name\t|"  + "\tBorrowed Date\t|" + "\tBorrowed Time\t| " + "\tPrice" + "\n")
    borrow_File.write("---------------------------------------------------------------------------------------------------------------\n")
    borrow_File.write(costumerName)#writing costumer name in txt file
    for key in borrowedBook_ID_List:#iterates all key from list one by one
        #writing book name,date,time and price in txt file
        borrow_File.write("\t\t|\t" + dictionary[key][0] + "\t|\t"+ str(date_Borrow) + "\t|\t" + str(time_Borrow) + "\t\t|\t" + dictionary[key][3]+ "\n")
        borrow_File.write("\t")#creates empty space
    borrow_File.write("\n---------------------------------------------------------------------------------------------------------------\n")
    borrow_File.write( "\t\t\t\t\t\t\t\t\t\tTotal Amount\t| " + "\t" + costBorrow_book() + "\n")#writing total cost for books borrowed
    borrow_File.write("---------------------------------------------------------------------------------------------------------------")
    borrow_File.close()
    borrow_File = open(str(unique_fileName) + "B" + ".txt","r")#opening and reading same file which is written above for custumer bill
    print(borrow_File.read())#reading txt file content line by line as single string
    borrow_File.close()#closing file

#-----------------------Handels return Function of program----------------------------------------------------------------------------
    
def return_Function():
    '''handles all operation for returning book by integrating all methods for return'''
    
    global costumerName,returnBooks_Id,days #declaring variable as global
    dict_display()
    returnBooks_Id = []#creating empty list
    days = []#creating empty list
    return_book = False#assigning boolean value to variable
    name = False
    while name == False:
        costumerName = input("Please, Enter the returner's name : ").replace(":","")#asking costumer name and replacing colon to empty string
        if costumerName == "" : #checking value of costumer name is empty
            print("----------------------------------------------------------------------------------------------------------------------------")
            print("\t\t\tName cannot be left empty!!! Please, Enter the returner's name. ")
            print("----------------------------------------------------------------------------------------------------------------------------\n")
        else:
            name = True#boolean value for exiting while loop
            validation_ReturnBookID()#calling validation_ReturnBookID method
            while return_book == False:
                print("\nDo you want to return more books ?")
                continuty = input("If you want then Enter 'Y' for YES and 'N' for NO to return more books : ").lower()
                print("\n")
                if continuty == "y" :
                    validation_ReturnBookID()#validation_ReturnBookID method will be invoked if user input  is y
                elif continuty == "n":
                    return_book = True#boolean value for exiting while loop
                    print("\n----------------------------------------------------------------------------------------------------------------------------")
                    print("\tUpdated books list in library after returning books :  ")
                    print("----------------------------------------------------------------------------------------------------------------------------")
                    dict_display()
                    returnDetails_Write_ReadOp()#returnDetails_Write_ReadOp method will be invoked if user input  is n
                    print("\n****************************************************************************************************************************")
                    print("\t\t\t\tThank you for using our library management system.")
                    print("****************************************************************************************************************************")
                else:
                    print("\n----------------------------------------------------------------------------------------------------------------------------")
                    print("Invalid Input!!! Please Provide 'Y' for YES and 'N' for NO to return books.. ")
                    print("----------------------------------------------------------------------------------------------------------------------------")

    
def validation_ReturnBookID():
    '''Handels validation operation of borrowed book ID provided by user'''
    
    bookID_List = allKey_List()#assiging return value of allKey_List method to variable
    dictionary = dict_Function()#assiging return value of dict_Function method to variable
    userInput_BookID = input("Enter book ID you want to return : ")
     
    if userInput_BookID in bookID_List:#checking condition to allow execution if user input book id is in list
        if userInput_BookID not in returnBooks_Id:#checking condition to allow execution if user input book id is not in list
            returnBooks_Id.append(userInput_BookID)#adding user input book id in list 
            selected = False#assigning boolean value to variable
            while selected == False:
                try :#handing ValueError exception using try except block 
                    totalDays_Borrowed = int(input("Enter the numbers of days you borrowed a book : "))#taking integer number from user
                    if totalDays_Borrowed > 0:
                        selected = True#boolean value for exiting while loop
                        days.append(totalDays_Borrowed)#adding user input day value in list 
                        updateReturn_File()#calling updateReturn_File method
                        print("\n---------------------------------------------------------------------------------------------------------------")
                        print("This book is successfully returned by you.")
                        print("---------------------------------------------------------------------------------------------------------------\n")
                        
                    else:
                        print("\n---------------------------------------------------------------------------------------------------------------")
                        print("Invalid input!!! Please, provide days in positive number.")
                        print("---------------------------------------------------------------------------------------------------------------\n")
                        
                except:
                    print("\n---------------------------------------------------------------------------------------------------------------")
                    print("Invalid input!!! Please, provide days in number.")
                    print("---------------------------------------------------------------------------------------------------------------\n")
        else:
            print("\n---------------------------------------------------------------------------------------------------------------")
            print("\tThis book is already returned by you.Please, provide another Book ID to return a book.")
            print("---------------------------------------------------------------------------------------------------------------\n")
            validation_ReturnBookID()#calling validation_ReturnBookID method
    else:
        print("\n---------------------------------------------------------------------------------------------------------------")
        print("\t\t\tInvalid book ID!!! Please, provide a valid book ID from above book table.")
        print("---------------------------------------------------------------------------------------------------------------\n")
        validation_ReturnBookID()#calling validation_ReturnBookID method
        

def updateReturn_File():
     '''handles writing update of borrowing books detais with updated quantitiy in txt file '''
     bookID_List = allKey_List()
     dictionary = dict_Function()
     file = open("bookStock_list.txt","w")#opening txt file in write mode
     for key,value in dictionary.items():#iterates all key,value from dictionary one by one
          if key in returnBooks_Id[-1]:#checking if value in last index of list matches key value
               newQuantity = int(value[2]) + 1#converting string value of value at index 2 in to integer, adding 1 to it and assingin to variable
               if key == bookID_List[-1]: 
                   file.write(value[0] + "," + value[1] + "," + str(newQuantity)+ "," + value[3])#writing in to txt file with update quantity value
               else:
                   file.write(value[0] + "," + value[1] + "," + str(newQuantity)+ "," + value[3] + "\n")
          else:
              if key == bookID_List[-1]:
                  file.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3])#writing same old value to txt file
              else:
                  file.write(value[0] + "," + value[1] + "," + value[2] + "," + value[3] + "\n")#writing same old value to txt file
     file.close()#closing file
     

def returnDetails_Write_ReadOp():
    '''handles writing operation for generating return bill as txt file and reading operation of same txt file '''
    dictionary = dict_Function()
    date_Return = datetime.datetime.now().strftime("%y-%m-%d,%a")
    time_Return = datetime.datetime.now().strftime("%H:%M")
    minute_Value = str(datetime.datetime.now().minute)#getting only minute from datetime module and converting it in to string
    microsec_Value = str(datetime.datetime.now().microsecond)#getting only microsecond from datetime module and converting it in to string
    unique_fileName = costumerName + minute_Value + microsec_Value#creating unique file name by concatenating name,minute and microsecond value
    i = 0#acting as counter 
    return_File = open(str(unique_fileName) + "R" + ".txt","w")#creating a txt fle with unique file name 
    return_File.write("****************************************************************************************************************************\n")
    return_File.write(" \t\t\t\t\tCustumer Return Books Details\n")
    return_File.write("****************************************************************************************************************************\n")
    return_File.write("\n----------------------------------------------------------------------------------------------------------------------------\n")
    return_File.write("Costumer Name \t\t|" + "\tBook Name\t|"  + "\tRetrun Date\t|" + "\tRetrun Time\t| " + "\tTotal Borrowed Days" + "\n")
    return_File.write("----------------------------------------------------------------------------------------------------------------------------\n")
    return_File.write(costumerName)#writing costumer name in txt file
    for key in returnBooks_Id:#iterates all key from list one by one
        #writing book name,date,time and lending days in txt file
        return_File.write("\t\t|\t" + dictionary[key][0] + "\t|\t"+ str(date_Return) + "\t|\t" + str(time_Return) + "\t\t|\t" + str(days[i])+ "\n")
        return_File.write("\t")#creates empty space
        i += 1
    return_File.write("\n----------------------------------------------------------------------------------------------------------------------------\n")
    return_File.write( "\t\t\t\t\t\t\t\t\t\tTotal Fine\t| " + "\t" + cal_Fine() + "\n")#writing total fine for late return of books
    return_File.write("----------------------------------------------------------------------------------------------------------------------------\n")
    return_File.write("Note : fine is charged 5% of total cost of each book per extra days.\n")
    return_File.write("       Fine will be applicable after only exceeding over 10 days.\n")
    return_File.write("****************************************************************************************************************************\n")
    return_File.close()#closing file
    return_File = open(str(unique_fileName) + "R" + ".txt","r")#opening and reading same file which is written above for custumer bill
    print(return_File.read())#reading txt file content line by line as single string
    return_File.close()#closing file

             
def cal_Fine():
    '''calculates the total fine to be paid for late returning of  books'''
    
    dictionary = dict_Function()
    totalFine = 0
    noCharge_duration = 10#defining maximum days for no fine charge
    i = 0#setting counter for index
    for key in returnBooks_Id:#iterates all key from list one by one 
        rate = float(dictionary[key][3].replace("$",""))#replacing $ sign of value at index 3 in dictionary value list(price)and assing to varaible as float datatype
        borrow_days = days[i]#iterating each days value one by one and assigning to variable
        if borrow_days > noCharge_duration:#checking if borrow days exceeds charge less duration in days
            extra_Days = borrow_days - noCharge_duration#claculating fineable days which are over 10 days
            fine = 0.05 * rate * extra_Days#fine is charged 5% of total cost of each book per extra days
            totalFine += fine#adding rate for calculating total
        else:
             fine = 0#setting fine to zero if lending days is less than 10
             totalFine += fine
        i += 1#incrementing counter value by 1
    totalFine_Amount = "$" + str(round(totalFine,2))#converting totalFine value to string and adding $ sign to sting value and rounding digit up to 2 
    return totalFine_Amount#returns the value of totalFine_Amount
        
                
        
#-------------------adding new books to book stock list---------------------------------------------------------------------------------------------
def add_Books():
    '''handels adding operation of book in book stck list.'''
    global book_Name#defining global variable
    bookName = list_BookName()
    print("\n")
    bookName_NotEmpty =  False
    while bookName_NotEmpty == False:
        book_Name = input("Please, provide the book name : ")
        if book_Name == "":
            print("\n---------------------------------------------------------------------------------------------------------------")
            print("\tBook name cannot be left empty, Please provide the book  name.")
            print("---------------------------------------------------------------------------------------------------------------\n")
        else:
            if book_Name.lower() not in bookName:#coverting string value of book_Name into lower case and checking in the list
                bookName_NotEmpty =  True
                userInput()#calling method
                add_Write()
                print("\n---------------------------------------------------------------------------------------------------------------")
                print("This book is successfully added to book list.")
                print("---------------------------------------------------------------------------------------------------------------\n")
                count = True
                while count == True:
                    print("\nDo you want to add more books ?")
                    answer = input("Please, provide 'Y' for Yes and 'N' for No to add more books : ").lower()
                    print("\n")
                    if answer == "y":
                        add_Books()
                        count = False
                    elif answer == "n":
                        count = False
                        print("\n--------------------------------------------------------------------------------------------------------------------")
                        print("\tUpdated books list in library after adding books :  ")
                        print("--------------------------------------------------------------------------------------------------------------------")
                        dict_display()
                    else:
                        print("\n---------------------------------------------------------------------------------------------------------------")
                        print("Invalid input!!! please, Provide 'Y' for Yes and 'No' for No.")
                        print("---------------------------------------------------------------------------------------------------------------\n")
                          
            else:
                print("\n---------------------------------------------------------------------------------------------------------------")
                print("\tThis book is already in book Stock list.Please, provide another Book Name to add book.")
                print("---------------------------------------------------------------------------------------------------------------\n")
                              
        
def add_Write():
    '''handles writing operation for adding new book details in txt file.'''
    file = open("bookStock_list.txt","a")#opening file in append mode
    file.write("\n" + book_Name + "," + book_Author_Name + "," + str(book_Quantity) + "," + "$" + str(book_price))#updating txt file with new book details
    file.close
                
     
def userInput():
    '''handels query operation for getting values from user'''
    global book_Author_Name,book_Quantity,book_price#defining global variable
    AuthorName_NotEmpty = False
    quantityValue_NotInt = True
    bookPrice_NotFloat = True
    while AuthorName_NotEmpty  == False:
        book_Author_Name = input("Please, provide the book author's name : ")
        if book_Author_Name == "":
            print("\n---------------------------------------------------------------------------------------------------------------")
            print("Book author's name cannot be left empty, Please provide the book author's name.")
            print("---------------------------------------------------------------------------------------------------------------\n")
        else:
            AuthorName_NotEmpty  = True        
    while quantityValue_NotInt  == True:
        try:#handing ValueError exception using try except block
            book_Quantity = int(input("Please, provide the book quantity : "))
            if book_Quantity >= 0:
                quantityValue_NotInt  = False
            else:
                print("\n---------------------------------------------------------------------------------------------------------------")
                print("Invalid input!!! Please provide valid quantity and of positive number. ")
                print("---------------------------------------------------------------------------------------------------------------\n")   
        except:
            print("\n---------------------------------------------------------------------------------------------------------------")
            print("Invalid input!!! Please provide quantity in  number. ")
            print("---------------------------------------------------------------------------------------------------------------\n")
    while bookPrice_NotFloat  == True:
        try:#handing ValueError exception using try except block
            book_price = float(input("please, provide the book price : "))
            if book_price > 0:
                bookPrice_NotFloat  = False
            else:
                print("\n---------------------------------------------------------------------------------------------------------------")
                print("Invalid input!!! Please provide valid price and of positive number. ")
                print("---------------------------------------------------------------------------------------------------------------\n")
        except:
            print("\n---------------------------------------------------------------------------------------------------------------")
            print("Invalid input!!! Please provide price in number. ")
            print("---------------------------------------------------------------------------------------------------------------\n")
    return book_Author_Name,book_Quantity,book_price#returns respective value
                
     
  
        
            

         
    


     
    



    
    
      


