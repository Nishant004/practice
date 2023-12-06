s = "abcd"
t = "abcde"

res = 0

# XOR all characters in s and t
for char in s + t:
    res ^= ord(char)

# Convert the XOR result back to character

print (chr(res))


#print(t)