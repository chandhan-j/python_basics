introString = input('enter any words: ')
characterCount = 0
wordCount = 1

for i in introString:
    characterCount = characterCount + 1
    if(i == ' '):
        wordCount = wordCount + 1
        
print('numberofCharactersInString')
print(characterCount)
print('numberOfWordsInString')
print(wordCount)
