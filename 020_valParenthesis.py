def isValid(s):

    dict_pare = {'{':'}', '[':']', '(':')'}
    l_s = []  
    n = len(s)
    for i in range(0, n):
        
        if s[i] in dict_pare:
            l_s.append(dict_pare[s[i]])
        elif l_s and l_s[-1] == s[i]:
            l_s.pop() 
        else: 
            return False
    return l_s == []
 

         



def isValid_demo(s):
    bracket_map = {"(": ")", "[": "]",  "{": "}"}
    open_par = set(["(", "[", "{"])
    stack = []
    for i in s:
        print(i)
        if i in open_par:
            stack.append(i)
        elif stack and i == bracket_map[stack[-1]]:
                stack.pop()
        else:
            return False
    return stack == []

print(isValid_demo("()[]{{}}"))     #T


print(isValid("{[]}")) #T
print(isValid("([)]")) #F
print(isValid("(]"))    #F
print(isValid("()[]{{}}"))     #T
print(isValid("["))  #F
print(isValid("(("))  #F
print(isValid("){")) #F
print(isValid("(){}}{")) #F
print(isValid("(])")) #F

            
        