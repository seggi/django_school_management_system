from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect , render

from shule.nkcore.decorators import secretary_required
from ..models import (Product, Staff, ProductSell, RegisterStudent, RegistrationEmployee,
                    FixeEmployeeSalary)
from shule.nkmodels import defaultdata, secmodels



STUDENT_GENDER = {'F': 'Fille', 'G': 'Garcon'}
GENDER = {'Ms': "Ms", 'Mr': "Mr", 'Mrs': "Mrs"}
MONTH = 'RAS'
DESIGNATION = 'RAS'
AMOUNT = 0
SALARY = 0



def displayProduct(secretary_id):
    get = secmodels.RequestProductDetails
    display = get.getProduct(secretary_id)
    return display

@login_required
@secretary_required
def displayLevelClasse(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    query = secmodels.GetLevel()
    if sec_session:
        display_level = query.selectLeveldb(get_id)
        display_classe = query.selectClassedb(get_id)
        display_faculty = query.selectFacultydb(get_id)
        bind = display_level + display_classe +  display_faculty
        return JsonResponse(bind, safe=False)
    return JsonResponse({'error': ''})


@login_required
@secretary_required
def saveProduct(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    get = secmodels.RequestProductDetails
    if request.method == 'POST' and 'hidden_article' in request.POST:
        article  =  request.POST.get('articles')
        quantity = request.POST.get('quantity')
        unit_price = request.POST.get('unit_price')
        tot_price = float(quantity) * float(unit_price)

        if article != '' and quantity != '' and unit_price != '':
            if Product.objects.filter(article=article, secretary_id=get_id).exists():
                return JsonResponse({'error': 'Ces donnees existent deja!'})
            else:
                save_product = Product(article=article, quantity=quantity, unit_amount=unit_price,
                                    tot_amount=tot_price, secretary_id=get_id)
                save_product.save()
                secmodels.extendProduct(get_id, quantity)
                return JsonResponse({"error": "Les données enregistrées avec succès"})
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})
    elif request.method == 'POST' and 'search_article' in request.POST:
        search = request.POST.get('search_article')
        if search != '':
            display_article = get.displayProductDetails(get_id, search)
            return JsonResponse(display_article, safe=False)
        else:
            return JsonResponse({'error': 'La list est vide'})

    return JsonResponse({'error': ''})


@login_required
@secretary_required
def registerStudent(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    extends = secmodels.StudentRegisterdb()
    if request.method == 'POST' and 'hidden_student1' in request.POST:
        first_name = request.POST.get('first_name')
        lastname =  request.POST.get('last_name')
        nickname = request.POST.get('nickname')
        sex = request.POST.get('sex')
        age = request.POST.get('age')
        level = request.POST.get('level')
        classe =  request.POST.get('classe')
        faculty = request.POST.get('faculty')

        # Parent 

        parent_name = request.POST.get('parent_name')
        parent_lastname =  request.POST.get('parent_lastname')
        gender = request.POST.get('parent_gender')
        address =  request.POST.get('location_address')
        phone  =  request.POST.get('phone')
        

        if first_name != '' and lastname != '' and sex != '' and\
            age != '' and level != '' and classe != '' and  parent_lastname != '' and\
                parent_lastname != '' and address != '' and phone != '':
            
            if RegisterStudent.objects.filter(name=first_name, lastname=lastname, sex=sex, level=level, 
                        classe=classe, faculty=faculty, secretary_id=get_id):
                        return JsonResponse({'error': 'Ces donnees existent deja!'})
            
            else:
                if faculty == None and nickname == '':
                    defaultfaculty = None
                    defaultnickname = 'RAS'
                    register = RegisterStudent(name=first_name, lastname=lastname, nickname=defaultnickname, sex=sex, age=age, classe_id=classe, 
                    faculty_id=defaultfaculty , level_id=level, secretary_id=get_id)
                    register.save()
                    extends.extendstudentregistration(get_id, parent_name, parent_lastname,gender, address, phone, level, classe, faculty)
                    
                    return JsonResponse({"error": "Les données enregistrées avec succès"})
                else:
                    register = RegisterStudent(name=first_name, lastname=lastname, nickname=nickname, sex=sex, age=age, classe_id=classe, 
                    faculty_id=faculty, level_id=level, secretary_id=get_id)
                    register.save()
                    extends.extendstudentregistration(get_id, parent_name, parent_lastname,gender, address, phone, level, classe, faculty)
                    
                    return JsonResponse({"error": "Les données enregistrées avec succès"})
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})

    elif request.method == 'POST' and 'student_level_hidden' in request.POST:
        search_student = request.POST.get('search_level')
        if search_student != '':
            display_students = extends.displayRegisteredStudent(get_id, search_student)
            return JsonResponse(display_students, safe=False)
        else:
            return JsonResponse({'error': 'La list est vide'})
        
    return JsonResponse({'error': ''})
            
                

@login_required
@secretary_required
def registerEmployee(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    if request.method == 'POST' and 'hidden_employee1' in request.POST:
        first_name = request.POST.get('first_name')
        lastname =  request.POST.get('last_name')
        nickname = request.POST.get('nickname')
        sex = request.POST.get('gender')
        age = request.POST.get('age')
        email = request.POST.get('email')
        phone =  request.POST.get('phone')
        function  = request.POST.get('employee_function')

        print(first_name, lastname, nickname, sex, age, email, phone, function)
        

        if first_name != '' and lastname != '' and sex != '' and\
            age != '' and email != '' and phone != '' and  function != '':

            if RegistrationEmployee.objects.filter(name=first_name, lastname=lastname, sex=sex, email=email, secretary_id=get_id):
                return JsonResponse({'error': 'Ces donnees existent deja!'})

            else:
                save_employee = RegistrationEmployee(name=first_name, lastname=lastname, nickname=nickname, 
                        sex=sex, age=age, email=email, phone=phone, function_id=function, secretary_id=get_id)
                save_employee.save()
                employee_salary  = FixeEmployeeSalary(month=MONTH, designation=DESIGNATION, amount=AMOUNT, salary=SALARY, employee_id=save_employee.id)
                employee_salary.save()
                return JsonResponse({"error": "Les données enregistrées avec succès"})
        else:
            
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})

    return JsonResponse({'error': ''})

@login_required
@secretary_required
def displayEmployee(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    query = secmodels.RegisterEmployee()
    if request.method == 'POST' and 'display_employee_work' in request.POST:
        search_employee = request.POST.get('display_employee_work')
        if search_employee != '':
            display_employees = query.displayRegisteredEmployee(get_id, search_employee)
            return JsonResponse(display_employees, safe=False)
        else:
            return JsonResponse({'error': 'La list est vide'})
        
    return JsonResponse({'error': ''})



@login_required
@secretary_required
def mainSecretary(request):
    sec_user = request.user.username 
    sec_session =  request.user.id 
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    template_name = "shule/staffs/secretary/mainpage.html"
    display_product  = displayProduct(get_id)
    display_level = secmodels.GetLevel.selectLeveldb(get_id)
    diplay_employee = secmodels.RegisterEmployee.employeeFunction(get_id)
    diplay_employees = secmodels.RegisterEmployee.displayEmployeeFunction(get_id)
    

    contents = {'username': sec_user, 'display_product': display_product, 
            'student_gender': STUDENT_GENDER , 'gender': GENDER, 
            'display_level': display_level, 'diplay_employee': diplay_employee, 
            'show_employee': diplay_employees}


    return render(request, template_name, contents)