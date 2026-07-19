patient_name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
insurance = input("Enter Insurance Status (Yes/No): ").lower()
policy = input("Enter Policy Status (Active/Expired): ").lower()
treatment_cost = float(input("Enter Estimated Treatment Cost: "))

if insurance == "yes" and policy == "active" and treatment_cost <= 500000:
    insurance_status = "Approved"
    decision = "Patient is eligible for Cashless Treatment."

elif insurance == "yes" and policy == "active" and treatment_cost > 500000 and treatment_cost <= 1000000:
    insurance_status = "Pending Approval"
    decision = "Additional approval from the insurance company is required."

elif insurance == "yes" and policy == "expired":
    insurance_status = "Rejected"
    decision = "Insurance policy has expired. Cashless treatment is not available."

elif insurance == "no":
    insurance_status = "Not Available"
    decision = "Patient must pay the treatment cost."

else:
    insurance_status = "Invalid"
    decision = "Invalid patient information entered."

print("Patient Name:", patient_name)
print("Patient Age:", age)
print("Insurance Status:", insurance_status)
print("Approval Status:", insurance_status)
print("Final Decision:", decision)

if age >= 65 and insurance_status == "Approved":
    print("\nSenior Citizen Benefit Applied")
    print("5% Discount on Hospital Service Charges")

emergency = input("\nIs the patient an Emergency Case? (Yes/No): ").lower()

if emergency == "yes":
    print("Emergency Priority: Immediate Treatment Required")