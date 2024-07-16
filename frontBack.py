'''
Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'
'''

def front_back(str):
  if len(str) > 1:
    firstChar = str[0:1]
    lastChar = str[-1:]
    str = str[1:]
    str = str[:-1]
    return (lastChar + str + firstChar)
  else:
    return str
