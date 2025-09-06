import re

def isAllowedSpecificChar(str1):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    str1 = charRe.search(str1)
    return not bool(str1)

print(isAllowedSpecificChar("ABCDEF1239"))
print(isAllowedSpecificChar("ABCD$#$123"))







