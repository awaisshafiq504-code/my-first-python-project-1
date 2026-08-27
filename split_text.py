# Split Text
experiment = "Python is useful for Scientific Data Analysis because we can process measurements and find patterns."
words = experiment.split()
print(words)
# Count all words
word_count = 0
for word in words:
    word_count = word_count + 1
print(f"Number of words: {word_count}")

# Number of each word
for number, word in enumerate(words, start=1):
        print(f"{number},{word}")
# Count the word "Data"
data_count = 0

for word in words:
      if word == "Data":
            data_count = data_count+1
print(f"Data appears: {data_count} time(s)")
            
