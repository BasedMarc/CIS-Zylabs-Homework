import csv

input1 = input()

with open(input1, 'r') as wordsfile:
    words_reader = csv.reader(wordsfile)
    for row in words_reader:
        word_list = row
no_duplicates = list(dict.fromkeys(word_list))
list_length = len(no_duplicates)

for i in range(list_length):
    print(no_duplicates[i], word_list.count(no_duplicates[i]))
