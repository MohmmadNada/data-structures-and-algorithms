from _pytest.python_api import ApproxScalar
from left_joint import leftJoint, Hashtable
import pytest

@pytest.fixture 
def antonym_HT():
    ht2=Hashtable()
    ht2.add('diligent', 'idle')
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('guide', 'follow')
    ht2.add('flow', 'jam')
    return ht2
@pytest.fixture
def synonym_HT():
    ht1=Hashtable()
    ht1.add('diligent', 'employed') 
    ht1.add('outfit', 'garb')
    ht1.add('fond', 'enamored')
    ht1.add('guide', 'usher')
    ht1.add('wrath', 'anger')
    return ht1
def test_antonymand_synonym(synonym_HT):
    ht1=synonym_HT
    ht2=Hashtable()
    ht2.add('fond', 'averse')
    ht2.add('wrath', 'delight')
    ht2.add('diligent', 'idle')
    ht2.add('guide', 'follow')
    ht2.add('flow', 'jam')
    actual=leftJoint(ht1,ht2)
    excepted = [['diligent', 'employed', 'idle'], ['outfit', 'garb', None], ['fond', 'enamored', 'averse'], ['guide', 'usher', 'follow'], ['wrath', 'anger', 'delight']]
    assert actual ==excepted
def test_empy_firstHT(synonym_HT):
    ht1=synonym_HT
    ht2=Hashtable()
    actual=leftJoint(ht2,ht1)
    excepted=[]
    assert actual ==excepted
def test_empy_secondHT(antonym_HT):
    ht1=antonym_HT
    ht2=Hashtable()
    actual=leftJoint(ht1,ht2)
    excepted=[['diligent', 'idle', None], ['flow', 'jam', None], ['fond', 'averse', None],['guide', 'follow', None],['wrath', 'delight', None]]
    
def test_two_empty():
    ht1=Hashtable()
    ht2=Hashtable()
    actual=leftJoint(ht1,ht2)
    excepted=[]
    assert actual ==excepted