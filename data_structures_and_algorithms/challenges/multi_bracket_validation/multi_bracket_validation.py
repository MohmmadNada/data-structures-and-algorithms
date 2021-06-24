# a function called multi_bracket_validation(input)
import re

def multi_bracket_validation(input):
    '''
    Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:
    1. Round Brackets : ()
    2. Square Brackets : []
    3. Curly Brackets : {}
    '''
    count_open_circle =input.count('(')
    count_close_circle =input.count(')')
    count_open_curly =input.count('{')
    count_close_curly =input.count('}')
    count_open_sequre =input.count('[')
    count_close_sequre =input.count(']')
    if count_open_circle==count_close_circle and count_open_curly==count_close_curly  and count_open_sequre ==count_close_sequre  :
        bracketsBalanceCount=True
    else:
        bracketsBalanceCount=False
    
    checkOrder1=re.search('\(.?}',input)
    checkOrder2=re.search('\(.?]',input)
    checkOrder3=re.search('\{.?\)',input)
    checkOrder4=re.search('\{.?]',input)
    checkOrder5=re.search('\[.?\)',input)
    checkOrder6=re.search('\[.?}',input)
    if checkOrder1 or checkOrder2 or checkOrder3 or checkOrder4 or checkOrder5 or checkOrder6:
        orderCondition =False
    else :
        orderCondition =True
    if orderCondition and bracketsBalanceCount:
        return True
    else  :
        return False

if __name__=='__main__':
    print(multi_bracket_validation('{}'))
    print(multi_bracket_validation('{}(){}'))
    print(multi_bracket_validation('()[[Extra Characters]]'))
    print(multi_bracket_validation('(){}[[]]'))
    print(multi_bracket_validation('{}{Code}[Fellows](())'))
    print(multi_bracket_validation('[({}]'))
    print(multi_bracket_validation('{(})'))
    print(multi_bracket_validation('[({}]'))