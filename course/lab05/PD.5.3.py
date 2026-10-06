def palindrome(word,left,right):
    if left>=right:
        return True
    elif word[left]!=word[right]:
        return False
    else:
        return palindrome(word,left+1,right-1)

word=input()
q=int(input())

for _ in range(q):
    left,right=map(int,input().split())
    result=palindrome(word,left-1,right-1)
    print("YES" if result else "NO")