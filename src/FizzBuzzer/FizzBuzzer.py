# -*- coding: utf-8 -*-
'''
Created on 22 Sep 2017

@author: Christos Tsotskas

'''

class FizzBuzzer():
    ''' Service to assess user input '''
    

    
    def __init__(self):
        pass
    
    def __return_fizz_buzz(self, userInput):
        '''
        Assess user input 
        
        @param userInput: integer number
        
        @return: "Fizz" for 3, "Buzz" for 5, "FizzBuzz" when devisible 
                by both 3 and 5, otherwise the provided integer will be return
        
        '''
    
        return "Fizz"*(userInput%3==0)+"Buzz"*(userInput%5==0) or str(userInput)
        
    
    def check_User_Input(self, userInput):
        '''
        public facing method to access the functionality of FizzBuzzer
        '''

    
        return self.__return_fizz_buzz(userInput)
    

if __name__ == '__main__':
    pass
