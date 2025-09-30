#3.1+3.2
names=["lily","tiffa","serina"]
for name in names:
    print(name.title())
    print(f"Hello {name.title()},how are you today?")
#3.3
vehicles=["cars","motorcycle","subway"]
for vehicle in vehicles:
    if vehicle=="cars":
        print(f"I would like to own a super {vehicle.title()}.")
    elif vehicle=="motorcycle":
        print(f"I would like to own a Honda {vehicle.title()}.")
    else:
        print(f"I can only take the {vehicle.title()} as my vehicle.")
#3.4
peoples=["lisa","john","eric"]
for people in peoples:
    print(people.title())
#3.5
print(f"due to some reasons,{peoples[1].title()} can not be here today.")
peoples[1]="tiffa"
for people in peoples:
    print(people.title()) 
#3.6
print("We have found a big table which can stay more people tonight!")
peoples.insert(0,"alex")
peoples.insert(2,"gigi")
peoples.append("rachel")
print(peoples)
#3.7
print("I am really sorry that I can only invite 2 people tonight.")
peoples_popped=peoples.pop()
print(f"\n{peoples_popped.title()},I am really sorry.")
peoples_popped=peoples.pop()
print(f"\n{peoples_popped.title()},I am really sorry.")
peoples_popped=peoples.pop()
print(f"\n{peoples_popped.title()},I am really sorry.")
peoples_popped=peoples.pop()
print(f"\n{peoples_popped.title()},I am really sorry.")
print(peoples)
print(f"Dear {peoples[0].title()},I am glad that you are still on the list.")
print(f"Dear {peoples[-1].title()},I am glad that you are still on the list.")
del peoples[0]
del peoples[0]
print(peoples)
#3.8
travel_places=["thiland","africa","korea","japan","england"]
print(travel_places)
print(sorted(travel_places))
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.sort(reverse=False)
print(travel_places)
print(len(travel_places))