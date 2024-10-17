'''
    Solution - Reverse a string
'''
import sys
import json 
import argparse

def reverseWords(message:str) -> list:
    '''
        Reverse the word order in a string separated by whitespace

        :Args:
            :message: str, Message to be reversed 
        :Return:
            str 
    '''
    listToWork = message.split(' ')    # The method will return a list with the splitted words 
    listToWork.reverse() # This method will affect the list directly 
    reversedString = ' '.join(listToWork)
    return {
        'Original': message,
        'Reversed': reversedString,
    }

def main():
    '''
        Example of argparse to capture user arguments 
    '''
    parser = argparse.ArgumentParser('First cool code!!')
    parser.add_argument('userMessage', type=str, help='Message that user wants to reverse')
    args = parser.parse_args()
    # Print
    reversedPhrase = reverseWords(args.userMessage)
    print(json.dumps(reversedPhrase, 
                     indent=4))
    return 0

if __name__ == "__main__":
    sys.exit(main())