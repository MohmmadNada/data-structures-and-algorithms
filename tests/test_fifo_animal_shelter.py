import pytest
from data_structures_and_algorithms.challenges.fifo_animal_shelter.fifo_animal_shelter import Node,Queue,Animal,Cat,Dog,AnimalShelter

def test_enqueu_cat(test_fixture):
    test_fixture.enqueue(Cat('firstCat'))
    excepted = test_fixture.mainQueue.front.value.type
    actual='cat'
    assert excepted==actual
def test_enqueu_dog(test_fixture):
    test_fixture.enqueue(Dog('firstDog'))
    test_fixture.enqueue(Dog('secondDog'))
    excepted = test_fixture.mainQueue.front.value.type
    actual='dog'
    assert excepted==actual
def test_enqueue_cat_dog(test_fixture):
    test_fixture.enqueue(Dog('firstDog'))
    excepted = test_fixture.mainQueue.front.value.type
    actual='dog'
    assert excepted==actual
    test_fixture.enqueue(Cat('firstCat'))
    excepted = test_fixture.mainQueue.front.next.value.type
    actual='cat'
    assert excepted==actual
def test_enqueue_not_dog_not_cat(test_fixture):
    assert 'Ops , your animal Must be Dog or Cat'==test_fixture.enqueue(Animal('firstDog'))
def test_dequeue_cat(test_fixture):
    test_fixture.enqueue(Cat('ahmadcat'))
    test_fixture.enqueue(Cat('secondcat'))
    test_fixture.enqueue(Dog('Dogss'))
    test_fixture.enqueue(Dog('maokli'))
    excepted='ahmadcat'
    actual=test_fixture.dequeue('cat')
    assert excepted==actual
def test_dequeue_dog(test_fixture):
    test_fixture.enqueue(Cat('ahmadcat'))
    test_fixture.enqueue(Cat('secondcat'))
    test_fixture.enqueue(Dog('Dogss'))
    test_fixture.enqueue(Dog('maokli'))
    excepted='Dogss'
    actual=test_fixture.dequeue('dog')
    assert excepted==actual
def test_dequeue_not_dog_not_cat(test_fixture):
    test_fixture.enqueue(Cat('ahmadcat'))
    test_fixture.enqueue(Dog('Dogss'))
    actual=test_fixture.dequeue('anyanimal')
    excepted=None
    assert excepted==actual

@pytest.fixture
def test_fixture():
    animalShelter=AnimalShelter()
    cat01=Cat('catName1')
    dog01=Dog('dogName1')
    return animalShelter