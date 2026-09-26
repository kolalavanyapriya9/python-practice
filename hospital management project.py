#Department
class Department:
    def __init__(self, department_id, name, location):
        self.department_id = department_id
        self.name = name
        self.location = location

    def display(self):
        print(
            self.department_id,
            self.name,
            self.location
        )

#DOCTOR
class Doctor:
    def __init__(self, doctor_id, name, specialization, phone, email, department_id):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.phone = phone
        self.email = email
        self.department_id = department_id

    def display(self):
        print(
            self.doctor_id,
            self.name,
            self.specialization,
            self.phone,
            self.email,
            self.department_id
        )
#PATIENT
class Patient:
    def __init__(
        self,
        patient_id,
        name,
        dob,
        gender,
        phone,
        email,
        address,
        blood_group,
        emergency_contact
    ):
        self.patient_id = patient_id
        self.name = name
        self.dob = dob
        self.gender = gender
        self.phone = phone
        self.email = email
        self.address = address
        self.blood_group = blood_group
        self.emergency_contact = emergency_contact

    def display(self):
        print("\nPatient ID:", self.patient_id)
        print("Name:", self.name)
        print("DOB:", self.dob)
        print("Gender:", self.gender)
        print("Phone:", self.phone)
        print("Email:", self.email)
        print("Address:", self.address)
        print("Blood Group:", self.blood_group)
        print("Emergency Contact:", self.emergency_contact)
#STAFF
class Staff:
    def __init__(self, staff_id, name, role, phone, department_id, salary):
        self.staff_id = staff_id
        self.name = name
        self.role = role
        self.phone = phone
        self.department_id = department_id
        self.salary = salary

    def display(self):
        print(
            self.staff_id,
            self.name,
            self.role,
            self.phone,
            self.department_id,
            self.salary
        )
#APPOINTMENT
class Appointment:
    def __init__(self,appointment_id,patient_id,doctor_id,date,time,reason,status):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time
        self.reason = reason
        self.status = status

    def display(self):
        print(
            self.appointment_id,
            self.patient_id,
            self.doctor_id,
            self.date,
            self.time,
            self.reason,
            self.status
        )
#ROOM
class Room:
    def __init__(self, room_id, room_number, room_type, charge_per_day, status):
        self.room_id = room_id
        self.room_number = room_number
        self.room_type = room_type
        self.charge_per_day = charge_per_day
        self.status = status

    def display(self):
        print(
            self.room_id,
            self.room_number,
            self.room_type,
            self.charge_per_day,
            self.status
        )
#ADMISSION
class Admission:
    def __init__(self,admission_id,patient_id,doctor_id,room_id,admission_date,discharge_date,status):
        self.admission_id = admission_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.room_id = room_id
        self.admission_date = admission_date
        self.discharge_date = discharge_date
        self.status = status

    def display(self):
        print(
            self.admission_id,
            self.patient_id,
            self.doctor_id,
            self.room_id,
            self.admission_date,
            self.discharge_date,
            self.status
        )
#MEDICAL RECORD
class MedicalRecord:
    def __init__(self,record_id,patient_id,doctor_id,diagnosis,symptoms,treatment,date):
        self.record_id = record_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.diagnosis = diagnosis
        self.symptoms = symptoms
        self.treatment = treatment
        self.date = date

    def display(self):
        print("\nRecord ID:", self.record_id)
        print("Patient ID:", self.patient_id)
        print("Doctor ID:", self.doctor_id)
        print("Diagnosis:", self.diagnosis)
        print("Symptoms:", self.symptoms)
        print("Treatment:", self.treatment)
        print("Date:", self.date)
# MEDICINE
class Medicine:
    def __init__(self, medicine_id, name, category, price, stock):
        self.medicine_id = medicine_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def display(self):
        print(
            self.medicine_id,
            self.name,
            self.category,
            self.price,
            self.stock
        )
#PRESCRIPTION
class Prescription:
    def __init__(self,prescription_id,record_id,medicine_id,dosage,duration,instructions):
        self.prescription_id = prescription_id
        self.record_id = record_id
        self.medicine_id = medicine_id
        self.dosage = dosage
        self.duration = duration
        self.instructions = instructions

    def display(self):
        print(
            self.prescription_id,
            self.record_id,
            self.medicine_id,
            self.dosage,
            self.duration,
            self.instructions
        )
#LAB TEST 
class LabTest:
    def __init__(self,test_id,patient_id,doctor_id,test_name,test_date,result,amount):
        self.test_id = test_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.test_name = test_name
        self.test_date = test_date
        self.result = result
        self.amount = amount

    def display(self):
        print(
            self.test_id,
            self.patient_id,
            self.doctor_id,
            self.test_name,
            self.test_date,
            self.result,
            self.amount
        )

