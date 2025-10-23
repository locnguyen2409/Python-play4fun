students = {
    "Alice": {"Math": 90,"English": 85},
    "Bob": {"Math": 78,"Science": 88},
}
print("Alice's Math score: ", students ["Alice"]["Math"])

print("Bob's Science score: ", students ["Bob"]["Science"])

students["Alice"]["History"] = 92

students["Bob"]["Math"] = 82

students["Charlie"]={"Math": 99,"English": 86}

del students["Alice"]["Math"]

print("Final dictionary: ")
for s in students:
    print(s, students[s])



