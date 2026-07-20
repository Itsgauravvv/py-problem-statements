patients = []


def add_patient():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["PatientId"] == patient_id:
            print("Patient ID already exists.")
            return

    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))

    if age <= 0:
        print("Invalid Age")
        return

    city = input("Enter City: ")

    patient = {
        "PatientId": patient_id,
        "PatientName": name,
        "Age": age,
        "City": city,
        "Visits": []
    }

    patients.append(patient)
    print("Patient Added Successfully.")


def add_visit():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["PatientId"] == patient_id:

            visit_id = int(input("Enter Visit ID: "))

            for visit in patient["Visits"]:
                if visit["VisitId"] == visit_id:
                    print("Visit ID already exists.")
                    return

            fee = int(input("Enter Consultation Fee: "))
            medicine = int(input("Enter Medicines Cost: "))

            if fee < 0 or medicine < 0:
                print("Invalid Amount")
                return

            visit = {
                "VisitId": visit_id,
                "DoctorName": input("Enter Doctor Name: "),
                "Department": input("Enter Department: "),
                "ConsultationFee": fee,
                "MedicinesCost": medicine,
                "Status": input("Enter Status: ")
            }

            patient["Visits"].append(visit)
            print("Visit Added Successfully.")
            return

    print("Patient not found.")


def view_patients():
    for patient in patients:

        print("\nPatient ID :", patient["PatientId"])
        print("Patient Name :", patient["PatientName"])
        print("Age :", patient["Age"])
        print("City :", patient["City"])

        print("\nVisits")

        if len(patient["Visits"]) == 0:
            print("No Visits")

        for visit in patient["Visits"]:
            print("Visit ID :", visit["VisitId"])
            print("Doctor :", visit["DoctorName"])
            print("Department :", visit["Department"])
            print("Consultation Fee :", visit["ConsultationFee"])
            print("Medicine Cost :", visit["MedicinesCost"])
            print("Status :", visit["Status"])
            print()

        print("--------------------------------")


def search_patient():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["PatientId"] == patient_id:

            print("\nPatient ID :", patient["PatientId"])
            print("Patient Name :", patient["PatientName"])
            print("Age :", patient["Age"])
            print("City :", patient["City"])
            print("Total Visits :", len(patient["Visits"]))

            for visit in patient["Visits"]:
                print("\nVisit ID :", visit["VisitId"])
                print("Doctor :", visit["DoctorName"])
                print("Department :", visit["Department"])
                print("Consultation Fee :", visit["ConsultationFee"])
                print("Medicine Cost :", visit["MedicinesCost"])
                print("Status :", visit["Status"])

            return

    print("Patient not found.")


def update_status():
    patient_id = int(input("Enter Patient ID: "))
    visit_id = int(input("Enter Visit ID: "))
    status = input("Enter New Status: ")

    for patient in patients:
        if patient["PatientId"] == patient_id:

            for visit in patient["Visits"]:
                if visit["VisitId"] == visit_id:
                    visit["Status"] = status
                    print("Status Updated Successfully.")
                    return

            print("Visit not found.")
            return

    print("Patient not found.")


def total_bill():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["PatientId"] == patient_id:

            total = 0

            for visit in patient["Visits"]:
                bill = visit["ConsultationFee"] + visit["MedicinesCost"]
                total += bill
                print("Visit", visit["VisitId"], "Bill :", bill)

            print("-----------------------")
            print("Total Bill :", total)
            return

    print("Patient not found.")