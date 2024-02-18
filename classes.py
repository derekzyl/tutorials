

class Precious:

    
    def __init__(self, my_religion, my_school, my_tribe):


        self.my_school = my_school
        self.my_religion = my_religion
        self.my_tribe = my_tribe

    def school(self):
        print(self.my_school)
    def tribe(self):
        print(self.my_tribe)
    

    def religion(self):
        print(self.my_religion)


presh = Precious("Christian","Any School", "Igbo")
presh2 = Precious(my_religion="Christian", my_school="Unical", my_tribe="Hausa")
presh2.religion()



class PreciosDaughter(Precious):
    def __init__ (self, dau_school, dau_religion, dau_tribe ):
        Precious.__init__(self,my_religion=dau_religion,my_school=dau_school, my_tribe=dau_tribe)



daughter = PreciosDaughter(dau_religion="Jew", dau_school="Uniben", dau_tribe= "Birom")

daughter.religion()
        