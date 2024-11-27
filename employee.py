class Employee:

    def __init__(self, name, id, designation, age, department):
        self.__employeeId = id
        self.__name = name
        self.__designation = designation
        self.__department = department

    # Getter for access private objects
    def getEmployeeId(self):
        self.__employeeId
    def getname(self):
        self.__name
    def getdesignation(self):
        self.__designation
    def getdepartment(self):
        self.__department
    
    # Setter for set value in private objects

    def setEmployeeId(self, id):
        self.__employeeId = id
    def setname(self, name):
        self.__name = name
    def setdesignation(self, designation):
        self.__designation = designation
    def setdepartment(self, department):
        self.__department = department
    

    def convertTo_string(self):
        return f"{self.__employeeId},{self.__name}, {self.__designation}, {self.__department}"



    


        