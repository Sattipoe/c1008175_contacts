import sys
import sysconfig



class Contacts:
    def __init__(self, name, address , birthday, telephone):
        """
        initialize the Contacts class and takes in 4 variables Name, Address, Birthday, Telephone
        """
        self.name = name
        self.address = address
        self.birthday = birthday
        self.telephone = telephone


contact_list = list()

# opens the contact file and reads it
f = open('contacts.txt', 'r')
contact_list = f.readlines()#readlines seperated it into lines
f.close()





user_input = ""#to be able to give the user input a variable late




while user_input != "e":
        print ("options = ")
        print("1 = enter contact information")
        print ("2 = display all contacts")
        print ("e = close program ")
        print("3 = search for a contact ")#interface that shows up when code is ran
        user_input = input("select option: ")#input allows the user to input something



        if user_input == "1":
            print("enter contact information")


            name = input( "name = ")
            address = input("Address =  ")
            birthday = input(" Birthday = ")
            telephone = input(" Telephone number = ")# used to alllow user to enter contact info

            person = [",", name, ",", address, ",", birthday, ",", telephone]
            with open('contacts.txt', 'a') as f:
                for persons in person:
                    f.write(persons.lower())
                f.write('\n')#opens the contacts text after formatting the user information that has been inputed and writes it back to the txt file

            print ("details have been stored ")
        elif user_input == "2":
            file = open('contacts.txt', 'r')
            data = file.read()
            file.close()
            print(data)# opens the current txt file and prints out all the information

        elif user_input == "3":
            search = input(" enter the name/address/number/birthday of the contact you want to find: ")
            count=-1
            for line in contact_list:
                count+=1 #gives the contacts a number to allow differentiation

                if search.lower() in line:# if the search is in the line print the entire line also lower forces it into lower case
                    print(str(count) + " "+ line) # changes the count into a string
                    edit = input("would you like to edit the contact")
                    delete = input("would you like to delete this Contact")
                    if edit == "yes":

                        new_input = input("Enter new details seperated by , : ")
                        f = open('contacts.txt', 'r')
                        contact_list = f.readlines()
                        f.close()

                        contact_list[count] = new_input #contact_list[count] is the thing holding the data that has been searched
                        f = open('contacts.txt', 'w')
                        for i in range(len(contact_list)):
                            f.write(contact_list[i])
                        f.close()
                        delete = input("would you like to delete this Contact")
                    if delete == "yes":
                        f = open("contacts.txt","r")
                        contact_list = f.readlines()
                        f.close()

                        contact_list.pop(count)

                        f = open('contacts.txt', 'w')
                        for i in range(len(contact_list)):
                            f.write(contact_list[i])
                        f.close()

#  used code from https://www.delftstack.com/howto/python/python-replace-line-in-file/#:~:text=Use%20the%20for%20Loop%20Along%20With%20the%20replace,Replace%20the%20Text%20in%20a%20Line%20in%20Pytho
# to help with the process of replacing and updating code
