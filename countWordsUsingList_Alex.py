#read from file
fileread = open("lincoln.txt", "r")

wordsList = []
amountList = []
stopwords = [ 'stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I', 'that', 'had', 'on', 'for', 'were', 'was', 'an' ]

for line in fileread:    #looks over entire file

    line = line.lower()
    line = line.replace(',' , '')
    line = line.replace('.' , '')

    for word in line.split():    #gets word by word
        #add into list
        #print(wordsList)
        #print(amountList)

        if word in wordsList:
            #increament the existing list
            index = wordsList.index(word)
            amountList[index] = amountList[index] + 1

        if not word in wordsList:
            #append to insert at end of index (if needed)
            wordsList.append(word)
            amountList.append(1)

#display all words and amount
print("all words and amount")
for a in wordsList:
    index = wordsList.index(a)
    print(a + " : " + str(amountList[index]) )

#sorting from min to max
for i in range(len(amountList)):
    min_index=i
    for j in range(i+1, len(amountList)):
        if amountList[min_index] > amountList[j]:
            min_index = j
    amountList[i], amountList[min_index] = amountList[min_index], amountList[i]
    wordsList[i], wordsList[min_index] = wordsList[min_index], wordsList[i] 

#display top 10 words
print("\n---top 10 words ---")
for b in range(len(wordsList)-1, len(wordsList)-10, -1):
    print(wordsList[b] + " : " + str(amountList[b]))

#display top 10 words excluding stop words
print("\n---top 10 words excluding stop words---")
index = len(wordsList) - 1 
limit = 0
while limit < 10:
    if wordsList[index] in stopwords:
        index = index - 1
    else:  
        print(wordsList[index] + " : " + str(amountList[index]))
        limit = limit + 1
        index = index - 1


