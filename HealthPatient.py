patient_name = input("Enter Patient Name: ")
age = int(input("Enter Patient Age: "))
temperature = float(input("Enter Body Temperature (°C): "))
heart_rate = int(input("Enter Heart Rate (BPM): "))
oxygen = int(input("Enter Oxygen Saturation (SpO2): "))

if oxygen < 90 or temperature > 40:
    risk = "Critical"
    recommendation = "Immediately transfer the patient to ICU."
elif (oxygen >= 90 and oxygen <= 94) or (temperature >= 38 and temperature <= 40):
    risk = "High"
    recommendation = "Doctor consultation and hospital admission required."
elif heart_rate > 100 or age > 60:
    risk = "Medium"
    recommendation = "Keep the patient under observation."
else:
    risk = "Low"
    recommendation = "Patient is healthy and can go home after consultation."

print("Patient Name:", patient_name)
print("Age:", age)
print("Temperature in Celsius:", temperature)
print("Heart Rate:", heart_rate, "BPM")
print("Oxygen Level:", oxygen, "%")
print("Risk Level:", risk)
print("Recommendation:", recommendation)

if age >= 75:
    print("\nSenior Citizen")
    print("Priority Consultation Required")