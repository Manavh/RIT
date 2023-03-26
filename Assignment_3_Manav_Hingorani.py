#Assingment_3 Manav Hingorani

#Electronic Medical Record(EMR)

import csv
class physician:
#This is the SLOTS of the physician
    __slots__ =['__Id_','__name_', '__speciality_']
#This is the CONSTRUCTOR of the physician
    def __init__(self, id, name, speciality):
        self.__Id_ = id
        self.__name_ = name
        self.__speciality_ = speciality
#This is the accessors and mutators of all the required fields
    def set__Id_(self,id):
        self.__Id_=id
    def get__Id_(self):
        return self.__Id_
    def set__name_(self,name):
        self.__name_=name
    def get__name_(self):
        return self.__name_
    def set__specialty_(self,specialty):
        self.__specialty_=specialty
    def get__specialty_(self):
        return self.__specialty_
#This is the str (special method)of the Physician
    def __str__(self):
         return  '('+ (self.__Id_)+ (self.__name_) +(self.__speciality_)+')'
#This is the repr  (special method) of the physician     
    def __repr__(self):
        rep = '(' + self.__name_ + ',' + str(self.__Id_) + ',' + str(self.__speciality_)+ ')'
        return rep

#This is the class of the patient
class Patient: 
#this is the slots of the Patient
    __slots__=["__emr_id","__name","__gender","__phone_number"] 
#This is the constructor of the patient
    def __init__(self,emr_id,name,gender,number): 
        self.__emr_id=emr_id
      self.__name=name
        self.__gender=gender
        self.__phone_number=number
#These are accessors and mutators of the required field
    def set_emr_id(self,emr_id):
        self.__emr_id=emr_id
    def get_emr_id(self):
        return self.__emr_id
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_gender(self,gender):
        self.__gender=gender
    def get_gender(self):
        return self.__gender
    def set_phone_number(self,number):
        self.__phone_number=number
    def get_phone_number(self):
        return self.__phone_number
#This is the str(special method) of the patient
    def __str__(self):
        return '(' + (self.__emr_id) + (self.__name) + (self.__gender) +(self.__phone_number)+')'
#This is the repr(special method) of the patient
    def _repr_(self):
        return 'Patient(id={self.__emr_id},name={self.__name},gender={self.__gender},phone_number={self.__phone_number}'
#This is the class of the Encounter
class Encounter: 
#This is the constructor of the  Encounter
    def _init_(self,physician,patient,date,disease,medication): 
        self.physician=physician
        self.patient=patient
        self.date=date
        self.disease=disease
        self.medication=medication
#This is the repr of the encounter
    def _repr_(self):
        return 'Encounter(Physician_Assigned={self.physician},Patient={self.patient},Date={self.date},Disease={self.disease},Medication_Alloted={self.medication}'
#This is the list to store of the object
def main():
    physician1=[]
    with open ('physician.csv','r') as physician1:
        for row in physician1:
            core = row.strip().split(",")
            physician1.append(physician(core[0],core[1],core[2]))
    patient1=[]
    with open ('patients.csv','r') as patient1:
        for row in patient1:
            core = row.strip().split(",")
            patient1.append(Patient(core[0],core[1],core[2]))
        
    Encounter_1=[]
    #there are the 5 objects for Encounter 
    Encounter_1.append(Encounter('Dr.manav','jack','6-9-2021','Fever','crocine')) 
    Encounter_1.append(Encounter('Dr.manav','jill','10-6-2021','covid-19','paracetamol'))
    Encounter_1.append(Encounter('Dr.saad','james','8-8-2021','malaria','mdma'))
    Encounter_1.append(Encounter('Dr.saad','george','1-2-2021','diabeties','diabmedic'))
    Encounter_1.append(Encounter('Dr.julian','marie','7-12-2021','loose motion','clear23'))
    for i in physician1:
        print(str(i))
    for i in patient1:
        print(str(i))
    for i in Encounter_1:
        print(repr(i))
    with open('encounter.csv', 'w') as f:
        writer = csv.writer(f)
        for j in Encounter_1:
            writer.writer([j.patient,j.physician,j.date,j.disease,j.medication])
    
main()


        
        
