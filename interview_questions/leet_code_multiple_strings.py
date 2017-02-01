# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
# 
# Note:
# 
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        digits1 = [int(num1[x]) for x in range(len(num1)-1,-1,-1)]
        digits2 = [int(num2[x]) for x in range(len(num1)-1,-1,-1)]
        
        print digits1
        print digits2
        
        for num2col in xrange(len(digits2)):
            carry = 0
            result = 0
            for num1col in xrange(len(digits1)):
                mult = digits1[num1col] * digits2[num2col] + carry
                carry = mult / 10
                mult = mult % 10
                result += 10*num1col*mult
            
            
                
            
            
        
        
