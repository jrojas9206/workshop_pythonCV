'''
    solution - Pyramids 
'''
import sys 

def pyramids(height:int, orientation:str='a'):
    '''
        Your code goes here
    '''
    getNPointsPerFloor = lambda floor: floor+(floor-1)
    getEmptySpacesPerFloor = lambda cfloor, fflor: fflor-cfloor
    cOrder = range(1, height+1) if orientation == 'a' else range(height, 0, -1)
    pattern = ''
    for cfloor in cOrder:
        whiteSpaces = ' '*getEmptySpacesPerFloor(cfloor, height)
        nPoints = '*'*getNPointsPerFloor(cfloor)
        pattern +=  whiteSpaces + nPoints + "\n"
    return pattern

def main():
    height = input('What height do you want for the pyramid?: ')
    orientation = input('What orientation do you desire?: ')
    availableOrientations = ['a', 'b']
    if not height.isnumeric():
        raise ValueError('The height must be a numeric value')
    if orientation not in availableOrientations:
        raise ValueError('Unexpected orientation value. Available values %s' %(str(availableOrientations)))
    height = int(height)
    pattern = pyramids(height, 
                       orientation=orientation)

    print(pattern)
    '''
        Note that this code can be improve and simply!
        try debug it! and improve it!
        Happy conding!
    '''
    return 0

if __name__ == '__main__':
    sys.exit(main())