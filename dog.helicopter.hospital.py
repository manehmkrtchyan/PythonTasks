import datetime

class Patient:
    def __init__(self, name: 'str', age: 'int', gender: 'str'):
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = datetime.datetime.now()

    def __str__(self):
        return f"Patient(name='{self.name}', age={self.age}, gender='{self.gender}'"

class Hospital:
    def __init__(self, name: 'str', free_rooms: 'int'):
        self.name = name
        self.free_rooms = free_rooms
        self.patients = []
        self.doctors = []
        self.nurses = []
    
    def admit(self, patient):
        if len(self.patients) >= self.free_rooms:
            return "No more room in the hospital"
        self.patients.append(patient)
        return f"{patient.name} has been admitted to the hospital"
    
    def discharge(self, patient):
        if patient not in self.patients:
            return f"{patient.name} is not a patient in this hospital"
        self.patients.remove(patient)
        return f"{patient.name} has been discharged from the hospital"
    
    def assign_doctor(self, patient, doctor):
        if patient not in self.patients:
            return f"{patient.name} is not a patient in this hospital"
        if doctor not in self.doctors:
            return f"{doctor.name} is not a doctor in this hospital"
        patient.doctor = doctor
        return f"Doctor {doctor.name} has been assigned to {patient.name}"
    
    def assign_nurse(self, patient, nurse):
        if patient not in self.patients:
            return f"{patient.name} is not a patient in this hospital"
        if nurse not in self.nurses:
            return f"{nurse.name} is not a nurse in this hospital"
        patient.nurse = nurse
        return f"Nurse {nurse.name} has been assigned to {patient.name}"
    
    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        return f"{doctor.name} has been added to the hospital staff"
    
    def add_nurse(self, nurse):
        self.nurses.append(nurse)
        return f"{nurse.name} has been added to the hospital staff"

class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty

class Nurse:
    def __init__(self, name):
        self.name = name


patient1 = Patient('Anna', 19, 'female')
patient2 = Patient('Bob', 20, 'male')
doctor1 = Doctor('Artur', 'Cardelog')
doctor2 = Doctor('Narine', 'Ortodont')
nurse1 = Nurse('Hasmik')
nurse2 = Nurse('Karine')
AMC = Hospital('Astghik', 100)

print(patient1)
print(AMC.add_doctor(doctor1))
print(AMC.assign_doctor(patient1, doctor1))
print(AMC.admit(patient2))
print(AMC.add_nurse(nurse2))
print(AMC.assign_nurse(patient2, nurse2))

class Helicopter:
    def __init__(self) -> None:
        self.type = 'aircraft'
        self.engine_works= False
        self.position = [0, 0, 0] #[x,y,z]
        self.door_state = 'open'
    def close_the_door(self):
        self.door_state = 'closed'
        return('The door is closed, now you can start the flight.')
    def start_flying(self):
        if self.door_state == 'open':
            return('The door has to be closed!')
        else:
            self.engine_works = True
            if self.position[2] == 0:
                self.position[2] = 10
                return(f'Your coordinates are {self.position}. Have a nice flight.')
            return("You are already in the air.")
    def fly_to_right(self, how_much: 'float'):
        if self.engine_works:
            self.position[0] += how_much
            return(f'Youre coordinates are {self.position}.')
        return f'Engine is turned off. Start flying'
    def fly_to_left(self, how_much: 'float'):
        if self.engine_works:
            self.position[0] -= how_much
            return(f'Youre coordinates are {self.position}.')
        return f'Engine is turned off. Start flying'
    def fly_to_up(self, how_much: 'float'):
        if self.engine_works:
            self.position[1] += how_much
            return(f'Youre coordinates are {self.position}.')
        return f'Engine is turned off. Start flying'   
    def fly_to_down(self, how_much: 'float'):
        if self.engine_works:
            if self.position[2] - how_much >= 0:
                self.position[2] -= how_much
                return(f'Youre coordinates are {self.position}.')
            return(f'Cant do this action!')
        else:
            return f'Engine is turned off. Start flying'

helicopter = Helicopter()
print(helicopter.close_the_door())
print(helicopter.start_flying())
print(helicopter.fly_to_down(5))
print(helicopter.fly_to_left(4))
print(helicopter.fly_to_up(10))

class Dog:
    def __init__(self, name, breed, age, color) -> None:
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color
        self.state = "standing"
    def bark(self):
        print("Haf-haf!")
    def set_name(self, new_name):
        self.name = new_name
    def set_state(self, new_state:'str'):
        self.state = new_state
        print(f'Now {self.name} is {self.state}.')
    def get_name(self):
        print(self.name)
    def get_age(self):
        print(self.age)
    def get_breed(self):
        print(self.breed)
    def get_color(self):
        print(self.color)
    def eat(self, food):
        if food in {'apple', 'pear', 'chicken', 'beef', 'turkey', 'strawberries', 'carrots', 'rice', 'dog food'}:
            print(f'{self.name} is eatting {food} now.')
        else:
            print(f"{self.name} doesn't eat {food}")