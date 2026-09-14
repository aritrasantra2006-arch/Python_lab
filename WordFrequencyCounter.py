# Get sentence input
sentence = input("Enter a sentence: ")

# Convert to lowercase and split into words
words = sentence.lower().split()

# Count word frequencies
frequency = {}
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Print word counts side-by-side
for word, count in frequency.items():
    print(f"{word}: {count}", end=", ")
print()
