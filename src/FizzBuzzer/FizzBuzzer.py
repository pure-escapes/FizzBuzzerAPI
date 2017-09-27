# -*- coding: utf-8 -*-
'''
Created on 22 Sep 2017

@author: Christos Tsotskas

'''

import json

class FizzBuzzer():
    '''Fizz Buzzer Service to assess user input '''  

    
    def __init__(self):
        self.json_output = {"output":None}
    
    def __return_fizz_buzz(self, userInput):
        '''
        Assess user input 
        
        @param userInput: integer number
        
        @return: "Fizz" for 3, "Buzz" for 5, "FizzBuzz" when devisible 
                by both 3 and 5, otherwise the provided integer will be return
        
        '''
        if type(userInput) != int:
            raise Exception('Integer was expected')
    
        return "Fizz"*(userInput%3==0)+"Buzz"*(userInput%5==0) or str(userInput)
        
    
    def check_User_Input(self, userInput):
        '''
        public facing method to access the functionality of FizzBuzzer
        '''    
        return self.__return_fizz_buzz(userInput)
    
    def get_output(self, userInput):
        '''
        Generate json output according to the FizzBuzz rules
        
        @param userInput: integer number
        @return: the output of userInput in the form of a json file
        '''
         
        self.json_output["output"] = self.__return_fizz_buzz(userInput)        
        
        return json.dumps(self.json_output)
        
        
    

if __name__ == '__main__':
    pass
