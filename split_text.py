# Split Text
experiment = "Python is useful for Scientific Data Analysis because we can process measurements and find patterns."
words = experiment.split()
print(len(words))
for number, word in enumerate(words, start=1):
        print(f"{number},{word}")