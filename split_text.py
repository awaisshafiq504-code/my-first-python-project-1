# Split Text
experiment = "Python Scientific Data Analysis"
words = experiment.split()
word_count = len(words)
first_word = words[0]
print(f"First word: {first_word}")
second_word = words[1]
print(f"Second word: {second_word}")
third_word = words[2]
print(f"Third word: {third_word}")
four_word = words[3]
print(f"Four word: {four_word}")
print(words)
print(f"Number of words: {word_count}")
for word in words:
    print(word)