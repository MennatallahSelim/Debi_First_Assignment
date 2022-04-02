#find the nth occurrence of a word in a string!

def find_nth_occurrence(substring, string, occurrence=1):
    try:
        a = -1
        for j in range( occurrence):
            a = string.find(substring, a + 1)
            if a < 0:
                break
        return a
    except: 
        print("You entered wrong data, Please try again!!")

#simlple string matching.

def solve(a,b):
    try:
        if("*" in a):
            a1 = a.split("*")
            b1 = b[len(a1[0]):]
            if(a1[1]==""):
                return b.startswith(a1[0])
            else:
                if(b1.endswith(a1[1])):
                    return True
                else:
                    return False
        else:
            return a==b
    except NameError:

        print("Enter right name")
    except:
        print("You Entered Wrong Data!!")
  
            

#is it a palindrome?

def is_palindrome(string):
    try:
        string = str(string)
        if string== string[::-1] :
            return True
        else:
            return False   
    except:
        print("Not Palindrome!!")
is_palindrome("a")
