'''
Created on 22 Sep 2017

@author: CHristos Tsotskas
'''
import unittest

from FizzBuzzer import FizzBuzzer


class testFizzBuzzer(unittest.TestCase):


    def setUp(self):
        self.FizzBuzzer = FizzBuzzer()


    def tearDown(self):
        pass


    def test_Return_Fizz_When_Integer_Number_Is_Devisible_By_Number_Three(self):
        expected_value = 'Fizz'
        user_input = 3
        
        received_value = self.FizzBuzzer.check_User_Input(user_input)
        
        error_message = "return Fizz if the user gives 3: read:" + str(received_value) + " whereas " + str(expected_value) 
        self.assertEquals(received_value, expected_value, error_message)
        
    def test_Return_Buzz_When_Integer_Number_Is_Devisible_By_Number_Five(self):
        expected_value = 'Buzz'
        user_input = 5
        
        received_value = self.FizzBuzzer.check_User_Input(user_input)
        
        error_message = "return Buzz if the user gives 5 read:" + str(received_value) + " whereas " + str(expected_value)
        self.assertEquals(received_value, expected_value, error_message)
               
    def test_return_number_as_a_string_when_integer_number_is_neither_devisible_by_number_five_nor_three(self):
        expected_value = '7'
        user_input = 7
        
        received_value = self.FizzBuzzer.check_User_Input(user_input)
        
        error_message = "return "+expected_value+" if the user gives "+ str(user_input) +" read:" + str(received_value) + " whereas " + str(expected_value)
        self.assertEquals(received_value, expected_value, error_message)
        
    def test_return_FizzBuzz_when_integer_number_is_devisible_by_number_five_and_three(self):
        expected_value = 'FizzBuzz'
        user_input = 15
        
        received_value = self.FizzBuzzer.check_User_Input(user_input)
        
        error_message = "return FizzBuzz if the user gives 15, read:" + str(received_value) + " whereas " + str(expected_value)
        self.assertEquals(received_value, expected_value, error_message)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()