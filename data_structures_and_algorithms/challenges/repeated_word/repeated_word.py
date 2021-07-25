
import re
def repeated_word(stringInput):
  stringInput=stringInput.lower()
  stringInput=re.findall(r'[A-Za-z]+',stringInput)
  checkArr = []

  for i in range(0,len(stringInput)-1):
    
    k=i
    for j in  range(i+1,len(stringInput)-1):
      k=k+1
      if stringInput[k] in checkArr:
        return stringInput[k]
      checkArr=checkArr+[stringInput[k]]
      if stringInput[k]==stringInput[i]:
        return stringInput[k]
    checkArr = []

  return None