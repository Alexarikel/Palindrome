while True:
    what = input("Enter a number or a word: ")
    print("The input you entered is a palindrome" if what[::1] == what[::-1] else "The input you entered is not a palindrome")




