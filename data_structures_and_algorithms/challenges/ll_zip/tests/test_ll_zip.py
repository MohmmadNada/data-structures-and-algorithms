from data_structures_and_algorithms.Data_Structures.linked_list.linked_list import LinkedList
from ll_zip import __version__
from ll_zip.ll_zip  import zipLists

def test_version():
    assert __version__ == '0.1.0'

def test_two_equal_LL():
    ll01=LinkedList()
    ll01.append('a')
    ll01.append('0')
    ll01.append('10')
    ll01.append(6) #a 0 10 6 
    ll02=LinkedList()
    ll02.append('first')
    ll02.append('22')
    ll02.append( 5 )
    ll02.append('Gostright')# first  22 5  gostright  
    zipLL=zipLists(ll02,ll01)
    assert str(zipLL)== "{ first } -> { a } -> { 22 } -> { 0 } -> { 5 } -> { 10 } -> { Gostright } -> { 6 } -> NULL"

def test_not_equal_LLs():
    ll01=LinkedList()
    ll01.append('a')
    ll01.append('0')
    ll01.append('10')
    ll01.append(6) #a 0 10 6 
    ll02=LinkedList()
    ll02.append('first')
    ll02.append('22')
    ll02.append('Gostright')# first  22  Gostright  
    zipLL=zipLists(ll02,ll01)
    assert str(zipLL)== "{ first } -> { a } -> { 22 } -> { 0 } -> { Gostright } -> { 10 } -> { 6 } -> NULL"
    zipLL=zipLists(ll01,ll02)
    assert str(zipLL)== "{ a } -> { first } -> { 0 } -> { 22 } -> { 10 } -> { Gostright } -> { 6 } -> NULL"

def test_empty_LL():
    ll01=LinkedList()
    ll01.append('a')
    ll01.append('0')
    ll01.append('10')# 4 0 10 
    emptyLL=LinkedList()
    zipLL01 =zipLists(ll01,emptyLL)
    zipLL02 =zipLists(emptyLL,ll01)
    zipLL03 =zipLists(emptyLL,emptyLL)
    assert str(zipLL01)=="{ a } -> { 0 } -> { 10 } -> NULL"==str(zipLL02)
    assert str(zipLL03)=="NULL"