#BILLING
class Billing:
    def __init__(self,bill_id,patient_id,admission_id,consultation_fee,room_charge,medicine_charge,test_charge,payment_status,bill_date):
        self.bill_id = bill_id
        self.patient_id = patient_id
        self.admission_id = admission_id
        self.consultation_fee = consultation_fee
        self.room_charge = room_charge
        self.medicine_charge = medicine_charge
        self.test_charge = test_charge
        self.total_amount = (
            consultation_fee
            + room_charge
            + medicine_charge
            + test_charge
        )
        self.payment_status = payment_status
        self.bill_date = bill_date

    def display(self):
        print("\n========== BILL ==========")
        print("Bill ID:", self.bill_id)
        print("Patient ID:", self.patient_id)
        print("Admission ID:", self.admission_id)
        print("Consultation Fee:", self.consultation_fee)
        print("Room Charge:", self.room_charge)
        print("Medicine Charge:", self.medicine_charge)
        print("Test Charge:", self.test_charge)
        print("Total Amount:", self.total_amount)
        print("Payment Status:", self.payment_status)
        print("Bill Date:", self.bill_date)
#Hopsital management 
class Hospital:
    def __init__(self):
        self.departments = {}
        self.doctors = {}
        self.patients = {}
        self.staff = {}
        self.appointments = {}
        self.rooms = {}
        self.admissions = {}
        self.records = {}
        self.medicines = {}
        self.prescriptions = {}
        self.lab_tests = {}
        self.bills = {}
    # DEPARTMENT
    def add_department(self):
        department_id = input("Enter Department ID: ")
        if department_id in self.departments:
            print("Department ID already exists.")
            return
        name = input("Enter Department Name: ")
        location = input("Enter Location: ")
        obj = Department(department_id,name,location)
        self.departments[department_id] = obj
        print("Department added successfully.")

    def view_departments(self):
        if not self.departments:
            print("No departments found.")
            return
        print("\nID\tName\tLocation")
        for obj in self.departments.values():
            obj.display()
   # DOCTOR
    def add_doctor(self):
        doctor_id = input("Enter Doctor ID: ")
        if doctor_id in self.doctors:
            print("Doctor ID already exists.")
            return
        name = input("Enter Doctor Name: ")
        specialization = input("Enter Specialization: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        department_id = input("Enter Department ID: ")
        if department_id not in self.departments:
            print("Department does not exist.")
            return
        obj = Doctor(doctor_id,name,specialization,phone,email,department_id)
        self.doctors[doctor_id] = obj
        print("Doctor added successfully.")
    def view_doctors(self):
        if not self.doctors:
            print("No doctors found.")
            return
        for obj in self.doctors.values():
            obj.display()
    # PATIENT
    def add_patient(self):
        patient_id = input("Enter Patient ID: ")
        if patient_id in self.patients:
            print("Patient ID already exists.")
            return
        name = input("Enter Patient Name: ")
        dob = input("Enter Date of Birth: ")
        gender = input("Enter Gender: ")
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        blood_group = input("Enter Blood Group: ")
        emergency_contact = input("Enter Emergency Contact: ")
        obj = Patient(patient_id,name,dob,gender,phone,email,address,blood_group,emergency_contact)
        self.patients[patient_id] = obj
        print("Patient added successfully.")

    def view_patients(self):
        if not self.patients:
            print("No patients found.")
            return
        for obj in self.patients.values():
            obj.display()
    # STAFF
    def add_staff(self):
        staff_id = input("Enter Staff ID: ")
        if staff_id in self.staff:
            print("Staff ID already exists.")
            return
        name = input("Enter Staff Name: ")
        role = input("Enter Role: ")
        phone = input("Enter Phone: ")
        department_id = input("Enter Department ID: ")
        salary = float(input("Enter Salary: ")) 
        if department_id not in self.departments:
            print("Department does not exist.")
            return
        obj = Staff(staff_id,name,role,phone,department_id,salary)
        self.staff[staff_id] = obj
        print("Staff added successfully.")

    def view_staff(self):
        if not self.staff:
            print("No staff found.")
            return
        for obj in self.staff.values():
            obj.display()
    # APPOINTMENT
    def book_appointment(self):
        appointment_id = input("Enter Appointment ID: ")
        if appointment_id in self.appointments:
            print("Appointment ID already exists.")
            return
        patient_id = input("Enter Patient ID: ")
        if patient_id not in self.patients:
            print("Patient does not exist.")
            return
        doctor_id = input("Enter Doctor ID: ")
        if doctor_id not in self.doctors:
            print("Doctor does not exist.")
            return
        date = input("Enter Appointment Date: ")
        time = input("Enter Appointment Time: ")
        reason = input("Enter Reason: ")
        status = "Scheduled"
        obj = Appointment(appointment_id,patient_id,doctor_id,date,time,reason,status)
        self.appointments[appointment_id] = obj
        print("Appointment booked successfully.")

    def view_appointments(self):
        if not self.appointments:
            print("No appointments found.")
            return
        for obj in self.appointments.values():
            obj.display()
    # ROOM
    def add_room(self):
        room_id = input("Enter Room ID: ")
        if room_id in self.rooms:
            print("Room ID already exists.")
            return
        room_number = input("Enter Room Number: ")
        room_type = input("Enter Room Type: ")
        charge = float(input("Enter Charge Per Day: "))
        status = "Available"
        obj = Room(room_id,room_number,room_type,charge,status)
        self.rooms[room_id] = obj
        print("Room added successfully.")

    def view_rooms(self):
        if not self.rooms:
            print("No rooms found.")
            return
        for obj in self.rooms.values():
            obj.display()
    # ADMISSION
    def admit_patient(self):
        admission_id = input("Enter Admission ID: ")
        if admission_id in self.admissions:
            print("Admission ID already exists.")
            return
        patient_id = input("Enter Patient ID: ")
        if patient_id not in self.patients:
            print("Patient does not exist.")
            return
        doctor_id = input("Enter Doctor ID: ")
        if doctor_id not in self.doctors:
            print("Doctor does not exist.")
            return
        room_id = input("Enter Room ID: ")
        if room_id not in self.rooms:
            print("Room does not exist.")
            return
        if self.rooms[room_id].status != "Available":
            print("Room is not available.")
            return
        admission_date = input("Enter Admission Date: ")
        discharge_date = ""
        status = "Admitted"
        obj = Admission(admission_id,patient_id,doctor_id,room_id,admission_date,discharge_date,status)
        self.admissions[admission_id] = obj
        self.rooms[room_id].status = "Occupied"
        print("Patient admitted successfully.")

    def view_admissions(self):
        if not self.admissions:
            print("No admissions found.")
            return
        for obj in self.admissions.values():
            obj.display()
    # MEDICAL RECORD
    def add_medical_record(self):
        record_id = input("Enter Record ID: ")
        if record_id in self.records:
            print("Record ID already exists.")
            return
        patient_id = input("Enter Patient ID: ")
        if patient_id not in self.patients:
            print("Patient does not exist.")
            return
        doctor_id = input("Enter Doctor ID: ")
        if doctor_id not in self.doctors:
            print("Doctor does not exist.")
            return
        diagnosis = input("Enter Diagnosis: ")
        symptoms = input("Enter Symptoms: ")
        treatment = input("Enter Treatment: ")
        date = input("Enter Date: ")
        obj = MedicalRecord(record_id,patient_id,doctor_id,diagnosis,symptoms,treatment,date)
        self.records[record_id] = obj
        print("Medical record added successfully.")

    def view_medical_records(self):
        if not self.records:
            print("No medical records found.")
            return
        for obj in self.records.values():
            obj.display()
    # MEDICINE
    def add_medicine(self):
        medicine_id = input("Enter Medicine ID: ")
        if medicine_id in self.medicines:
            print("Medicine ID already exists.")
            return
        name = input("Enter Medicine Name: ")
        category = input("Enter Category: ")
        price = float(input("Enter Price: "))
        stock = int(input("Enter Stock: "))
        obj = Medicine(medicine_id,name,category,price,stock)
        self.medicines[medicine_id] = obj
        print("Medicine added successfully.")

    def view_medicines(self):
        if not self.medicines:
            print("No medicines found.")
            return
        for obj in self.medicines.values():
            obj.display()
    # PRESCRIPTION
    def add_prescription(self):
        prescription_id = input("Enter Prescription ID: ")
        if prescription_id in self.prescriptions:
            print("Prescription ID already exists.")
            return
        record_id = input("Enter Medical Record ID: ")
        if record_id not in self.records:
            print("Medical record does not exist.")
            return
        medicine_id = input("Enter Medicine ID: ")
        if medicine_id not in self.medicines:
            print("Medicine does not exist.")
            return
        if self.medicines[medicine_id].stock <= 0:
            print("Medicine is out of stock.")
            return
        dosage = input("Enter Dosage: ")
        duration = input("Enter Duration: ")
        instructions = input("Enter Instructions: ")
        obj = Prescription(prescription_id,record_id,medicine_id,dosage,duration,instructions)
        self.prescriptions[prescription_id] = obj
        self.medicines[medicine_id].stock -= 1
        print("Prescription added successfully.")

    def view_prescriptions(self):
        if not self.prescriptions:
            print("No prescriptions found.")
            return
        for obj in self.prescriptions.values():
            obj.display()
    # LAB TEST
    def add_lab_test(self):
        test_id = input("Enter Test ID: ")
        if test_id in self.lab_tests:
            print("Test ID already exists.")
            return
        patient_id = input("Enter Patient ID: ")
        if patient_id not in self.patients:
            print("Patient does not exist.")
            return
        doctor_id = input("Enter Doctor ID: ")
        if doctor_id not in self.doctors:
            print("Doctor does not exist.")
            return
        test_name = input("Enter Test Name: ")
        test_date = input("Enter Test Date: ")
        result = input("Enter Result: ")
        amount = float(input("Enter Test Amount: "))
        obj = LabTest(test_id,patient_id,doctor_id,test_name,test_date,result,amount)
        self.lab_tests[test_id] = obj
        print("Lab test added successfully.")

    def view_lab_tests(self):
        if not self.lab_tests:
            print("No lab tests found.")
            return
        for obj in self.lab_tests.values():
            obj.display()
    # BILLING
    def create_bill(self):
        bill_id = input("Enter Bill ID: ")
        if bill_id in self.bills:
            print("Bill ID already exists.")
            return
        patient_id = input("Enter Patient ID: ")
        if patient_id not in self.patients:
            print("Patient does not exist.")
            return
        admission_id = input("Enter Admission ID: ")
        if admission_id not in self.admissions:
            print("Admission does not exist.")
            return
        consultation_fee = float(input("Enter Consultation Fee: "))
        room_charge = float(input("Enter Room Charge: "))
        medicine_charge = float(input("Enter Medicine Charge: "))
        test_charge = float(input("Enter Test Charge: "))
        payment_status = input("Enter Payment Status (Paid/Pending): ")
        bill_date = input("Enter Bill Date: ")
        obj = Billing(bill_id,patient_id,admission_id,consultation_fee,room_charge,medicine_charge,test_charge,payment_status,bill_date)
        self.bills[bill_id] = obj
        print("Bill created successfully.")
        obj.display()
    def view_bills(self):
        if not self.bills:
            print("No bills found.")
            return
        for obj in self.bills.values():
            obj.display()
    # SEARCH PATIENT
    def search_patient(self):
        patient_id = input("Enter Patient ID: ")
        if patient_id in self.patients:
            self.patients[patient_id].display()
        else:
            print("Patient not found.")

#MAIN PROGRAM
hospital = Hospital()
while True:
    print("\n")
    print("""1.Add Department 2.View Departments 3.Add Doctor 4.View Doctors 5.Add Patient 6.View Patients 7.Search Patient 8.Add Staff 9.View Staff 10.Book Appointment 11.View Appointments 12.Add Room 13.View Rooms 14.Admit Patient 15.View Admissions 16.Add Medical Record 17.View Medical Records 18.Add Medicine 19.View Medicines 20.Add Prescription 21.View Prescriptions 22.Add Lab Test 23.View Lab Tests 24.Create Bill 25.View Bills 0.Exit""")
    print("\n")
    choice = input("Enter your choice: ")
    # Department
    if choice == "1":
        hospital.add_department()
    elif choice == "2":
        hospital.view_departments()
    # Doctor
    elif choice == "3":
        hospital.add_doctor()
    elif choice == "4":
        hospital.view_doctors()
    # Patient
    elif choice == "5":
        hospital.add_patient()
    elif choice == "6":
        hospital.view_patients()
    elif choice == "7":
        hospital.search_patient()
    # Staff
    elif choice == "8":
        hospital.add_staff()

    elif choice == "9":
        hospital.view_staff()
    # Appointment
    elif choice == "10":
        hospital.book_appointment()

    elif choice == "11":
        hospital.view_appointments()
    # Room
    elif choice == "12":
        hospital.add_room()
    elif choice == "13":
        hospital.view_rooms()
    # Admission
    elif choice == "14":
        hospital.admit_patient()
    elif choice == "15":
        hospital.view_admissions()
    # Medical Record
    elif choice == "16":
        hospital.add_medical_record()
    elif choice == "17":
        hospital.view_medical_records()
    # Medicine
    elif choice == "18":
        hospital.add_medicine()
    elif choice == "19":
        hospital.view_medicines()
    # Prescription
    elif choice == "20":
        hospital.add_prescription()
    elif choice == "21":
        hospital.view_prescriptions()
    # Lab Test
    elif choice == "22":
        hospital.add_lab_test()
    elif choice == "23":
        hospital.view_lab_tests()
    # Billing
    elif choice == "24":
        hospital.create_bill()
    elif choice == "25":
        hospital.view_bills()
    # Exit
    elif choice == "0":
        print("Thank you for using Hospital Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
 