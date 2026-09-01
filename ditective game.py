
suspects = ["Arjun", "Meera", "Rahul"]
clues = {
    "Arjun": "Was at the office",
    "Meera": "Was at home",
    "Rahul": "Was near the museum"
}


def show_suspects():
    print("\n----- SUSPECTS -----")

    for suspect in suspects:
        print(suspect)


def show_clues():
    print("\n----- CLUES -----")

    for suspect, clue in clues.items():
        print(suspect, ":", clue)


def check_suspect(name):
    if name == "Rahul":
        return "Case Solved! Rahul is the culprit."

    elif name in suspects:
        return "This suspect is innocent."

    else:
        return "Suspect not found."


print("================================")
print("      MYSTERY CASE SOLVER")
print("================================")

print("\nA valuable artifact has been stolen!")
print("You are the detective.")
print("Find the culprit using the clues.")

show_suspects()
show_clues()

choice = input("\nEnter the suspect's name: ").title()

result = check_suspect(choice)

print("\n----- INVESTIGATION RESULT -----")
print(result)

if "Case Solved" in result:
    print("Congratulations! You solved the mystery.")
else:
    print("The investigation is still open.")