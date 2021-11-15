from lib2to3.pgen2.grammar import name


class Contacts:
    def __init__(self, name, address , birthday, telephone):
        self.name = name
        self.address = address
        self.birthday = birthday
        self.telephone = telephone


contact_list = list()



f = open('contacts.txt', 'r')
contact_list = f.read()
for lines in contact_list:
    contact_lists = contact_list.split(",")




##print(contents[1])
user_input = ""


while user_input != "e":
        print ("options = ")
        print("1 = enter contact information")
        print ("2 = display all contacts")
        print ("e = close program ")
        print("3 = search for a contact ")
        print("4 = search and edit contacts")
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
        elif user_input == "2":
            file = open('contacts.txt', 'r')
            data = file.read()
            file.close()
            print(data)
        elif user_input == "3":
            file = open('contacts.txt', 'r')
            search = input("enter the name of the contact you want to find :")











##if __name__ == "__main__"
    ##contactList =["Samuel Attipoe", "19" , "E111 tweed castle leazes", "28/08/2002", "07716548718" ]
    #contact1 = contacts("bill", "17", "sddress", "01/02/0304", "0192837465")
    #contactList=[]
    #contactList.append(Contacts("bill", "17", "sddress", "01/02/0304", "0192837465"))

    #print( contactList[1].name )

    #for i in range(100):
     #   print(contactList[i].name + )