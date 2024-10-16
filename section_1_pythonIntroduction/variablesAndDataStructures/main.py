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

# Tuples 
