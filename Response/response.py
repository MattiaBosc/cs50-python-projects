from validator_collection import checkers

email = input("What's your meail address: ")

if checkers.is_email(email) == True:
    print("Valid")
else:
    print("Invalid")
