class Contacts:
    def __init__(self, name, age, address , birthday, telephone):
        self.name = name
        self.age= age
        self.address = address
        self.birthday = birthday
        self.telephone = telephone
class contact_book:
    def __init__(self):

if __name__ == "__main__":
    ##contactList =["Samuel Attipoe", "19" , "E111 tweed castle leazes", "28/08/2002", "07716548718" ]
    #contact1 = contacts("bill", "17", "sddress", "01/02/0304", "0192837465")
    contactList=[]
    contactList.append(Contacts("bill", "17", "sddress", "01/02/0304", "0192837465"))

    print( contactList[1].name )

    #for i in range(100):
     #   print(contactList[i].name + )