import os
import sys 
import time 

def blinkText(msg:str, dtime:float) -> None:
    '''
        Make blink a message surrounded by some asterisk
        e.g:
        t0:
            **********
            ** HOLA **
            **********
        t1:
            **********
            **      **
            **********

        :Args:
            - msg: str, Word or phrase to show 
            - dtime: float, Blinking period on off/on 
    '''

    """
        It is a fast solution!!... Try to improved!! 
        less code, more readable? 
        maybe add colors?
    """
    asteriskNumber = len(msg) + 6
    headerMsg = '*' * asteriskNumber
    for numberBlinks in range(10):
        os.system('cls||clear')
        print(headerMsg)
        print('**', ' '*(asteriskNumber-6) if numberBlinks%2==0 else msg, '**')
        print(headerMsg)
        time.sleep(dtime)
    return 0 

def main():
    myMessage = input('Give me the message to print: ')
    msgFreq = float(input('Give me the message frequency: '))
    # Big step of the work
    blinkText(myMessage, msgFreq)
    return 0

if __name__ == '__main__':
    sys.exit(main())