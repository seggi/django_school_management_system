from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser



GENDER = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]

class ShuleUser(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_cachier = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False) 
    phone = models.IntegerField(null=True, blank=True)


# Default models 

class Month(models.Model):
    name = models.CharField(max_length=10)

class Country(models.Model):
	name = models.CharField(max_length=100)

class State(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

class City(models.Model):
	city = models.ForeignKey(State, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)


# Admin signup model

class Admin(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.ForeignKey(Country,max_length=50, on_delete=models.CASCADE, blank=True)
    state = models.ForeignKey(State,max_length=50, on_delete=models.CASCADE, blank=True)
    city = models.ForeignKey(City,max_length=50,on_delete=models.CASCADE,  blank=True)

    # def __str__(self):
    #     return str(self.country)

# Staff registration models << Staff will be registered by Admin >> 

class Staff(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=3, choices=GENDER)
    address = models.CharField(max_length=255,blank=True)



# Admin session management
# --------------------- Add level ----------------------
class Level(models.Model):
	shulde_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
	title = models.CharField(max_length=30)

class Classe(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

class Faculty(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

class Periode(models.Model):
	admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
	name = models.CharField(max_length=30)

class EmployFunction(models.Model):
    shulde_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)

# -------------------- Add Fee Type & payment --------------

class FeeType(models.Model):
	admin = models.ForeignKey(Admin, on_delete=models.CASCADE,)
	title = models.CharField(max_length= 50)

class FixePayment(models.Model):
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE,)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, null=True)
    feetype = models.ForeignKey(FeeType, on_delete=models.CASCADE)
    periode = models.ForeignKey(Periode, on_delete=models.CASCADE)
    amount = models.FloatField()
    tot_amount = models.FloatField()
    date =  models.DateTimeField(auto_now_add=True)


# Secretary session management 
#  --------------- Register student --------------------------
class RegisterStudent(models.Model):
    secretary = models.ForeignKey(Staff, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname =  models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=4)
    age = models.CharField(max_length=10)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

class Parents(models.Model):
    student = models.OneToOneField(RegisterStudent, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname =  models.CharField(max_length=50)
    nickname = models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=6)
    age = models.CharField(max_length=10)
    occupation =  models.CharField(max_length=20)
    
    city = models.CharField(max_length=50)
    quater = models.CharField(max_length=50)
    avenue = models.CharField(max_length=50)
    date =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# ------------------- Register Teachers ------------------------

class RegistrationEmployee(models.Model):
    secretary = models.ForeignKey(Staff, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    lastname =  models.CharField(max_length=50)
    nickname =  models.CharField(max_length=50, blank=True)
    sex = models.CharField(max_length=4)
    age = models.DateField()
    function = models.ForeignKey(EmployFunction, on_delete=models.CASCADE)
    email = models.CharField(max_length=30, blank=True)
    phone = models.IntegerField()

    def __str__(self):
        return self.name 

# Secondary session --------------------------------

class Course(models.Model):
    secretary = models.ForeignKey(Staff, on_delete=models.CASCADE)
    teacher = models.ForeignKey(RegistrationEmployee, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    date =  models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    secretary = models.ForeignKey(Staff, on_delete=models.CASCADE)
    article = models.TextField()
    quantity = models.IntegerField()
    unit_amount = models.FloatField()
    tot_amount = models.IntegerField()
    date =  models.DateTimeField(auto_now_add=True)


# ------------------Admin enchange --------------------------
class FixeEmployeeSalary(models.Model):
    # shulde_admin = models.ForeignKey(Admin, on_delete= models.CASCADE)
    employee = models.ForeignKey(RegistrationEmployee, on_delete=models.CASCADE)
    month = models.CharField(max_length=11)
    designation = models.TextField()
    amount = models.FloatField()
    salary = models.FloatField()
    date =  models.DateTimeField(auto_now_add=True)


# Cachier session management 


# ------------------ Auto fill student payment -----------------
class ProductSell(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    designation = models.TextField()
    sold_amount = models.FloatField()
    remaing = models.IntegerField()


class StudentPayment(models.Model):
    # student = models.ForeignKey(RegisterStudent, on_delete=models.CASCADE)
    # payment = models.ForeignKey(FixePayment, on_delete= models.CASCADE)
    student = models.IntegerField()
    payment = models.IntegerField()
    designation = models.TextField()
    amount = models.FloatField()
    totfee = models.FloatField()
    date =  models.DateTimeField(auto_now_add=True)

class EmployeeSalary(models.Model):
    cachier = models.ForeignKey(Staff, on_delete= models.CASCADE)
    employee_id = models.ForeignKey(RegistrationEmployee, on_delete=models.CASCADE)
    designation = models.TextField()
    amount = models.FloatField()
    tot_payment = models.FloatField()
    date =  models.DateTimeField(auto_now_add=True)

# -------------------- Cash out ------------------------

class RapportCaisse(models.Model):
    cachier = models.ForeignKey(Staff, on_delete= models.CASCADE)
    designation = models.TextField()
    debit = models.FloatField() #	From Student payment 
    credit = models.FloatField() # Frmm teachers payment and other outlay
    balance = models.FloatField() # From  debit- credit
    date =  models.DateTimeField(auto_now_add=True)





    















