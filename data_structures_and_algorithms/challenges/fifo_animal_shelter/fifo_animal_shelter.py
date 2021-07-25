class Node :
    '''
    Node class that has properties for the value stored in the Node, and a pointer to the next node.
    '''
    def __init__(self,value):
        self.value=value
        self.next=None


class Queue :
    def __init__(self):
        '''
        This object should be aware of a default empty value assigned to front when the queue is created.
        '''
        self.front=None
        self.rear=None
    def enqueue(self,value):
        '''
        takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
        '''
        newNode=Node(value)
        if self.rear==None:
            self.rear=newNode
            self.front=newNode
        else:
            self.rear.next=newNode
            self.rear=newNode
    def dequeue (self):
        '''
        Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value. Should raise exception when called on empty queue
        '''
        try:
            if self.rear==None:
                raise Exception('THIS Queue is Empty')
            else:
                temp=self.front
                self.front=self.front.next
                temp.next=None
            return temp.value
        except ValueError:
            return 'Oops  , empty Queue'
    def peek(self):
        '''
        does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue. Should raise exception when called on empty queue
        '''
        try:
            if self.front==None:
                raise Exception('Oop`s This Queue is Empty ')
            else:
                temp=self.front
                return temp.value
        except AttributeError:
            return 'the queue is empty '
    def isEmpty(self):
        '''
        Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.
        '''
        if self.front==None:
            return True
        else:
            return False

class Animal:
    def __init__(self,animalName):
        self.value=animalName
        self.next=None
class Cat(Animal):
    # def ___init_(self,cat_name):
        # self.value=cat_name
        # self.next=None
        type='cat'
class Dog(Animal):
    # def ___init_(self,dog_name):
        # self.value=dog_name
        # self.next=None
        type='dog'


class AnimalShelter:
    '''AnimalShelter which holds only dogs and cats. The shelter operates using a first-in, first-out approach.
        '''
    def __init__(self):
        self.mainQueue=Queue()
        self.secondQueue=Queue()
    def enqueue(self,animal): # add to the back 
        '''
        enqueue(animal): adds animal to the shelter. animal can be either a dog or a cat object.
        '''
        # isinstance(object, classtype)
        if isinstance(animal, Cat) or isinstance(animal, Dog) :
            self.mainQueue.enqueue(animal)
        else:
            return 'Ops , your animal Must be Dog or Cat'
    def dequeue(self,pref):
        # dequeue(pref): returns either a dog or a cat. If pref is not "dog" or "cat" then return null.
        current = None
        while not self.mainQueue.isEmpty():
            if self.mainQueue.front.value.type==pref  :
                # print('---------99')
                # self.mainQueue.dequeue()
                if current==None:
                    current= self.mainQueue.dequeue()
                    current =current.value
                else:
                    self.mainQueue.dequeue()
            else:
                enqueueItem=self.mainQueue.dequeue()
                self.secondQueue.enqueue(enqueueItem)
        while not self.secondQueue.isEmpty():
            enqueueItem=self.secondQueue.dequeue()
            self.mainQueue.enqueue(enqueueItem)
        

        return current
if __name__=='__main__':
    animalShelter=AnimalShelter()
    cat1=Cat('ca01')
    cat2=Cat('ca02')
    cat3=Cat('ca03')
    dog1=Dog('dog01')
    dog2=Dog('dog02')
    dog3=Dog('dog03')
    dog4=Dog('dog04')
    animalShelter.enqueue(cat1) # ca01
    animalShelter.enqueue(cat2)# ca02
    animalShelter.enqueue(cat3)# ca03
    animalShelter.enqueue(dog1)
    animalShelter.enqueue(dog2)
    animalShelter.enqueue(dog3)
    animalShelter.enqueue(dog4)
    # print(animalShelter.dequeue('cat')) # cat01
    print(animalShelter.dequeue('dog'))# dog01
    # print(cat.type,cat.next,cat.value)# cat None ca01
    # print(animalShelter.mainQueue.front.value)# cat
