import inspect
import os
import re

import pytest

import session6


README_CONTENT_CHECK_FOR = [
    'create_deck',
    'call_lambda',
    'winner'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 1, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 5


# def test_indentations():
#     ''' Returns pass if used four spaces for each level of syntactically \
#     significant indenting.'''
#     lines = inspect.getsource(session6)
#     spaces = re.findall('\n +.', lines)
#     for space in spaces:
#         assert len(space) % 4 == 2, "Your script contains misplaced indentations"
#         assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_royal_flush_1():
    hand_1 = ['c-10', 'c-j', 'c-q', 'c-k', 'c-a']
    hand_2 = ['h-8', 'H-9', 'h-10', 'h-j', 'h-q']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Royal Flush ** Player 1 won !', 'Incorrect Result'

def test_royal_flush_2():
    hand_1 = ['h-8', 'H-9', 'c-10', 'H-K', 'h-Q']
    hand_2 = [ 's-10', 'S-j', 'S-q', 's-A', 'S-k']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Royal Flush ** Player 2 won !', 'Incorrect Result'
    
def test_straight_flush_3():
    hand_1 = ['c-2', 'c-3','c-4','c-5','c-6']
    hand_2 = [ 'c-q', 'd-q', 's-q', 'H-q', 'D-2']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight Flush ** Player 1 won !', 'Incorrect Result'
    
def test_straight_flush_4():
    hand_1 = ['c-2', 'c-3','c-4','c-5','c-6']
    hand_2 = ['H-9', 'h-10', 'h-j', 'h-Q','H-K']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight Flush ** Player 2 won !', 'Incorrect Result'    
    
def test_straight_flush_5():
    hand_1 = ['d-8', 'd-9', 'd-10', 'D-j']
    hand_2 = ['S-a', 'c-a','d-a','h-a']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight Flush ** Player 1 won !', 'Incorrect Result'    
    
def test_straight_flush_6():
    hand_1 = ['c-10', 'c-9', 'c-8', 'c-k']
    hand_2 = ['s-9', 's-10', 's-j', 's-q']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight Flush ** Player 2 won !', 'Incorrect Result'    
    
def test_straight_flush_7():
    hand_1 = ['d-9', 'd-10', 'D-j']
    hand_2 = ['S-2', 'c-3','c-4']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight Flush ** Player 1 won !', 'Incorrect Result'    
    
def test_straight_flush_8():
    hand_1 = ['c-9', 'c-10', 'C-j']
    hand_2 = ['d-9', 'd-10', 'D-j']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight Flush ** Player 2 won !', 'Incorrect Result'

def test_four_of_a_kind_9():
    hand_1 = ['c-q', 'd-q', 's-q', 'H-q', 'c-2']
    hand_2 = ['h-8', 'H-9', 'h-10', 'h-j', 'S-k']
    output = session6.winner(hand_1, hand_2)
    assert output == '4-of-kind ** Player 1 won !', 'Incorrect Result'
    
def test_four_of_a_kind_10():
    hand_1 = ['h-8', 'c-9', 'c-10', 's-2', 'h-Q']
    hand_2 = ['d-a','d-10', 's-a', 'c-A', 'h-a']
    output = session6.winner(hand_1, hand_2)
    assert output == '4-of-kind ** Player 2 won !', 'Incorrect Result'

def test_four_of_a_kind_11():
    hand_1 = ['s-4', 'c-4', 'd-4', 'H-4']
    hand_2 = ['c-2', 'c-3','c-a','c-5']
    output = session6.winner(hand_1, hand_2)
    assert output == '4-of-kind ** Player 1 won !', 'Incorrect Result'

def test_four_of_a_kind_12():
    hand_1 = ['D-A','s-a', 'c-a', 'D-9']
    hand_2 = [ 'D-10', 'C-10', 's-10', 'h-10']
    output = session6.winner(hand_1, hand_2)
    assert output == '4-of-kind ** Player 2 won !', 'Incorrect Result'

def test_full_house_13():
    hand_1 = ['c-9','d-9','S-9','h-2','S-2']
    hand_2 = ['c-2','c-3','c-4','c-k','c-a']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Full-House ** Player 1 won !', 'Incorrect Result' 

def test_full_house_14():
    hand_1 = ['c-2','c-3','c-4','c-9','c-a']
    hand_2 = ['c-q','d-q', 'S-q', 'h-8', 'c-8']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Full-House ** Player 2 won !', 'Incorrect Result'
    
def test_flush_15():
    hand_1 = ['c-2', 'c-3', 'c-9', 'c-K', 'c-a']
    hand_2 = ['s-9', 'c-10', 'd-j', 'h-q', 's-K']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Flush ** Player 1 won !', 'Incorrect Result'    
    
def test_flush_16():
    hand_1 = ['c-10', 'c-9', 'c-8', 'c-k', 'c-A']
    hand_2 = ['d-10', 'd-9', 'd-8', 'd-K', 'd-a']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Flush ** Player 2 won !', 'Incorrect Result'    
    
def test_flush_17():
    hand_1 = ['c-2', 'c-3', 'c-a', 'c-K']
    hand_2 = ['s-K', 'c-10', 'd-j', 'h-q']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Flush ** Player 1 won !', 'Incorrect Result'       
    
def test_flush_18():
    hand_1 = ['h-10', 'h-9', 'H-8', 'h-a']
    hand_2 = ['s-10', 's-9', 's-8', 's-a']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Flush ** Player 2 won !', 'Incorrect Result'   
    
def test_flush_19():
    hand_1 = ['c-2', 'c-a', 'c-K']
    hand_2 = ['s-K', 'h-k', 'd-k']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Flush ** Player 1 won !', 'Incorrect Result'   
    
def test_flush_20():
    hand_1 = ['D-2', 'S-2', 'c-K']
    hand_2 = ['s-10', 's-a', 's-4']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Flush ** Player 2 won !', 'Incorrect Result'    

def test_straight_21():
    hand_1 = ['c-2', 'c-3', 'c-4', 'd-6', 'C-5']
    hand_2 = [ 'c-10', 'd-10', 's-9', 's-10', 'c-7']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight ** Player 1 won !', 'Incorrect Result'     
    
def test_straight_22():
    hand_1 = ['c-9', 's-9', 'd-2', 'h-2', 's-A']
    hand_2 = ['c-3', 'd-4', 'H-5', 's-7', 'S-6']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight ** Player 2 won !', 'Incorrect Result'      
    
def test_straight_23():
    hand_1 = ['s-10', 'c-9', 's-8', 's-j']
    hand_2 = [ 's-k', 'c-k', 'd-2', 'c-3']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight ** Player 1 won !', 'Incorrect Result'  

def test_straight_24():
    hand_1 = ['c-2', 'd-3', 'h-4', 's-5']
    hand_2 = [ 's-7', 'c-8', 'd-10', 'h-9']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight ** Player 2 won !', 'Incorrect Result'  

def test_straight_25():
    hand_1 = [ 's-2', 'd-4', 'c-3']
    hand_2 = [ 's-a', 'c-a', 'd-a']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight ** Player 1 won !', 'Incorrect Result'  

def test_straight_26():
    hand_1 = [ 's-10', 'c-q', 'd-j']
    hand_2 = ['h-A', 's-a', 's-2']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Straight ** Player 1 won !', 'Incorrect Result'

def test_three_of_a_kind_27():
    hand_1 = ['s-a', 'c-a', 's-10', 'c-2', 'd-a']
    hand_2 = ['s-j', 'd-j', 's-9', 'c-9', 'h-3']
    output = session6.winner(hand_1, hand_2)
    assert output == '3-of-a-kind ** Player 1 won !', 'Incorrect Result'

def test_three_of_a_kind_28():
    hand_1 = [ 's-9', 'h-9', 'd-3', 'c-4', 's-a']
    hand_2 = [ 's-10', 'c-2', 'd-2', 'h-2', 'h-q']
    output = session6.winner(hand_1, hand_2)
    assert output == '3-of-a-kind ** Player 2 won !', 'Incorrect Result'  

def test_three_of_a_kind_29():
    hand_1 = ['s-a', 'c-a', 's-9', 'h-a']
    hand_2 = ['s-10', 'c-10', 'd-3', 'h-10']
    output = session6.winner(hand_1, hand_2)
    assert output == '3-of-a-kind ** Player 1 won !', 'Incorrect Result'  

def test_three_of_a_kind_30():
    hand_1 = [ 's-9', 'c-9', 'd-9']
    hand_2 = [ 's-a', 'c-a', 'd-10']
    output = session6.winner(hand_1, hand_2)
    assert output == '3-of-a-kind ** Player 1 won !', 'Incorrect Result'      
    
def test_two_pair_31():
    hand_1 = [ 's-j', 'd-j', 's-9', 'c-9', 'h-3']
    hand_2 = ['s-k', 'd-k', 'c-2', 'd-4', 'h-q']
    output = session6.winner(hand_1, hand_2)
    assert output == '2-pairs ** Player 1 won !', 'Incorrect Result'      

def test_two_pair_32():
    hand_1 = ['s-10', 'c-10', 's-8', 'h-8', 'd-2']
    hand_2 = ['s-j', 'd-j', 's-9', 'c-9', 'h-3']
    output = session6.winner(hand_1, hand_2)
    assert output == '2-pairs ** Player 2 won !', 'Incorrect Result'     

def test_two_pair_33():
    hand_1 = ['s-a', 'c-a', 'h-9', 'd-9']
    hand_2 = ['c-q', 'd-q', 'h-4', 'h-7']
    output = session6.winner(hand_1, hand_2)
    assert output == '2-pairs ** Player 1 won !', 'Incorrect Result'     

def test_two_pair_34():
    hand_1 = [ 'd-a', 'h-a', 's-2', 'c-2']
    hand_2 = ['s-a', 'c-a', 'h-9', 'd-9']
    output = session6.winner(hand_1, hand_2)
    assert output == '2-pairs ** Player 2 won !', 'Incorrect Result'     

def test_one_pair_35():
    hand_1 = [ 's-9', 'h-9', 'd-3', 'c-4', 's-Q']
    hand_2 = ['s-a', 'd-10', 'c-7', 'h-k', 'c-2']
    output = session6.winner(hand_1, hand_2)
    assert output == '1-pair ** Player 1 won !', 'Incorrect Result'      

def test_one_pair_36():
    hand_1 = [ 's-9', 'h-9', 'd-3', 'c-4', 's-a']
    hand_2 = ['c-a', 'd-a', 'c-3', 'd-4', 'c-k']
    output = session6.winner(hand_1, hand_2)
    assert output == '1-pair ** Player 2 won !', 'Incorrect Result'    

def test_one_pair_37():
    hand_1 = ['c-q', 'd-q', 'h-4', 'h-7']
    hand_2 = ['c-a', 'd-k', 'h-6', 's-Q']
    output = session6.winner(hand_1, hand_2)
    assert output == '1-pair ** Player 1 won !', 'Incorrect Result'    

def test_one_pair_38():
    hand_1 = ['s-10', 'c-10', 'd-2']
    hand_2 = ['s-a',  'd-j', 'h-3']
    output = session6.winner(hand_1, hand_2)
    assert output == '1-pair ** Player 1 won !', 'Incorrect Result'    

def test_one_pair_39():
    hand_1 = ['s-2', 'c-2', 'd-3']
    hand_2 = ['s-a', 'd-a', 'h-2']
    output = session6.winner(hand_1, hand_2)
    assert output == '1-pair ** Player 2 won !', 'Incorrect Result'    

def test_equal_hand_40():
    hand_1 = ['s-2', 'c-2', 'd-3','c-4']
    hand_2 = ['s-a', 'd-a', 'h-2']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Both hands need equal cards', 'Incorrect Result'   

def test_more_than_5_cards_41():
    hand_1 =['s-2', 'c-2', 'd-3','c-4','c-a','c-q']
    hand_2 =['s-a', 'd-a', 'h-2','h-3','h-5','h-6']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Each hand needs 3, 4 or 5 cards - More than 5 cards found', 'Incorrect Result' 
    
def test_less_than_3_cards_42():
    hand_1 =['s-2', 'c-2']
    hand_2 =['s-a', 'd-a']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Each hand needs 3, 4 or 5 cards - Less than 3 cards found', 'Incorrect Result'   
    
def test_duplicate_cards_in_hands_43():
    hand_1 =[ 's-9', 'h-9', 'd-3', 'c-4', 's-a']
    hand_2 = ['c-a', 'd-a', 'c-3', 'd-4', 's-9']
    output = session6.winner(hand_1, hand_2)
    assert output == 'Duplicate cards found in both hands - Only 1 deck is permitted', 'Incorrect Result'   

def test_deck_creation_normal_function_44():
    suites = ['C','D','H','S']
    cards  = ['2','3','4','5','6','7','8','9','10','J','K','Q','A']    
    lst    = session6.create_deck(suites,cards)
    assert len(lst) == 52, 'Wrong number of cards in deck'
    
def test_deck_creation_lambda_function_45():
    suites = ['C','D','H','S']
    cards  = ['2','3','4','5','6','7','8','9','10','J','K','Q','A'] 
    fn     = lambda x,y: x + '-' + y    
    lst    = session6.call_lambda(fn, suites, cards)
    assert len(lst) == 52, 'Wrong number of cards in deck'    