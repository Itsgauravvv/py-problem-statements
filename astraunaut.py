astronauts = []

def register_astronaut():
    astro_id = int(input("Enter Astronaut ID: "))

    for astro in astronauts:
        if astro[0] == astro_id:
            print("Astronaut ID already exists.")
            return

    name = input("Enter Astronaut Name: ")
    agency = input("Enter Space Agency: ")

    n = int(input("Enter Number of Missions: "))
    missions = []

    for i in range(n):
        mission = input("Enter Mission Name: ")
        missions.append(mission)

    astronauts.append((astro_id, name, agency, missions))
    print("Astronaut Registered Successfully.")


def view_astronauts():
    if len(astronauts) > 0:
        for astro in astronauts:
            print("\nAstronaut ID :", astro[0])
            print("Name         :", astro[1])
            print("Agency       :", astro[2])
            print("Missions     :", ", ".join(astro[3]))
            print("----------------------------------")
    else:
        print("No data currently")


def assign_mission():
    astro_id = int(input("Enter Astronaut ID: "))
    mission = input("Enter New Mission Name: ")

    for astro in astronauts:
        if astro[0] == astro_id:
            astro[3].append(mission)
            print("Mission Assigned Successfully.")
            return

    print("Astronaut not found.")


def remove_mission():
    astro_id = int(input("Enter Astronaut ID: "))
    mission = input("Enter Mission Name: ")

    for astro in astronauts:
        if astro[0] == astro_id:
            if mission in astro[3]:
                astro[3].remove(mission)
                print("Mission Removed Successfully.")
            else:
                print("Mission not found.")
            return

    print("Astronaut not found.")


def search_astronaut():
    astro_id = int(input("Enter Astronaut ID: "))

    for astro in astronauts:
        if astro[0] == astro_id:
            print("\nAstronaut ID :", astro[0])
            print("Name         :", astro[1])
            print("Agency       :", astro[2])
            print("Missions     :", ", ".join(astro[3]))
            return

    print("Astronaut not found.")


def experienced_astronauts():
    print("\nExperienced Astronauts\n")

    found = False

    for astro in astronauts:
        if len(astro[3]) >= 3:
            print("Name :", astro[1])
            print("Agency :", astro[2])
            print("Total Missions :", len(astro[3]))
            print("----------------------")
            found = True

    if found == False:
        print("No Experienced Astronaut Found.")


def agency_count():
    agencies = []

    for astro in astronauts:
        if astro[2] not in agencies:
            agencies.append(astro[2])

    print()

    for agency in agencies:
        count = 0

        for astro in astronauts:
            if astro[2] == agency:
                count += 1

        print(agency, ":", count)


while True:

    print("\n===== Astronaut Mission Management System =====")
    print("1. Register New Astronaut")
    print("2. View All Astronauts")
    print("3. Assign New Mission")
    print("4. Remove Mission")
    print("5. Search Astronaut")
    print("6. Display Experienced Astronauts")
    print("7. Space Agency-wise Astronaut Count")
    print("8. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        register_astronaut()

    elif choice == 2:
        view_astronauts()

    elif choice == 3:
        assign_mission()

    elif choice == 4:
        remove_mission()

    elif choice == 5:
        search_astronaut()

    elif choice == 6:
        experienced_astronauts()

    elif choice == 7:
        agency_count()

    elif choice == 8:
        print("Thank You")
        break

    else:
        print("Invalid Choice")