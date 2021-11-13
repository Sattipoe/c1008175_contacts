from lib2to3.pgen2.grammar import name


class Contacts:
    def __init__(self, name, address , birthday, telephone):
        self.name = name
        self.address = address
        self.birthday = birthday
        self.telephone = telephone



f = open('contacts.txt', 'r')
contents = f.read().split('\n')
f.close()

##print(contents[1])
    user_input = ""


    print ("press 1 to show all contacts")
    while user_input != "e":
        print ("options = ")
        print("1 = enter contact information")
        print ("2 = display all contacts")
        print ("e = close program ")
        user_input = input("select option: ")
        if user_input == "1":
            print("enter contact information")


            name = input( " First and last name = ")
            address = input("Address =  ")
            birthday = input(" Birthday = ")
            telephone = input(" Telephone number = ")

            person = [name, ", ", address, ",", birthday, ", ", telephone]
            with open('contacts.txt', 'a') as f:
            for persons in person:
            f.write(persons)
            f.write('\n')

            print ("details have been stored ")


##if __name__ == "__main__"
    ##contactList =["Samuel Attipoe", "19" , "E111 tweed castle leazes", "28/08/2002", "07716548718" ]
    #contact1 = contacts("bill", "17", "sddress", "01/02/0304", "0192837465")
    #contactList=[]
    #contactList.append(Contacts("bill", "17", "sddress", "01/02/0304", "0192837465"))

    #print( contactList[1].name )

    #for i in range(100):
     #   print(contactList[i].name + )