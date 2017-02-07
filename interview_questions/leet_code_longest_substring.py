# Given a string, find the length of the longest substring without repeating characters.
# 
# Examples:
# 
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if s == "":
            return 0
        
        left = 0
        right = 1
        end = len(s)
        longest_substr = right - left
        
        letter_dict = {}
        self.make_letter_dict(s[left:right], letter_dict)
        
        while right < end:
            right += 1
            letter = s[right-1:right]
            if letter in letter_dict:
                if letter_dict[letter] > 0:
                    while letter_dict[letter] > 0:
                        left += 1
                        letter_dict[s[left-1:left]] -= 1
                if right > left:
                    letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1
            
            if right - left >  longest_substr:
                longest_substr = right - left
        
        return longest_substr


    def make_letter_dict(self, substr, letter_dict):
        for letter in substr:
            if letter in letter_dict:
                letter_dict[letter] += 1
            else:
                letter_dict[letter] = 1

