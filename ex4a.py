from sys import argv

flags = argv[1:4]

if "-h" in flags:
    print("This is the help text!")

team = argv[4]

print(f"Your favorite team is {team}.")

other_team = argv[5]

print(f"Your least favorite team is {other_team}.")

if "-a" in flags:
    print(f"To reiterate, those teams were {team} and {other_team}.")

if "-b" in flags:
    print("That was fun!")
