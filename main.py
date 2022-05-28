# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    if(len(word) == len(anagram)):

        sorted_str1 = sorted(word)
        sorted_str2 = sorted(anagram)

        # if sorted char arrays are same
        if(sorted_str1 == sorted_str2):
             return True
        else:
            return False

    else:
        return False
print("Checking if two words are Anagrams")
word = input("Enter the first word")
word2 =input("Enter the second Word")
print(find_anagram(word.lower(),word2.lower()))
