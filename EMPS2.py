def add_emp(emp):

    e_id = int(input("Enter Employee ID: "))

    for e_tup in emp:
        if e_tup[0] == e_id:
            print("Employee ID already exists.")
            return

    e_name = input("Enter Employee Name: ")
    e_d = input("Enter Department: ")

    n = int(input("Enter Number of Projects: "))

    p_l = []

    for i in range(n):
        p_name = input(f"Enter Project {i+1}: ")
        p_l.append(p_name)

    e_tup = (e_id, e_name, e_d, p_l)

    emp.append(e_tup)

    print("Employee added successfully.")


def view_emp(emp):

    if len(emp) == 0:
        print("No employees found.")
        return

    for e_tup in emp:

        print(f"\nEmployee ID: {e_tup[0]}")
        print(f"Employee Name: {e_tup[1]}")
        print(f"Department: {e_tup[2]}")
        print("Projects:")

        for i, p in enumerate(e_tup[3], start=1):
            print(f"{i}. {p}")

        print("-" * 30)


def add_p(emp):

    e_id = int(input("Enter Employee ID: "))

    for e_tup in emp:

        if e_tup[0] == e_id:

            p = input("Enter New Project: ")

            e_tup[3].append(p)

            print("Project assigned successfully.")

            return

    print("Employee not found.")


def rem_p(emp):

    e_id = int(input("Enter Employee ID: "))

    for e_tup in emp:

        if e_tup[0] == e_id:

            p = input("Enter Project Name: ")

            if p in e_tup[3]:
                e_tup[3].remove(p)
                print("Project removed successfully.")
            else:
                print("Project not found.")

            return

    print("Employee not found.")


def search_emp(emp):

    e_id = int(input("Enter Employee ID: "))

    for e_tup in emp:

        if e_tup[0] == e_id:

            print(f"\nEmployee ID: {e_tup[0]}")
            print(f"Employee Name: {e_tup[1]}")
            print(f"Department: {e_tup[2]}")
            print("Projects:")

            for i, p in enumerate(e_tup[3], start=1):
                print(f"{i}. {p}")

            return

    print("Employee not found.")


def multi_p(emp):

    f = False

    for e_tup in emp:

        if len(e_tup[3]) > 2:

            print(f"\nEmployee Name: {e_tup[1]}")
            print(f"Projects: {len(e_tup[3])}")

            f = True

    if not f:
        print("No employee is working on more than two projects.")


def dept_cnt(emp):

    if len(emp) == 0:
        print("No employees found.")
        return

    d_l = []

    for e_tup in emp:

        if e_tup[2] not in d_l:
            d_l.append(e_tup[2])

    for d in d_l:

        c = 0

        for e_tup in emp:

            if e_tup[2] == d:
                c += 1

        print(f"{d}: {c}")


emp = []

while True:

    print("\n========== Employee Project Management System ==========")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Assign New Project")
    print("4. Remove Project")
    print("5. Search Employee")
    print("6. Display Employees Working on Multiple Projects")
    print("7. Display Department-wise Employee Count")
    print("8. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        add_emp(emp)

    elif ch == 2:
        view_emp(emp)

    elif ch == 3:
        add_p(emp)

    elif ch == 4:
        rem_p(emp)

    elif ch == 5:
        search_emp(emp)

    elif ch == 6:
        multi_p(emp)

    elif ch == 7:
        dept_cnt(emp)

    elif ch == 8:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")