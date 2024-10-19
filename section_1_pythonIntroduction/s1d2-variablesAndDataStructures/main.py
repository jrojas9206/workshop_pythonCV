#########
# INTRO #
#########

'''
 In the following script you will find some basic operations 
 that can be applied to variable and datastructures
'''

# Testing the float variables 
print('-> Testing floats')
try:
    value = 2.0**2048
    print(' ', value)
except OverflowError:
    print('  [ERROR] the value can not be keep it in memory')

try:
    value = 2.0**1023
    print(' ', value)
except OverflowError:
    print(' [ERROR] the value can not be keep it in memory')

#########
# Lists #
#########

# Example of list creation 
L0 = list()
L01 = []
L1 = [1,2,3]
L2 = [i for i in range(4)]
L3 = [L1, [4,5,6], 7]

print('\n-> Selecting values from a list')
# How to print the 5 in the L3 Variable ?
print('  -> L3 values %s' %(str(L3)))
print('   -> L3[1][1] =', L3[1][1])

# How to print the 7 of L3?
print('    -> L3[2] =', L3[2])

# How to change a value in a list?
print("\n-> Original values of L1: %s" %(str(L1)))
print(" -> Setting 4 in position 0 of variable L1")
L1[0] = 4
print(" -> Update value of L1 - L1[0] = 4: %s" %(str(L1)))

# How to select a range of values in a list?
Lnew = L3[1:3]
print('\n-> Values on L3: %s' %(str(L3)))
print(" -> Selected range of L3 - L3[1:3] = %s" %(str(Lnew)))

# How to append Values to a list - With the method append(Value)
print("\n-> Using some methods available for lists")
print('\n  -> Original value of L1 -', L1)

L1.append(5)
print('  ->  Update values from L0 after L0.append(5)')
print('  ', L1)
# How to reverese the order of a list 
print('  -> Reversing the order of L0 - L0.reverse()')
L1.reverse()
print('  ', L1)

##########
# Tuples #
##########

print('\Tuple definitions')

T0 = tuple()
T1 = (1, 2, 3)
T2 = (i for i in range(4)) # It will return the pointer of the object 
T21 = tuple(i for i in range(4)) # Will return the object - after conversion 
T3 = (L1, [4,5,6], 7)

try:
    T1[0] = 4
except TypeError:
    print('[ERROR] It is not possible to modify a tuple they are immutable')

print('\n-> Creating a tuple from 1 till 100')
T0to100 = tuple(i for i in range(1,101))
print('  ', T0to100)

print('\n-> Selecting the second position of the tuple T3')
print('T3[1]= ', T3[1])

print('-> Counting elements in a tuple, T0.count(VALUE)')
T0 = [1,2,2,3,4,4]
print(' -> Tuple T0 = ', T0)
# How many 4 are in the tuple T0
foursInT0 = T0.count(4)

print(f' -> There are {foursInT0} Fours in T0')