"""Test for my functions.

Note: because these are 'empty' functions (return None), here we just test
  that the functions execute, and return None, as expected.
"""

from functions import get_info, check_whole, check_powerMale, check_powerFemale, advise_user


def test_check_whole():
    input_dict = {'sex': 'female', 'age': 20, 'weight': 200, 'height': 5.6, 'last donation': 0}
    assert isinstance(check_whole(input_dict), bool)
    assert callable(check_whole)
             
def test_check_powerMale():
    input_dict = {'sex': 'female', 'age': 20, 'weight': 200, 'height': 5.6, 'last donation': 0}
    assert isinstance(check_powerMale(input_dict), bool)
    assert callable(check_powerMale)
    
def test_check_powerFemale(): 
    input_dict = {'sex': 'female', 'age': 20, 'weight': 200, 'height': 5.6, 'last donation': 0}
    assert isinstance(check_powerFemale(input_dict), bool)
    assert callable(check_powerFemale)
     
def test_advise_user():
    input_dict = {'sex': 'female', 'age': 20, 'weight': 200, 'height': 5.6, 'last donation': 0}
    eligible_w = check_whole(input_dict)
    eligible_m = check_powerMale(input_dict)
    eligible_f = check_powerFemale(input_dict)
    assert callable(advise_user)
    assert isinstance(eligible_w, bool)
    assert isinstance(eligible_m, bool)
    assert isinstance(eligible_f, bool)
               
               


                 
    