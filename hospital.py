days = int(input())
doctors = 7
patients_treated = 0
patients_untreated = 0

for i in range(1,days + 1):
    patients = int(input())
    if i % 3 == 0:
        if patients_untreated > patients_treated:
            doctors = doctors + 1
    if patients - doctors == 0:
        patients_treated = patients_treated + doctors
        patients_untreated = patients_untreated + (patients - doctors)
    elif patients - doctors > 0:
        patients_treated = patients_treated + doctors
        patients_untreated = patients_untreated + (patients - doctors)
    elif patients - doctors < 0:
        patients_treated = patients_treated + patients

            
            
print(f"Treated patients: {patients_treated}.")
print(f"Untreated patients: {patients_untreated}.")

    