'''
 Solution - Calculator 

 :NOTE: This script contain the basic Idea of how to work with 
        classes.  
'''
import os
import sys 

class Operations(object):

    def __init__(self, a:float, b:float, operation:int):
        '''
            :Args:
                :a: float, Value to operate
                :b: float, Value to operate 
                :operation: int, Operation to apply 
        '''
        self._valueA = a 
        self._valueB = b 
        self._operator = operation
        self._result = -1
        self._strOperator = ''
    
    def add(self):
        self._result = self._valueA + self._valueB

    def substract(self):
        self._result = self._valueA - self._valueB

    def multiplication(self):
        self._result = self._valueA * self._valueB

    def division(self):
        self._result = self._valueA / self._valueB

    def __applyOperation(self):
        if self._operator == 1:
            self.add()
            self._strOperator = '+'
        elif self._operator == 2:
            self.substract()
            self._strOperator = '-'
        elif self._operator == 3:
            self._strOperator = '/'
            self.division()
        elif self._operator == 4:
            self._strOperator = '*'
            self.multiplication()
        else:
            raise ValueError('Unexpected operator')

    def getStrOperator(self):
        return self._strOperator

    def getResult(self) -> float:
        self.__applyOperation()
        return self._result
    
class Calculator():

    def __init__(self):
        self._toDisplay = ""

    def run(self):
        while(True):
            os.system('cls||clear')
            print('****')
            print('Welcome to a complicated CALCULATOR')
            print('To exit press q')
            print('****')
            value1 = input('Introduce the 1st value: ')
            if value1 == 'q':
                break
            value2 = input('Introduce the 2nd value: ')
            if value2 == 'q':
                break
            print('What operation do you want to apply?')
            print('1. Addition')
            print('2. Substraction')
            print('3. Division')
            print('4. Multiplication')
            operation = input('Write the number of the operation: ')
            if value1 == 'q' or value2 == 'q' or operation == 'q':
                break 
            if not value1.isnumeric() or not value2.isnumeric() or not operation.isnumeric():
                raise ValueError('The input values must be numeric')
            value2 = float(value2)
            value1 = float(value1) 
            operation = int(operation)
            objOperation = Operations(value1, 
                                      value2, 
                                      operation)
            result = objOperation.getResult()
            self.__DisplayResult(value1,
                                 value2,
                                 objOperation.getStrOperator(),
                                 result)
            input('To continue press enter')

    def __DisplayResult(self, value1, value2, strOperator, result):
        print('*****')
        print(f'* {strOperator} *')
        print('*****')
        print(f'* {value1} {strOperator} {value2}')
        print('******')
        print(f'* {result} *')
        print('******')
            
def main():
    c = Calculator()
    c.run()

if __name__ == '__main__':
    sys.exit(main())