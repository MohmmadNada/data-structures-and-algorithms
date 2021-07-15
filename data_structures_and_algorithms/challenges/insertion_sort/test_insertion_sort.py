from insertion_sort import insertion_sort
def test_simple_list():
    arr1=[8,4,23,42,16,15]
    actual = insertion_sort(arr1)
    excepted = [4, 8, 15, 16, 23, 42]
    assert actual == excepted  

def test_reverse_sorted():
    arr1=[20,18,12,8,5,-2]
    actual = insertion_sort(arr1)
    excepted = [-2,5,8,12,18,20]
    assert actual == excepted  

def test_few_uniques():
    arr1=[5,12,7,5,5,7]
    actual = insertion_sort(arr1)
    excepted = [5,5,5,7,7,12]
    assert actual == excepted

def test_nearly_sorted():
    arr1=[2,3,5,7,13,11]
    actual = insertion_sort(arr1)
    excepted = [2,3,5,7,11,13]
    assert actual == excepted