# import pytest
from repeated_word import repeated_word

def test_repeated_word():
    actual=repeated_word("Once upon a time , there was a brave princess who ..."	)
    excepted = "a"
    assert actual ==excepted 
    
def test_repeated_word_with_not_letter():
    stringtest="It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."	
    actual=repeated_word(stringtest)
    excepted = "it"
    assert actual ==excepted
def test_repeated_word_more_than_word_repeated():
    testStr="It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."	
    actual=repeated_word(testStr)
    excepted = "summer"
    assert actual ==excepted
def test_no_repeat_word():
    testStr='hi all world, haw are you ???'
    actual=repeated_word(testStr)
    excepted = None
    assert actual ==excepted
def test_empty_str():
    testStr=''
    actual=repeated_word(testStr)
    excepted = None
    assert actual ==excepted