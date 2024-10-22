import sys 
# Definition of the object
class Bike(object):
    
    #Object Contstructor
    def __init__(self):

        # Public attributes 
        self._frame = {
            'material': 'steel',
            'color': 'white',
            'quantity': 1
        }
        self._wheel = {
            'material': 'rubber',
            'geometry': 'circle'
        }
    
    # Public method
    def Rocking(self, value): 
        '''
            Action difinition goes here
        '''
        return 'work in progress.._(-8-)_'

    # Public method
    def Tilting(self, angle):
        '''
            Action difinition goes here
        '''
        return 'work in progress..\\(*8*)'

    # Public method
    def Turning(self, direction):
        '''
            Action difinition goes here
        '''
        return 'work in progress..(*8*)/'
    
def main():
    objBike = Bike() # Creation of the bike instance 
    msg = objBike.Rocking() # Calling a method from the object
    print(msg) # Print on terminal the answer message 
    return 0

if __name__ == '__main__':
    sys.exit(main())
