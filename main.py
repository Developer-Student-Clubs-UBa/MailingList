
def mailing_list():
    """ this will test for a python file containing and loads names and email  """


    data = readMail()
    for key, value in data.items():

        print(f'{key.capitalize()} :: {data[key]}')
    choices()


    #return mailing_list()


def createmail():
    """ this function creates a new mail into a python file """
    print("CREATE NEW MAIL")
    name = input("enter name: ")
    email = input("enter email: ")
    mode = "a"
    file = "mailList.txt"
    file = open(file, w) #since we are creating mail, mode should be write.
    file.write(f'{name}:{email}\n')
    file.close()
    print('Mail created')
    choices()


def searchmail():
    """ this function uses a key or value of the dictionary from the readmail() function to display a particular address"""
    data = readMail()
    print(' SEARCH A MAIL')
    choice = input('enter name to search a mail by name or email to search by email: ')

    if choice == 'name':
        a_name = input("please enter name to search mail by list: ")
        if a_name in data.values():
            for name in data.keys():
                if name == a_name:
                    print("=====================================")
                    print("                Results              ")
                    print("=====================================")
                    print(f' {name.capitalize()} :: {data[name]}')
        else:
            print("========================")
            print("Name Not found")
            print("========================")

    elif choice == 'email':
        email = input('please enter email search mail by email: ')
        if email in data.values():
          for keys, value in data.items():
              if value == email:
                  u_name = keys
                  print(f' {u_name.capitalize()} :: {data[u_name]}')
        else:
            print("Email Not Found!")
    choices()


def readMail():
    """ this function reads data from the python file into a dictionary"""
    import csv
    fileName = 'mailList.txt'
    accessMode = 'r'

    dict = {}
    lst1 = []
    with open(fileName, accessMode) as myCSVFile:
        myFile = csv.reader(myCSVFile)
        for row in myFile:
            for value in row:
                lst1 = value.split(':')
                dict[lst1[0]] = lst1[1]
    return dict

def choices():
    print('============================================================')
    print('PERFORM OPERATIONS LIKE SEARCH A MAIL OR ADD A MAIL')
    print('0 to quit application')
    print('1 to ADD NEW MAIL')
    print ('2 to SEARCH NEW MAIL')
    print('3 to view all mails')
    print('============================================================')
    choice = input(': ')
    if choice == '1':
        createmail()
    elif choice == '2':
        searchmail()
    elif choice == '3':
        print("All Mails")
        print("============")
        mailing_list()
    elif choice == '0':
        quit()
    else:
        print('unknown application')
        quit()

#mailing_list()
choices()
