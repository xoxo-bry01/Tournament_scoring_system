# Tournament Scoring System
# Unit 4 Programming Assignment

# Data Structures
teams = {}
individuals = {}
one_event_entries = {}

# Main Program Loop
running = True

print("===================================")
print(" TOURNAMENT SCORING SYSTEM ")
print("===================================")

while running:

    # Main Menu
    print("\nMAIN MENU")
    print("1. Add Team")
    print("2. Add Individual")
    print("3. Add One Event Entry")
    print("4. Enter Scores")
    print("5. View Rankings")
    print("6. Save Results")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    # Menu Selection
    if choice == "1":
        #get team name
        team_name= input("Enter team name:")
        #create empty member list
        members= []

        #Loop to add five members
        for i in range (5):
            member= input(f"Enter Member {i+1} name:") 
            members.append(member)
            #store team information
            teams[team_name] ={
                "members": members,
                "scores": [0, 0, 0, 0, 0, 0],
                "total": 0
            }
            print(f"{team_name} added successfully!")

    elif choice == "2":
        print("Add Individual selected")

    elif choice == "3":
        print("Add One Event Entry selected")

    elif choice == "4":
        print("Enter Scores selected")

    elif choice == "5":
        print("View Rankings selected")

    elif choice == "6":
        print("Save Results selected")

    elif choice == "7":
        print("Program closed")
        running = False

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")