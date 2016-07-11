
# Word Counter
# filename = input("Enter the filename: ")
filename = "README.md"
inputFile = open(filename, 'r')
uniqueWords = {}

# Add the unique words in the file to the list
for line in inputFile:
    words = line.split()
    for word in words:
        frequency = uniqueWords.get(word, 0)
        if frequency is None:
            uniqueWords[word] = 1
        else:
            uniqueWords[word] = frequency + 1
# close file
inputFile.close()

# Print the unique words and their frequencies,
# in alphabetical order
words = list(uniqueWords.keys())
words.sort()
length = 25
for word in words:
    print("{:{}} : {}".format(word, length, uniqueWords[word]))
