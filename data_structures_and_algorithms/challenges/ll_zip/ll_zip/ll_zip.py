'''
Write a function called zipLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
'''
import re
import sys
from typing import Counter              # 1 import from outside this project 
sys.path.append('..')   # 2. import from outside this project 
from Data_Structures.linked_list.linked_list import LinkedList
from Data_Structures.linked_list import *
# must get what we used, and edit * in previous line

def zipLists(list1, list2):
    current_1=list1.head
    current_2=list2.head
    newLL=LinkedList()
    # length_1=len(list1)#5
    # length_2=len(list2)#4
    # print('new LL :  ' ,length_1 ,length_2 )
    while True:
        if current_2 ==None and current_1==None :
                break
        if current_1 != None:
            newLL.append(current_1.value)
            current_1=current_1.next
        if current_2 != None:
            newLL.append(current_2.value) 
            current_2=current_2.next
    return newLL


if __name__=='__main__':
    ll_1=LinkedList()
    ll_1.append('5')
    ll_1.append('-1')
    ll_1.append('-11')
    ll_1.append(1111)
    ll_1.append('05')
    ll_1.append('stright')
    ll_1.append('stright1')
    ll_2=LinkedList()
    ll_2.append('start')
    ll_2.append('2')
    ll_2.append(' sss ')
    ll_2.append('done ')
    print(' linked list first arg :    ',ll_2)# { start } -> { 2 } -> {  sss  } -> { done  } -> NULL
    # print(' linked list second argument:    ',ll_1)
    # emptyLL=LinkedList()
    # print(zipLists(ll_2,ll_1))
    # print(zipLists(emptyLL,ll_1))
    # print(zipLists(emptyLL,emptyLL))
