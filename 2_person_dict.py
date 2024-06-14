person = {}
person["fname"] = "Joe"
person["lname"] = "Fonebone"
person["age"] = 51
person["spouse"] = "Edna"
person["children"] = ["Ralph", "Betty", "Joey"]
person["pets"] = {"dog": "Fido", "cat": "Sox"}

#print(person)

print(person)

# print out the name of the second child

print(person["children"][1])

# print out the name of the cat

print(person["pets"]["cat"])

# use a loop to print out the names of each child

for name in person["children"]:
    print(name)


# use a loop to print out the pets in the following format:
# The type of pet is: dog and the name of the pet is: Fido

for i,j in person["pets"].items():
    print(f" The type of pet is {i} and the name of the pet is: {j}")
