'''
    Problem definition 

Create a function called halfPyramid. The function will have two 
arguments and return the desired string. The first argument must
be the height of the pyramid (integer). The second argument is an 
optional argument called position (str) which will allow me to select 
position a, b,c,d. If the datatype is not correct or the height is 0 
or lower raise and error

a          c
*            *
**          **
***        ***

d          b
***        ***
 **        **
  *        *
'''
import sys 

def halfPyramid(height:int, orientation:str='a') -> str:
    '''
        Your code goes here
    '''
    return ''

def main():
    '''
        Define the input from the user
    '''
    pattern = halfPyramid()
    print(pattern)
    return 0

if __name__ == '__main__':
    sys.exit(main())