word_count = {}  # Map each word to its count
input_file = open('quote.txt', 'r')

for line in input_file:
  words = line.split()
  for word in words:
    word = word.lower()
    word_count[word] = word_count.get(word,0) + 1

print word_count
input_file.close()  