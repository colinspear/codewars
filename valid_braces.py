def my_validBraces(string):
    '''
    loop through characters in string
    as you encounter open braces, create an ordered queue that tells you 
        which closed brace you should encounter first
    if you encounter a closed brace, check if it's the correct one
    if not exit with false
    if so, drop from queue and continue to next character
    '''
    o = '([{'
    c = ')]}'
    q = []
    
    for s in string:
        print('q: ', q)
        if s in o:
            q.append(c[o.index(s)])
        if s in c:
            if q == []:
                return False
            if s == q[-1]:
                q = q[:-1]
            else:
                return False

    if q == []:
        return True
    else:
        return False

def top_validBraces(string):
    braces = {"(": ")", "[": "]", "{": "}"}
    stack = []
    for character in string:
        if character in braces.keys():
            stack.append(character)
        else:
            if len(stack) == 0 or braces[stack.pop()] != character:
                return False
    return len(stack) == 0  

def alt_validBraces(s):
  while '{}' in s or '()' in s or '[]' in s:
      s=s.replace('{}','')
      s=s.replace('[]','')
      s=s.replace('()','')
  return s==''