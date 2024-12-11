#8 palindrome
class PalindromeChecker:
    def __init__(self, text):
        self.text = text

    def is_palindrome(self):
        # Normalize the text by removing non-alphanumeric characters and converting to lowercase
        normalized_text = ''.join(char.lower() for char in self.text if char.isalnum())
        return normalized_text == normalized_text[::-1]
    
text = input("Enter a text to check if it is a palindrome: ")
checker = PalindromeChecker(text)

if checker.is_palindrome():
    print("The text is a palindrome.")
else:
    print("The text is not a palindrome.")
