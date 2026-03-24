A=['a','b','c','d']
def next(s):
    for i in range(len(s)-1,-1,-1):
        if s.count('d') == len(s):
            return 'a'*(len(s)+1)
        if s[i] == A[-1]:
            pass
        elif s[i] in A:
            for n in range(len(A)):
                if A[n] == s[i]:
                    s=s[0:i]+A[n+1]+'a'*len(s[i+1:])
                    break
            break
    return s
    
test=['aaa','bccc','ddd','bbcd','ddabdc','addd']
for i in test:
    print(f'The next string of s is: {next(i)}')
    
def previous(s):
    for i in range(len(s)-1,-1,-1):
        if s.count('a') == len(s):
            return 'd'*(len(s)-1)
        if s[i] == A[0]:
            pass
        elif s[i] in A:
            for n in range(len(A)):
                if A[n] == s[i]:
                    s=s[0:i]+A[n-1]+'d'*len(s[i+1:])
                    break
            break
    return s

def previous_palindrome(s):
    s=previous(s)
    if s ==s[::-1]:
        return s
    else:
        return previous_palindrome(s)

test=['aaa','bccc','ddd','bbcd','ddabdc','addd','abc','adda','daac']
for i in test:
    print(f'The nearest palindrome string that stands before s is: {previous_palindrome(i)}')
    
def count_palindrome(s):
    a=previous(s)
    count=0
    while len(a) == len(s):
        if a == a[::-1]:
            count+=1
        a=previous(a)
    return count

test=['aaa','abc','adda','daac']
for i in test:
    print(f'the number of palindrome strings which have the same length as s and stand behind s is: {count_palindrome((i))}')
    
def count_contain_s(n,s):
    a='a'*n
    count=0
    while len(a) == n:
        if s in a:
            count+=1
        a=next(a)
    return count

test=[[4,'aaa'],[3,'ab'],[5,'adda'],[5,'daac']]
for i in test:
    print(f'The number of strings of length n which contain s is: {count_contain_s(i[0],i[1])}')
    


