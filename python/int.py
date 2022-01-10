newpass = input("entre new password: ")
print("new password set")
tries = 0
passinput = ("need password")
def needpass():
    passinput = ("need password")
    print(passinput)
    passinput = input("entre password: ")
while passinput != newpass:
    for tries in range(3):
        if passinput == ("need password"):
            passinput = input("entre password: ")
        elif passinput == newpass:
            break
        else:
            print("password inccorect")     
            needpass()
    else:
        print("device locked, too many attempt")
        quit()
else:
    print("welcome user")