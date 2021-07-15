from marge_sort import margeSort,marge

def test_Reverse_sorted():
    testArr=[20,18,12,8,5,-2]
    actual=margeSort(testArr)
    excepted=[-2,5,8,12,18,20]
    assert testArr== excepted
def test_Few_uniques():
    testArr=[5,12,7,5,5,7]
    actual=margeSort(testArr)
    excepted=[5,5,5,7,7,12]
    assert testArr== excepted
def test_Nearly_sorted():
    testArr=[2,3,5,7,13,11]
    actual=margeSort(testArr)
    excepted=[2,3,5,7,11,13]
    assert testArr== excepted