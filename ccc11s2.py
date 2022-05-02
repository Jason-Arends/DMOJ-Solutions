# CCC '11 S2 - Multiple Choice

blob = str(input())

# pull the number off the front
num_of_resp = int(blob[0])

# left with alphas
letters = blob[1:]

# remove whitespace from the input
i = 0
redux = ''
while i < len(letters):
    #if letters[i] is not ' ':
    if letters[i].isalpha():
        redux = redux + letters[i]
    i += 1

# separate responses from correct answers (superfluous, but helpful for overcoming my own deficiencies)
resps = redux[0:num_of_resp]
key = redux[num_of_resp:]

# while loop to compare responses with correct answers 
correct = 0
inc = 0
while inc != num_of_resp:
    if key[inc] == resps[inc]:
        correct += 1
    inc += 1

print(correct)