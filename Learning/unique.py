with open("team.txt", "r") as f:
    names = [line.strip() for line in f]

unique = list(dict.fromkeys(names))

print(unique)

print(len(unique))