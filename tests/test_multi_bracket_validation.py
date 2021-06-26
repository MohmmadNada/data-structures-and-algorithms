import pytest
from data_structures_and_algorithms.challenges.multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

def test_multi_bracket_validation_two_items_in():
    actual=multi_bracket_validation('{}')
    excepted=True
    assert actual==excepted
def test_multi_bracket_validation_many_items_in():
    actual=multi_bracket_validation('{}(){}')
    excepted=True
    assert actual==excepted
def test_multi_bracket_validation_many_items_in_with_word():
    actual=multi_bracket_validation('()[[Extra Characters]]')
    excepted=True
    assert actual==excepted
def test_multi_bracket_validation_many_items_in_without_word():
    actual=multi_bracket_validation('(){}[[]]')   
    excepted=True
    assert actual==excepted

def test_multi_bracket_validation_many_items_in_with_many_words():
    actual=multi_bracket_validation('{}{Code}[Fellows](())')   
    excepted=True
    assert actual==excepted
def test_multi_bracket_validation_order():
    actual=multi_bracket_validation('{}{Code}[Fellows](())')   
    excepted=True
    assert actual==excepted
def test_multi_bracket_validation_many_items_False_case():
    actual=multi_bracket_validation('[({}]')   
    excepted=False
    assert actual==excepted