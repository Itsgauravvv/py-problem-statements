def display_employee(e_tup):
    print(f"Employee ID: {e_tup[0]}")
    print(f"Employee Name: {e_tup[1]}")
    print(f"Employee Department: {e_tup[2]}")
    print("Projects Assigned:")
    for i , project in enumerate (e_tup[3], start = 1):
        print(f"{i}. {project}")

def add_project(e_tup):
    inp = input("Enter project name to add: ")
    e_tup[3].append(inp)
    print("Project added successfully.")
  
def rem_project(e_tup):
    inp = input("Enter project name to remove: ")
    if inp not in e_tup[3]:
        print("Project not found.")
        return
    else:
        e_tup[3].remove(inp)
        print("Project removed successfully.")  

def search_project(e_tup):
    inp = input("Enter project name to search: ")
    if inp in e_tup[3]:
        print("Project assigned.")
        return
    else:
        print("Project not assigned.")

def count_project(e_tup):
    count = len(e_tup[3])
    if count == 0:
        print("No projects assigned.")
    else:
        print(f"Total projects: {count}")

def sort_project(e_tup, projects):
    e_tup[3].sort()
    for i in projects:
        print(f"{i}\n")


e_id = int(input("Enter employee ID: "))
e_name = input("Enter employee name: ")
e_d = input("Enter employee department: ")

n = int(input("Enter number of projects assigned: "))
projects = []
for i in range(n):
    p_name = input(f"Enter name of project {i+1}: ")
    projects.append(p_name)
e_tup = (e_id, e_name, e_d, projects)

while True:

    print("\n========== Employee Project Management System ==========")
    print("1. View Employee Details")
    print("2. Add New Project")
    print("3. Remove a Project")
    print("4. Search a Project")
    print("5. Display Total Number of Projects")
    print("6. Display Projects Alphabetically")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nEmployee Details")
        print("-------------------------")
        display_employee(e_tup)

    elif choice == 2:
        add_project(e_tup)

    elif choice == 3:
        rem_project(e_tup)
        
    elif choice == 4:
        search_project(e_tup)

    elif choice == 5:
        count_project(e_tup)

    elif choice == 6:
        sort_project(e_tup, projects)

    elif choice == 7:
        print("Thank You!")
        break
    else:
        print("Invalid Choice.")