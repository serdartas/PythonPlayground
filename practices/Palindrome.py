# A palindrome is a word that is spelled the same backwords.
# Example: backword(racecar) = racecar

def isPalindrome(word):
    if len(word) <= 1:
        return True
    if word[0] != word[len(word)-1]:
        return False
    return isPalindrome(word[1:len(word)-1])

# __name__ returns __main__ when file is executed directly
if __name__ == "__main__":
    print("To check if a word is a palindrome")
    word = input("Enter a word: ")
    print(word, " is", "" if isPalindrome(word) else " not", " a palindrome", sep = "")