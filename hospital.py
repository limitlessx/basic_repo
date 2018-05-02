class patient(object):
  bed_num=0
  id = 0
  def __init__(self, name, allergies):
    patient.id = patient.id+1
    self.name = name
    self.allergies = allergies
    patient.bed_num = patient.bed_num +1
    #self.display_patient_info()
    
  def display_patient_info(self):
    print "id: {}\nname: {}\nallergies: {}\nbed_num: {}\n".format(patient.id,self.name.title(),self.allergies.title(),patient.bed_num)

    
class hospital(object):
  def __init__(self,name):
    self.patients =[]
    self.hospital_name = name
    self.capacity = 3
    print "Welcome to", self.hospital_name.title(), "\n"
    
  def admit(self,new_patient):
    if len(self.patients)>=self.capacity:
      print 'the hospital is full'
    else:
      self.patients.append(new_patient)
  
  def spaces(self):
    self.left=self.capacity-len(self.patients)
    print  "currently {} bed(s) are available \n".format(self.left)
  
  def discharge(self,num):
    self.patients.pop(num)
  
  def info(self):
    for i in self.patients:
       i.display_patient_info()
    
      
patient1=patient('john wang', 'peatnut')
patient2=patient('wanda beach', 'coconut')
patient3=patient('jessica huang', 'icecream')
patient4=patient('trang nyu', 'rice')
#patient5=patient('kevin low', 'bbq')


one=hospital("kaiser")
one.admit(patient1)
one.admit(patient2)
one.admit(patient3)
one.spaces()
one.admit(patient4)
one.discharge(0)
one.spaces()
#one.admit(patient5)
#one.spaces()

one.info()