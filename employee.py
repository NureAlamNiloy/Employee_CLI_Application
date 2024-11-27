class Employee:

    def __init__(self,  employeeId, name, designation, department):
        self.__employeeId = employeeId
        self.name = name
        self.designation = designation
        self.department = department

    # Getter for access private objects
    def getEmployeeId(self):
        return self.__employeeId
    
    # Setter for set value in private objects
    def setEmployeeId(self, id):
        self.__employeeId = id


class EmployeeManager:

    def __init__(self, employee_data = "employees.txt"):
        self.employee_data = employee_data
        self.employee_list = []
        self.add_employee_list()
    
    #add all data to the employee_list from employees.txt file
    def add_employee_list(self): 
        try:
            with open(self.employee_data, 'r') as data:
                for emp in data:
                    x = emp.strip().split(",")
                    if len(x)<4:
                        continue
                    employeeId, name, designation, department = x
                    self.employee_list.append(Employee(employeeId, name, designation, department))

        except FileNotFoundError:
            print("File have no data or file not found")
        
    # save employee in file from employee_list 
    def save_employee(self):
        #open file as a write mode
        with open(self.employee_data, 'w') as data:
            # add all data from my employee list to the file
            for emp in self.employee_list:
                data.write(f"{emp.getEmployeeId()}, {emp.name.strip()}, {emp.designation.strip()}, {emp.department.strip()}\n")


    def add_employee(self, name, designation, department):
        if name and designation and department:
            employeeId = str(len(self.employee_list) + 1)
            new_employee = Employee(employeeId,name, designation, department)
            self.employee_list.append(new_employee)
            self.save_employee()
            print("Employee added Successfully")
        else:
            print("Provide all info correctly")
    
    def update_employee(self, employeeId, name, designation, department):
        for emp in self.employee_list:
            if emp.getEmployeeId() == employeeId:
                if name:
                    emp.name = name
                if designation:
                    emp.designation = designation
                if department:
                    emp.department = department
                
                self.save_employee()
                print("Employee update successfully")
                return
        
        print("Employee id not found")
    
    # Delete specific Employee 
    def delete_employee(self, employeeId):
        # here I create a new list from previous list and skip the specific employee using list comprehension 
        self.employee_list = [emp for emp in self.employee_list if emp.getEmployeeId() != employeeId]
        self.save_employee()
        return "Specific Employee Delete Successfully"
    
    def view_all_employee(self):
        if self.employee_list:
            for emp in self.employee_list:
                print(f"{emp.getEmployeeId()}, {emp.name}, {emp.designation}, {emp.department}")
        else:
            print("Employee list is empty")
            
    def search_employee(self, name, designation):
        search_list = [emp for emp in self.employee_list if ((name.lower() in emp.name.lower() if name else True) and (designation.lower() in emp.designation.lower() if designation else True))]
        if search_list:
            for emp in search_list:
                print(f"{emp.getEmployeeId()}, {emp.name}, {emp.designation}, {emp.department}")
        else:
            print("Not result matches")

manager = EmployeeManager()

# input 1 for add employee
# input 2 for update employee
# input 3 for Delete employee
# input 4 for view all employee
# input 5 for search employee
output = input("Enter output type = ") 

if output == '1':
    name = input("Enter Employee name: ")
    designation = input("Enter Employee designation: ")
    department = input("Enter Employee department: ")
    manager.add_employee(name,designation,department)

elif output == '2':
    id = input("Enter Employee Id: ")
    name = input("Enter Employee name: ")
    designation = input("Enter Employee designation: ")
    department = input("Enter Employee department: ")
    manager.update_employee(id, name, designation, department)

elif output == "3":
    id = input("Enter Employee Id: ")
    manager.delete_employee(id)  

elif output == "4":
    manager.view_all_employee()

elif output == "5":
    name = input("Enter Employee name: ")
    designation = input("Enter Employee designation: ")
    manager.search_employee(name , designation)

    


        