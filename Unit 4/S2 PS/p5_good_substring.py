"""
Understand:
- Write function count_good_substrings() that takes in parameter string s
and returns number of good substrings of length three.
- A string is good if there are no repeated characters.
- Multiple occurences of the same substring are counted.
Plan:
- Create helper function, no_repeat() that takes in parameter string ss and
returns True if there are no repeated chracters. False otherwise.
    - Iterate through index, i, of ss via for loop.
    - Iterate through index, j=i+1, of ss via for loop.
    - During each iteration, compare ss[i] to ss[j], if equal, return False
    otherwise increment j, to the end of len(ss).
    - Repeat for every char ss[i].
    - Return True
- Create counter, count, initialized at 0.
- Create pointer, start, initalized at 0.
- Create pointer, end, initialized at start+3.
- Iterate through s via while loop until end = len(s)
- If no_repeat(s.substring(start, end)), then increment count.
- Increment start and end by 1.
- Return count.

Implement:
"""
def no_repeat(ss):
    for i in range(0, len(ss)):
        for j in range(i+1, len(ss)):
            if ss[i] == ss[j]:
                return False
    return True
    pass

def count_good_substrings(s):
    count = 0
    start = 0
    end = start+3

    while (end <= len(s)):
        if (no_repeat(s[start:end])):
            print(s[start:end])
            count += 1
        start, end = start+1, end+1

    return count
    pass

s1 = "xyzzaz"
s2 = "xyzxyz"
print(count_good_substrings(s1))
print(count_good_substrings(s2))
