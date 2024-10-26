"""
Understand:
- Write function first_palindrome() that takes in parameter words (String 
list) and returns first palindromic string in list. A string is palindromic
if it reades the same forward and backward.
- Return "" if not found.
Plan:
- Iterate index of words via for loop.
- If words[index] == words[index][::-1], return it
- Return ""
Implement:
"""
def first_palindrome(words):
    for index in range(0, len(words)-1):
        if(words[index] == words[index][::-1]):
            return words[index]
        
    return "";
    pass


words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)