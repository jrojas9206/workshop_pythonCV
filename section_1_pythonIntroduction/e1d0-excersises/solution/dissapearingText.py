import os 
import sys 
import time
import argparse

def dissapearingText(msg:str, speed:float=0.5, nreps:int=10) -> None:
    '''
        Make dissapear a word of phrase chracter by character
        e.g:

        T0:
           Hola Mundo!
        T1:
           Ola Mundo!
        T2:
            la Mundo!
        
        :Args:
          - msg: str, Message to show
          - speed: float, Speed in which the text have to dessapear. Default: 0.5
          - nreps: number of repetitions default 10
    '''
    temporal = msg
    cntrReps = 0
    while cntrReps < nreps:
        for i in range(len(msg)):
            os.system('cls||clear')
            emptyText2add = " "*(len(temporal)-len(msg[i:]))
            print(emptyText2add+msg[i:])
            time.sleep(speed)
        cntrReps += 1
    # There is a bug in this code, can you find it? ;) 
    os.system('cls||clear')

def main():
    parser = argparse.ArgumentParser('Python excersie For Loop and methods')
    parser.add_argument('message', type=str, help="Message to print")
    parser.add_argument('--speed', type=float, help='Dissqpperance speed. Default: 0.5', default=0.5)
    parser.add_argument('--nreps', type=int, help='Number or repetitions. Default:5', default=5)
    args = parser.parse_args()
    dissapearingText(args.message,
                     args.speed,
                     args.nreps)
    return 0

if __name__ == '__main__':
    sys.exit(main())