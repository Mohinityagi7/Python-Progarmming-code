# define is_palindrome function that take one word in string as input and return True if it is palindrome else return False

# palindrome - word that reads some backwords as forward

# example
# is_palindrome("madam") ------> True
# is_palindrome("naman") ------> True
# is_palindrome("horse") ------> False


# logic (algoritham)
# step 1 -> reverse the string
# step 2 -> compare string with original string

# def is_palindrom(word):
#     reversed_word = word[::-1]
#     if word == reversed_word:
#         return True
#     else:
#         return False



# def is_palindrom(word):
#     if word == word[::-1]:
#         return True
#     return False


def is_palindrom(word):
    return  word == word[::-1]


print(is_palindrom("naman"))
print(is_palindrom("horse"))