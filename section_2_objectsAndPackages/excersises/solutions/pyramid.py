'''
    Solution - Pyramids 
'''
import sys 

def pyramidAB(height:int, orientation:str='a'):
    '''
        Create the pattern of half pyramids 

        a    b
        *    ***
        **   ** 
        ***  *

        :Args:
            :height: int, Number of floor for the pyramid 
            :orientation: str, Desired orientation [a, b]. Default: a
    '''
    hpyramid2return = ""
    floors = range(1, height+1) if orientation == 'a' else range(height, 0, -1)
    for floor in floors:
        hpyramid2return = hpyramid2return + '*'*floor + '\n'
    return hpyramid2return

def pyramidCD(height:int, orientation:str='c'):
    '''
        Create the pattern of half pyramids 

        c    d
          *   ***
         **    ** 
        ***     *

        :Args:
            :height: int, Number of floor for the pyramid 
            :orientation: str, Desired orientation [a, b]. Default: a
    '''
    hpyramid2return = ""
    floors = range(1, height+1) if orientation == 'c' else range(height, 0, -1)
    for cFloor in floors:
        tmp = ('*'*cFloor) + (' '*(height-cFloor)) + '\n'
        tmp = [character for character in tmp]
        tmp.reverse()
        hpyramid2return += ''.join(tmp)
    return hpyramid2return

def halfPyramid(height:int, orientation:str='a') -> str:
    '''
        Your code goes here
    '''
    pattern = ''
    if orientation == 'a' or orientation == 'b':
        pattern = pyramidAB(height,
                            orientation=orientation)
    elif orientation == 'c' or orientation == 'd':
        pattern = pyramidCD(height,
                            orientation=orientation)
    else:
        raise ValueError('Unexpected pyramid orientation')
    return pattern

def main():
    heigth = input('How many floor do you want in your pyramid?: ')
    orientation = input('What orientation do you want [a,b,c,d]?: ')
    possibleOrientation =  ['a','b','c','d']
    if orientation not in possibleOrientation:
        raise ValueError('Undefined orientation, the available orientation are: %s' %(str(possibleOrientation)))
    if not heigth.isnumeric():
        raise ValueError('The heigh must be a numeric value')
    heigth = int(heigth)
    pattern = halfPyramid(heigth,
                          orientation=orientation)
    print(pattern)
    '''
        Note that in this solution there undesired newLines, 
        how will you correct such behaviour?
    '''
    return 0

if __name__ == '__main__':
    sys.exit(main())