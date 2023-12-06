# Example 1:

word = "USA"
# Output: true
# Example 2:
#
# word = "FlaG"
# Output: false


if word.isupper() or word[1:].isupper() or word.islower():
    print (True)

if word[0].isupper() and word[1:].islower():
    print (True)

else:

    print (False)