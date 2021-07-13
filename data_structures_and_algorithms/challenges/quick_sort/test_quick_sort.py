from quick_sort import quickSort

def test_quickSort_1():
    arrayForTest=[20,18,12,8,5,-2]
    quickSort(arrayForTest,0,len(arrayForTest)-1)
    excepted=[-2,5,8,12,18,20]
    assert excepted==arrayForTest
def test_quickSort_2():
    arrayForTest=[5,12,7,5,5,7]
    quickSort(arrayForTest,0,len(arrayForTest)-1)
    excepted=[5,5,5,7,7,12]
    assert excepted==arrayForTest
def test_quickSort_3():
    arrayForTest=[2,3,5,7,13,11]
    quickSort(arrayForTest,0,len(arrayForTest)-1)
    excepted=[2,3,5,7,11,13]
    assert excepted==arrayForTest

