# example 1
personal = ["Alferd", "Tom", "Ben", "Lessi", "Mary", "Duglas"]
coutries = ["UA", "GB", "I", "SP", "FIN"]
pn = []
print(personal[1])
print(f"{personal[0]} and {personal[3]} is best friends")

print("######################################################")

# example 2
print(len(personal))
print(personal[-1])
print(personal[0:2])
print(personal[1:3])
print(personal[::])
print(personal[::-1])
print(personal[4:])

print("######################################################")

# example 3
personal.append("Chi Z")
print(personal)
pn.append(personal)
pn.append(coutries)
print(pn)
print("######################################################")
