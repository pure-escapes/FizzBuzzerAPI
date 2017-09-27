# -*- coding: utf-8 -*-
'''
Created on 22 Sep 2017

@author: Christos Tsotskas
'''
import unittest
import json

from FizzBuzzer import FizzBuzzer

class testFizzBuzzer(unittest.TestCase):


    def setUp(self):
        self.FizzBuzzer = FizzBuzzer()


    def tearDown(self):
        pass


    def test_return_Fizz_when_integer_number_is_devisible_by_number_three(self):
        expected_value = 'Fizz'
        user_input = 3
        
        received_value = self.FizzBuzzer.check_User_Input(user_input)
        
        error_message = "return Fizz if the user gives 3: read:" + str(received_value) + " whereas " + str(expected_value) 
        self.assertEquals(received_value, expected_value, error_message)
        
    def test_return_Buzz_when_integer_number_is_devisible_by_number_five(self):
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

    def test_an_exception_is_raised_if_a_bad_input_is_provided(self):        
        user_input = "somethingBad!"
        
        with self.assertRaises(Exception) as context:
            self.FizzBuzzer.check_User_Input(user_input)
        
        error_message = 'an exception with message "Integer was expected" should have been raised'
        self.assertTrue('Integer was expected' in context.exception, error_message)
        
    def test_a_json_file_is_generated_as_an_output(self):
        expected_value = 'FizzBuzz'
        check_for_json_type_output = False
        user_input = 15
        
        received_value = self.FizzBuzzer.get_output(user_input)
        
        try:
            check_for_json_type_output = json.loads(received_value)
            check_for_json_type_output = True
        except ValueError as e:
            print('invalid json: %s' % e)
            
            
        self.assertTrue(check_for_json_type_output,"a valid json file was expected!")
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()