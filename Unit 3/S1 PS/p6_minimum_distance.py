"""
Understand:
- Write function min_distance() w/ paramaters words (String list), 
word1 and word2 (Strings).
- Return minimum distance between word1 and word2 in words.
- Distance between one word and adjacent word is 1 (so integers)
Plan:
- Establish indexes of word1 and word2. This can be done by s.find(x) method.
- Return the difference between word1 and word2 indexes.
*s.find(x) method oesn't work with list of Strings, only Strings.

New Plan:
- Create two variables representing the word1 index and word2 index in words.
- Iterate through words, checked to find the index of word1 and word2.
- Return the difference between the index variables of word1 and word2.

Implement:
"""

def min_distance(words, word1, word2):
    index1 = 0
    index2 = 0

    for index in range(0, len(words)):
        if words[index] == word1:
            index1 = index
        elif words[index] == word2:
            index2 = index
    return abs(index2 - index1)
    

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words2, "code", "practice")
print(dist3)
