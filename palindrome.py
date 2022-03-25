# This only works with three-digits numbers
what = input ("Enter a three- or four-digit number: ")
what = int(what)

if what > 99 and what < 1000:

    
    a = what%10


    b = what/100

   

    if a == int(b):
        print("The number you entered is a palindrome")

    else:
        print("The number you entered is not a palindrome")


elif what >= 1000 and what <10000:

    
    a = what%10


    b = what/10

    c = int(b)%10
    d = int(b)/10
    e = int(d)%10
    f = int(d)/10


    if a == int(f) and int(c) == e:
        print("The number you entered is a palindrome")

    else:
        print("The number you entered is not a palindrome")

else:
    print("Incorrect number")
        




