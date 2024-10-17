'''
    Simple definition and use of an object 

    This script define a class Employee and shows how to 
    use some of their methods.
'''

import sys 

class Employee(object):
    '''
        Employee simple abstraction class
    '''

    def __init__(self):
        '''
            Class constructor
        '''
        self.name = ""
        self.salary = 0.0
        self.area = ""
        self.id = -1

    '''
        Setters definition 
    '''

    def setName(self, iname:str) -> None:
        self.name = iname

    def setSalary(self, cSalary:float) -> None:
        self.salary = cSalary

    def setArea(self, cArea:float) -> None:
        self.area = cArea
    
    def setId(self, id:int) -> None:
        self.id = id

    '''
        Getters definition 
    '''

    def getName(self) -> str:
        return self.name
    
    def getId(self) -> int:
        return self.id

    def getSalary(self) -> float:
        return self.salary
    
    '''
        Other methods definition
    '''

    def display(self):
        print("***********")
        print(f'Employee name: {self.name}\nEmployee Salary: {self.salary}')
        print(f'Employee area: {self.area}')
        print('Employee ID: %s' %('Unknown' if self.id <= 0 else str(self.id)))
        print("***********")
    
def main():
    objEmployee = Employee()

    objEmployee.setArea('Agro')
    objEmployee.setSalary(150000)
    objEmployee.setName('Employee 1')

    objEmployee.display()

    return 0 

if __name__ == "__main__":
    sys.exit(main())