from abc import ABC,abstractmethod
class Employee(ABC):
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.__salary = salary
        self.department = department

    def show(self):
        print("name:", self.name)
        print("salary:", self.__salary)
        print("age:", self.age)
        print("department:", self.department)

    def upd_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("error: invalid salary")

    @abstractmethod
    def perform_duty(self):
                    pass


#em1 = Employee("hind", 30, 3000, "doctor")
#em2 = Employee("ahmed", 40, 2000, "nurse")
#em3 = Employee("sara", 28, 2500, "pharmacy")

# إضافة كائنات الموظفين إلى القائمة
#emplo = [em1, em2, em3]

# عرض بيانات جميع الموظفين
#for employee in emplo:
   # employee.show()
    #print("----------------")
###الوراثه 
    
class Doctor(Employee):
    def __init__(self, name, age, salary, department, special):
        super().__init__(name, age, salary, department)
        self.special = special

    def perform_duty(self):
        print(self.name, "is a doctor. Speciality:", self.special)


class Nurse(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary, department)

    def perform_duty(self):
        print(self.name, "is taking care of patients")


class Pharmacist(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary, department)

    def perform_duty(self):
        print(self.name, "is dispensing medicine")


doctor1 = Doctor("Salwa", 44, 9000, "doctor", "Dentist")
doctor2= Doctor( "mona",44,8000,
"doctor","dinsat")
doctor1.show()
doctor1.perform_duty()
Nurse1= Nurse("huda",38,7000,"nurse")
Pharmacist1=Pharmacist("gwad",22,5000,"Pharmacist")


##بوليرفيزم
duty=[doctor1,Nurse1,Pharmacist1]
for employee in duty:
    employee.perform_duty()
    ##ABDALAZEEZ HASSABALLA
class Patient:
     def __init__(self,kEYNUMBER,name,age,digno):
          self.kEYNUMBER=kEYNUMBER
          self.name=name
          self.age=age
          self.digno=digno

     def  show(self):
          print(self.kEYNUMBER ,".",self.name,"is a patient he is"
                ,self.age,"years old his digno is",self.digno)   
Patient1=Patient(1,"awad",33,"headeke")
Patient2=Patient (2,"ziad",22,"fever")
Patient3=Patient(3,"sara",23,"sto")

pat=[Patient1,Patient2,Patient3]
for patient in pat:
    if patient.kEYNUMBER == 2:
        patient.show()


class Appointment:
    def __init__(self, id, patient, doctor, date, time):
        self.id = id
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def show_appo(self):
     print(self.id, "Patient name:", self.patient.name,
          "Doctor name:", self.doctor.name,
          "Date:", self.date,
          "Time:", self.time)
appointment1 = Appointment(
    1, Patient1, doctor1, "2026-11-13", "10:00 AM"
)
appointment2 = Appointment(
    2, Patient2, doctor1, "2026-11-13", "10:00 AM"
)
appointment3 = Appointment(
    3, Patient2, doctor2, "2026-11-13", "10:00 AM"
)
appo=[appointment1,appointment2,appointment3]
for appointment in appo:
    if appointment.id == 2:
        appointment.show_appo()
        


