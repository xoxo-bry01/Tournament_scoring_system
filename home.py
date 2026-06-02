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
print(" Developed for College Tournament ")
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
        #get indiviidual competitors name
        individual_name= input("enter competitors name:")

        #store competitors information
        individuals[individual_name]={
            "scores":[0, 0, 0, 0, 0],
            "totals":0
        }

        print(f"{individual_name} added successfully")

        
    elif choice == "3":
       #List od avaliable events 
       events =[
           "Football",
           "Quiz",
           "Relay race",
           "chess",
           "Dodge Ball"

       ]
       #Get a competitor name
       entry_name= input("Enter competitor Name:")
       #show event list
       print("\n Avalaible Events:")

       for i in range (len(events)):
           print(f"{i+1}. {events[i]}")

       #choose event    
       event_choice= int(input("Choose one event(1-5):  "))

       #store entry
       choosen_event= events[event_choice - 1]

       one_event_entries[entry_name] = {
           "event": choosen_event,
           "score":0
       }
       print(f"{entry_name} registered for {choosen_event}!")


       
    elif choice == "4":
        #Events Lists
        events = [
            "Football",
            "Quiz",
            "Relay Race",
            "Chess",
            "Dodgeball"

        ]

        #Display Events
        print("\nEvents:")

        for i in range(len(events)):
            print(f"{i+1} . {events[i]}")

        #Choose event
        event_choice = int(input("Selelect Event (1-5):"))

        #Get score index 
        event_index = event_choice - 1

        #Enter scores for teams 
        print("\nEnter Team Scores ")

        for team in teams :

            score = int(input(f"Enter Score for {team}: "))

            #Store score 
            teams [team]["scores"][event_index] = score

            #Update total score
            teams[team]["total"] = sum(teams[team]["scores"])

        #Enter scores for individuals
        print("\nEnter Individual Scores")

        for person in individuals:

            score = int(input(f"Enter score for {person}: "))

            #Store score
            individuals[person]["scores"][event_index] = score

            #Update total score 
            individuals[person]["total"] = sum(individuals[person]["scores"])

        print("scores Updated successfully!")        
            

    elif choice == "5":
        
        print("\n====== TEAM RANKINGS ======")

        #Display team rankings
        for team in teams:
            print(f"\nTeam: {team}")
            print(f"Members: {teams[team]["members"]}")
            print(f"Scores: {teams[team]["scores"]}")
            print(f"Total Points: {teams[team]["total"]}")

        print("\n====== INDIVIDUAL RANKINGS ======")

        #Display individual rankings
        for person in individuals:

            print(f"\nCompetitor: {person}")
            print(f"Scores: {individuals[person]["scores"]}")
            print(f"Total Points: {individuals[person]["total"]}")

        print("\n====== ONE EVENT ENTRIES ======")

        #Display one-event entries
        for entry in one_event_entries:
            print(f"\nCompetitor: {entry}")
            print(f"Event: {one_event_entries[entry]["event"]}")
            print(f"Score: {one_event_entries[entry]["score"]}")
                     

    elif choice == "6":
       

       # Open file
       file = open("tournament_results.txt", "w")

       # Write team rankings
       file.write("===== TEAM RANKINGS =====\n")

       for team in teams:

            file.write(f"\nTeam: {team}\n")
            file.write(f"Members: {teams[team]['members']}\n")
            file.write(f"Scores: {teams[team]['scores']}\n")
            file.write(f"Total Points: {teams[team]['total']}\n")

        # Write individual rankings
       file.write("\n===== INDIVIDUAL RANKINGS =====\n")

       for person in individuals:

            file.write(f"\nCompetitor: {person}\n")
            file.write(f"Scores: {individuals[person]['scores']}\n")
            file.write(f"Total Points: {individuals[person]['total']}\n")

       # Write one-event entries
       file.write("\n===== ONE EVENT ENTRIES =====\n")

       for entry in one_event_entries:

            file.write(f"\nCompetitor: {entry}\n")
            file.write(f"Event: {one_event_entries[entry]['event']}\n")
            file.write(f"Score: {one_event_entries[entry]['score']}\n")

       # Close file
       file.close()

       print("Results saved successfully!")

    elif choice == "7":
        print("Thank you for using the Tournament Scoring System")
        print("Program closed")
        running = False

    else:
        print("Invalid choice. Please enter a number between 1 and 7.")