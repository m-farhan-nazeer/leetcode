
def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack=[]
    
    for val in s :
        
        if not stack and (val =="]" or val =="}" or val ==")"):
            print('----------')
            return False
        if val =="(" or val =="{" or val =="[":
            stack.append(val)
        else:
            key = stack[-1]
            if key =="(" and val ==")" or key =="{" and val =="}" or key =="[" and val =="]" :
                stack.pop()
            else:
                return False

        
            
    if stack:
        return False
    return True
            
print(isValid("()"))