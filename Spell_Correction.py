from textblob import TextBlob

wrd = input("Enter a Word : ")

b = TextBlob(wrd)
print(b.correct())

#Another way to spell check

'''from spellchecker import SpellChecker

corrector = SpellChecker()

word = input("Enter a Word : ")

if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is : ", correct_word)'''