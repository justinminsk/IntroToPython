wordstring= 'it was the best of times it was the worst of times '
wordstring+= 'it was the age of wisdom it was the age of foolishness'
wordlist = wordstring.split()
wordfreq= [] # create empty Python list
for w in wordlist:
    wordfreq.append(wordlist.count(w)) # count of the times word appears in the list
print("String\n" + wordstring+"\n")
print("List\n" + str(wordlist) + "\n")
print("Frequencies\n" + str(wordfreq) + "\n")
print("Pairs\n" + str(list(zip(wordlist, wordfreq))))