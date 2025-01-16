with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())

with open("students.txt", "'r") as file:
    for line in file:
        print(line[2])

with open("students.txt", "r") as file:
    for line in file:
        if len(line.strip()) > 6:
            print(line.strip())
new_line = input("enter a new name: ")

with open("students.txt", "a") as file:
    file.write(new_line + "\n")