# a function called multi_bracket_validation(input)

def multi_bracket_validation(input):
    '''
    Your function should take a string as its only argument, and should return a boolean representing whether or not the brackets in the string are balanced. There are 3 types of brackets:
    1. Round Brackets : ()
    2. Square Brackets : []
    3. Curly Brackets : {}
    '''
    bracketsArr=[]
    for element in input:
        if element in ('{','}','(',')','[',']'):
            bracketsArr.append(element)
        arrayLen=len(bracketsArr)
    # print(bracketsArr)
    if arrayLen%2==0:
        for element in range(0,arrayLen//2): 
            if '{' in bracketsArr:
                if '}'in bracketsArr:
                    bracketsArr.remove('}') 
                    bracketsArr.remove('{')
            elif '(' in bracketsArr :

                if ')'in bracketsArr:
                    bracketsArr.remove(')') 
                    bracketsArr.remove('(')
            elif '[' in bracketsArr :

                if ']'in bracketsArr:
                    bracketsArr.remove(']') 
                    bracketsArr.remove('[')
    else:
        return False
    if len(bracketsArr)==0:
        return True
    else :
        return False
if __name__=='__main__':
    # print(multi_bracket_validation('{}'))
    # print(multi_bracket_validation('{}(){}'))
    # print(multi_bracket_validation('()[[Extra Characters]]'))
    # print(multi_bracket_validation('(){}[[]]'))
    # print(multi_bracket_validation('{}{Code}[Fellows](())'))
    # print(multi_bracket_validation('[({}]'))
    print(multi_bracket_validation('(]('))