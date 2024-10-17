'''
    Problem definition:

Write the function reverseWords. The function must take 1 argument. 
The function return the original and reversed word in a dictionary with
the keys Original and Reversed.

Input:
    'hola mundo!'
Expected output:
    {
        'Original': 'hola mundo!',
        'Reversed': 'mundo! hola',
    }
'''
import sys 

def reverseWords(msg:str) -> str:
    '''
        Write your code here
    '''
    return {}

def main():
    '''
        Define the input from the user and modify the code to make it 
        work 
    '''
    dict2print = reverseWords()

    print(dict2print)
    return 0

if __name__ == '__main__':
    sys.exit(main())