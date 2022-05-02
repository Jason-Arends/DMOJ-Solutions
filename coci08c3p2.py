# COCI '08 Contest 3 #2 Kemija

words = str(input())
i = 0
message = ''
while i < len(words):
    message = message + words[i]
    if words[i] in 'aeiou':
        i += 3
    else:
        i += 1
print(message)
