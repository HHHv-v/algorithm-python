def palindrome(word):
    if len(word)<=1:
        return True
    elif word[0]!=word[-1]:
        return False
    else:
        return palindrome(word[1:-1])

word=input()
q=int(input())

for _ in range(q):
    left,right=map(int,input().split())
    result=palindrome(word[left-1:right])
    print("YES" if result else "NO")