def palindrome(arr):
    if(arr==arr[::-1]):
        return 'palindrome' 
    else:
        return 'no palindrome'

print(palindrome([1,2,3,3,2,1]))