def alpha_hashing(s):
    hash_arr=[0]*26
    for i in range(len(s)):
            hash_arr[ord(s[i])-ord('a')]+=1
                 
    return hash_arr



if __name__=='__main__':
    s='aaaaqwttyr'
    print(alpha_hashing(s))
