"""
409. Longest Palindrome

Given a string text which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.

For this question, letters are case-sensitive, for example, "Aa" is not considered a palindrome.
"""
# Change this function so it works correctly
letters=[]
lower_letters=[]
for i in range(65,91):
    letters.append(chr(i))
    lower_letters.append(chr(i).lower())
All_letters = letters + lower_letters
def longest_palindrome_length(text):
    if len(text) == 1:
        return 1
    else:
        for e in All_letters:
            if text.count(e) %2==0 and text.count(e)>0 :
                tem=1+text.count(e)
                if tem<=len(text):
                    return tem
                else:
                    return len(text)



if __name__ == '__main__':
    test_cases = [('abccccdd', 7),      # dccaccd / dccbccd
                  ('a', 1),             # a
                  ('school', 3)]        # oso / oco / oho / olo

    for test_text, expected in test_cases:
        result = longest_palindrome_length(test_text)
        msg = 'Correct' if expected == result else 'Wrong'
        print(f'[{msg:7s}] longest_palindrome_length("{test_text}") should be {expected}')



