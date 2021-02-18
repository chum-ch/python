# Add in code below the following functions : 
#        - function capitalize(word)
#        - function reverse(word)
# Edit the code below to use those functions and avoid code repetition 
# Note : A palindrome is a word which reads the same backward as forward. Example: madam, racecar.

word = input("Input a word :")
print("What do you want to do :")
print("1 : capitalize")
print("2 : reverse the word")
print("3 : check if it is palindromic")
choice = int(input("Choose an option :"))
if choice == 1:
    wordCaptitalized = word.upper()
    print(word + " => " +wordCaptitalized)
    
elif choice == 2:
    reversedWord = ""
    for i in range(len(word)-1, -1, -1):
        reversedWord += word[i]
    print(word + " => " + reversedWord)
elif choice == 3:
    reversedWord = ""
    for i in range(len(word)-1, -1, -1):
        reversedWord += word[i]
    wordCaptitalized = word.upper()
    reversedWordCaptitalized = reversedWord.upper()
    if wordCaptitalized == reversedWordCaptitalized :
        print(" => this is palindromic !")
    else:
        print(" => this is NOT palindromic !")