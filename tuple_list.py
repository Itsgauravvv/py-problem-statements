employee = (
    101,
    "Anshi Agarwal",
    "AI Developer",
    ["Payroll System", "HR Portal"]
)


def view_details():
    print("\nEmployee ID:", employee[0])
    print("Employee Name:", employee[1])
    print("Department:", employee[2])
    print("Assigned Projects:")
    for i in employee[3]:
        print(i)


def add_project():
    project = input("Enter Project Name: ")
    employee[3].append(project)
    print("Project added successfully.")


def remove_project():
    project = input("Enter Project Name: ")
    if project in employee[3]:
        employee[3].remove(project)
        print("Project removed successfully.")
    else:
        print("Project not found.")


def search_project():
    project = input("Enter Project Name: ")
    if project in employee[3]:
        print("Project Assigned.")
    else:
        print("Project Not Assigned.")


def total_projects():
    print("Total Projects:", len(employee[3]))


def display_projects():
    projects = sorted(employee[3])
    print("\nProjects in Alphabetical Order:")
    for i in projects:
        print(i)


while True:

    print("\n----- Employee Project Management System -----")
    print("1. View Employee Details")
    print("2. Add New Project")
    print("3. Remove a Project")
    print("4. Search a Project")
    print("5. Display Total Number of Projects")
    print("6. Display Projects Alphabetically")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_details()

    elif choice == 2:
        add_project()

    elif choice == 3:
        remove_project()

    elif choice == 4:
        search_project()

    elif choice == 5:
        total_projects()

    elif choice == 6:
        display_projects()

    elif choice == 7:
        print("Thank You")
        break

    else:
        print("Invalid Choice")