sentence = input("Enter a sentence: ")
word = input("Enter word to replace: ")
re_word = input("Enter replacement word: ")

if len(re_word)>1:
    start = sentence.find(word)
    len_word = len(word)
    result = sentence[:start] + re_word + sentence[start+len_word:]
    print(result)
else:
    print("The word you entered is not in the sentence.")

