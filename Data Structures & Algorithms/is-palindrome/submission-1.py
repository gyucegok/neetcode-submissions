class Solution:
    def isPalindrome(self, s: str) -> bool:
        my_list = [c.lower() for c in s if c.isalnum()]
        forward_string = "".join(my_list)
        backward_string = forward_string[::-1]
        if backward_string == forward_string:
            return True
        else:
            return False
        
        