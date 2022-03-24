# This only works with three-digits numbers
what = input ("Enter a three- or four-digit number: ")

if int(what) > 99 and int(what) < 1000:

    print("starting check for three digits")
    a = int(what)%10


    b = int(what)/10

    c = int(b)%10
    d = int(b)/10

   

    if a == int(d):
        print("The number you entered is a palindrome")

    else:
        print("The number you entered is not a palindrome")


if int(what) >= 1000 and int(what) <10000:

    
    a = int(what)%10


    b = int(what)/10

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
        




