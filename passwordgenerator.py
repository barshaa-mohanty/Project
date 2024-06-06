# PASSWORD GENERATOR
try:
    import string
    import random
    if __name__=="__main__":
        s1=string.ascii_lowercase
        s2=string.ascii_uppercase
        s3=string.digits
        s4=string.punctuation
        len=int(input("Enter the length of your password:"))
        l=[]
        l.extend(list(s1))
        l.extend(list(s2))
        l.extend(list(s3))
        l.extend(list(s4))
        random.shuffle(l)
        print("Your password is:")
        print("".join(l[0:len]))
except:
    print("The length of password should be integer")