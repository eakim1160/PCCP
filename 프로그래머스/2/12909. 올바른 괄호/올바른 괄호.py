def solution(s):
    # '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때, 문자열 s가 올바른 괄호이면 true를 return 
    
    answer = True
    count = 0

    if s[0] == ")":
        return False
    
    for ch in s:
            
        if ch == "(":
            count += 1
        
        else:    
            count -= 1
            
        if count < 0:
            return False
            
    return count == 0  
