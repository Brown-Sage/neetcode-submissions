import math
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for char in s:
            if char.isalnum():
                new_s += char.lower()
        point = math.ceil(len(new_s)/2)
        if len(new_s)%2 !=0:
            str1 = new_s[:point]
            str2 = new_s[point-1:len(new_s)][::-1]
        else:
            str1 = new_s[:point]
            str2 = new_s[point:len(new_s)][::-1]
        print(str1)
        print(str2)
        
        if str1 == str2 :
            return True
        else : 
            return False
    