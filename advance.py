##############  OOPS ##############





# Encapsulation: To provide the security to data and methods
# access specifier(public, protected, private)


# Private Access specifier
# 1st way: Syntax method
class Hospital:
    hname = "AIIMS"
    __total_doc = 18
    def __init__(self, loc, mail, patient_count):
        self.loc=loc
        self.mail=mail
        self.__patient_count=patient_count
    
    @classmethod
    def disp(cls):
        print(cls.hname, cls.__total_doc)
    
    def display(self):
        return self.loc,self.mail
         
h1 = Hospital("mumbai", "patient@aiims.com",40)
print(Hospital._Hospital__total_doc)
h1.disp()
print(h1.display())
print(h1._Hospital__patient_count)
# print(Hospital._Hospital__patient_count)  # We can't access __patient_count bcz it belongs to instance of our class not directly class




# 2nd way: Getter and Setter method
class Hospital:
    hname = "AIIMS"
    __total_doc = 18
    def __init__(self, loc, mail, patient_count):
        self.loc=loc
        self.mail=mail
        self.__patient_count=patient_count
    
    @classmethod
    def get_details(cls):
        return cls.hname, cls.__total_doc
    
    @classmethod
    def setDoc(cls, new):
        cls.__total_doc=new
    
    def get_patientDetails(self):
        return self.loc, self.mail, self.__patient_count
    
    def set_UpdatePatient(self,new):
        self.__patient_count=new
    
H1 = Hospital("mumbai", "patient@aiims.com", 40)
# print(H1.get_details())
H1.setDoc(20)
print(H1.get_details())
# print(H1.get_patientDetails())
H1.set_UpdatePatient(45)
print(H1.get_patientDetails())



# 3rd Way : property method
class Hospital:
    hname = "AIIMS"
    __total_doc = 18
    def __init__(self, loc, mail, patient_count):
        self.loc=loc
        self.mail=mail
        self.__patient_count=patient_count
    
    @property
    def details(self):
        return self.loc, self.mail, self.__patient_count
    
    @details.setter
    def details(self, new):
        self.__patient_count = new
H1 = Hospital("mumbai", "patient@aiims.com", 40)
print(H1.details)
H1.details=60
print(H1.details)
    

# Difference between getter setter and property method:
# In getter setter method we have to call method to get and set the value 
# but in property method we can directly access the attribute to get and set the value