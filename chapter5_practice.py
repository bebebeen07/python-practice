#5.1
car="subaru"
if car == "subaru":
    print("True")
else:
    print("False")
#5.3+5.4+5.5
alien_color="green"
if alien_color == "green":
    print("You've got 5 scores")
else:
    print("You've got 10 scores")
#5.6
age=1
if age < 2:
    print("This is a baby.")
elif age < 4:
    print("This is a children.")
elif age < 13:
    print("This is a child.")
elif age < 18:
    print("This is an adolescent")
elif age < 65:
    print("This is an adult.")
else:
    print("Old.")
#5.8+5.9
names=["sam","admin","jaden","sara","nick"]
for name in names:
    if name == "admin":
        print(f"Hello {name.title()},would you like to see a status report?")
    elif name =="":
        print("We need to find some users!")
    else:
        print(f"Hello {name.title()},thank you for logging in again.")
#5.10