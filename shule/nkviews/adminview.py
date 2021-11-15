from django.contrib.auth import login, authenticate
from django.shortcuts import redirect , render
from django.views.generic import CreateView 
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView

from shule.nkcore.decorators import admin_required
from shule.nkforms.adminform import ShuleAdminSignUpForm,\
            RegisterCachierForm, RegisterSecretaryForm
from shule.nkmodels.defaultdata import DefaultLocation
from ..models import ShuleUser, Admin, Staff
from shule.nkmodels import adminmodels



NOTIFICATION = 'Entrez le chiffre dans la case "Classes organisez" '\
                  'qui correspons aux classes que vous organisez\n'
NOTIFICATION1 =  'Ex: 1eme, 2eme... \n'\
                  'Entrez le chiffre 1 ou 2'


# Shule Admin signup session then redirect to shule_admin

class ShuleAdminSignUpView(CreateView):
    model = ShuleUser
    form_class = ShuleAdminSignUpForm
    template_name = 'registration/signup_admin.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admin:admin_home')

# -------------------------------------------------
#  display by default

def locationData(request):
    location = DefaultLocation()
    if True:
        country = location.countries()
        state = location.states()
        city = location.cities()
        bind = country + state + city

        return JsonResponse(bind, safe=False)
    return JsonResponse({'error': ""})

class AdminRequestData:
    dict_functions = { 'is_cachier': 'Caissier', 'is_secretary': 'Secretaire'}
    
        
# -------------------------------------------------
# Shule admin  login  session and start main page 

@login_required
@admin_required
def request_admin_pk(request):
    pk = request.user.id
    if pk != None:
        admin = Admin.objects.get(user_id=pk)
        return JsonResponse({'pk': admin.id})
    return JsonResponse({"error": ''})

# Register cacahier......

@login_required
@admin_required
def registerCachier(request):
    cachier_form = RegisterCachierForm(request.POST)
    if request.is_ajax and request.method == 'POST':
        if cachier_form.is_valid():
            cachier_form.save()
            return JsonResponse({"error": "Les données enregistrées avec succès"})
        
        else:
            return JsonResponse({"error": "Ooops!, Les données ne sont pas enregistrées."})

    return JsonResponse({'error': ''})


# Regiter secretary.....

# @login_required
# @admin_required
# def registerSecretary(request):
#     secretary_form = RegisterSecretaryForm(request.POST)
#     if request.method == 'POST':
#         if secretary_form.is_valid():
#             secretary_form.save()
#             return JsonResponse({"error": "Les données enregistrées avec succès"})
        
#         else:
#             print(secretary_form.errors.as_data())
#             return JsonResponse({"error": "Ooops!, Les données ne sont pas enregistrées."})

#     return JsonResponse({'error': ''})

@login_required
@admin_required
def registerSecretary(request):
    secretary_form = RegisterSecretaryForm(request.POST)
    if request.is_ajax and request.method == 'POST':
        if secretary_form.is_valid():
            secretary_form.save()
            return JsonResponse({"error": "Les données enregistrées avec succès"})
        else:
            print(secretary_form.errors.as_data())
            return JsonResponse({"error": "Ooops!, Les données ne sont pas enregistrées."})
    return JsonResponse({'error': ''})


# Display cachier, secretary list to the table...

@login_required
@admin_required
def postStaffList(request):
    pk = request.user.id
    admin = Admin.objects.get(user_id=pk)
    get_staff = adminmodels.RequestStaff()
    if request.is_ajax and request.method == 'POST':
        pick_table = request.POST.get('admin-fonction')
        display_tbl = get_staff.displayStaffListdb(admin.id, pick_table)
        if len(display_tbl) > 0:
            return JsonResponse(display_tbl, safe=False)
        else:
            return JsonResponse({"msg": 'La list est encore vide!'})
    
    return JsonResponse({"msg": 'La list est encore vide!'})

# Display Employee details and Edit salary....

@login_required
@admin_required
def editEmployeeItem(request):
    pk = request.user.id
    admin = Admin.objects.get(user_id=pk)
    get_staff = adminmodels.RequestStaff()
    if request.method == "POST" and "getftn" in request.POST:
        getFunction =  request.POST.get("getftn")
        if getFunction != None:
            display = get_staff.showEMployeeDetails(admin, getFunction)
            if len(display) > 0:
                return JsonResponse(display, safe=False)
            else:
                return JsonResponse({"msg": 'La list est encore vide!'})

    elif request.method == "POST" and "rmv_emp" in request.POST:
        rmv = request.POST.get("rmv_emp")
        if rmv != None:
            reloads = get_staff.removeEmployee(rmv)
            if len(reloads) > 0:
                return JsonResponse(reloads, safe=False)
            else:
                return JsonResponse({'error': 'La list est vide!'})
        else:
            return JsonResponse({'error': 'Error'})

    elif request.method == "POST" and "edt_emp" in request.POST:
        employee_id =  request.POST.get("edt_emp")
    
        if employee_id != None:
            return JsonResponse(get_staff.getItemToEdit(employee_id), safe=False)
        else:
            return JsonResponse({'error': 'Error'})

    elif request.method == "POST" and "get_item_id" in request.POST:
        name = request.POST.get("name")
        lastname =  request.POST.get("lastname")
        nickname =  request.POST.get("nickname")
        salary = request.POST.get("salary")
        getitemid =  request.POST.get("get_item_id")

        if name != "" and lastname != "" and nickname != "" and salary != "" and getitemid != None:
            updated = get_staff.updateEmployeeItem(name, lastname, nickname, salary, getitemid)
            return JsonResponse(updated, safe=False)
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})
        
    return JsonResponse({"msg": 'La list est encore vide!'})


# Add classes.......

from shule.nkcore.autodata import GenerateClasses
from shule.nkmodels.adminmodels import AddLeveldb, FeePayment
from ..models import Level, Classe, Faculty, FeeType, FixePayment, Periode,\
    EmployFunction

@login_required
@admin_required
def addLevelClass(request):
    pk = request.user.id
    admin = Admin.objects.get(user_id=pk)
    generator = GenerateClasses()
    if request.method == "POST":
        level = request.POST.get('niveau')
        classes = request.POST.get('classes')
        if level != '' and classes != '':
            get_word = generator.generatorClasseWord(classes)
            if Level.objects.filter(title=level, shulde_admin_id=admin.id):
                return JsonResponse({'error': 'Ces donnees existent deja!'})

            else:
                save_level = AddLeveldb.saveLeveldb(admin.id, level)
                save_level(get_word)
                return JsonResponse({"error": "Les données enregistrées avec succès"})
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})
    return JsonResponse({'error': ''})

@login_required
@admin_required
def displayLevelClasse(request):
    pk = request.user.id
    admin = Admin.objects.get(user_id=pk)
    if pk:
        display_level = AddLeveldb.selectLeveldb(admin.id)
        display_classe = AddLeveldb.selectClassedb(admin.id)
        display_faculty = AddLeveldb.selectFacultydb(admin.id)
        bind = display_level + display_classe +  display_faculty
        return JsonResponse(bind, safe=False)
    return JsonResponse({'error': ''})


@login_required
@admin_required
def selectLevelClasse(request):
    pk = request.user.id
    admin = Admin.objects.get(user_id=pk)
    if request.method == 'POST':
        select_level = request.POST.get('select_level')
        select_classe = request.POST.get('select_classe')
        get_faculty = request.POST.get('add_faculte')

        if select_level != '' and select_classe != '' and get_faculty != '':
            if Faculty.objects.filter(title=get_faculty, classe_id=select_classe):
                return JsonResponse({'error': 'Ces donnees existent deja!'})
            else: 
                AddLeveldb.saveLevelClassedb(get_faculty, select_classe)
                return JsonResponse({"error": "Les données enregistrées avec succès"})

        return JsonResponse({'error':'Toutes les cases doivent etre remplis'})
    return JsonResponse({'error': ''})

@login_required
@admin_required
def showLevelDetails(request):
    pk = request.user.id
    admin = Admin.objects.get(user_id=pk) 
    if request.method == 'POST':
        select = request.POST.get('display_level_list')
        if select != '':
            display = AddLeveldb.displayLevelClasseFacultydb(admin.id, select)
            return JsonResponse(display, safe=False)
    return JsonResponse({'error':  ''})



# Fee session......................

def displayFeeType(school_id):
    fee = FeePayment()
    display = fee.displayFeetype(school_id)
    return display

def displayPaymentPeriode(school_id):
    periode = FeePayment()
    display = periode.displayPriode(school_id)
    return display

def displayEmployeeFunction(school_id):
    function = FeePayment()
    display = function.displayEmployeeFunctiondb(school_id)
    return display

@login_required
@admin_required
def saveFeeCategory(request):
    pk = request.user.id
    admin = Admin.objects.get(user_id=pk) 
    if request.method == 'POST' and 'type-frais' in request.POST :
        save_fee = request.POST.get('type-frais')
        if save_fee != '':
            if FeeType.objects.filter(title=save_fee, admin=admin.id):
                return JsonResponse({'error': 'Ces donnees existent deja!'})
            else:
                save_new_type = FeeType(title=save_fee, admin_id=admin.id)
                save_new_type.save()
                return JsonResponse({"error": "Les données enregistrées avec succès"})
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})


    elif request.method == 'POST' and 'add_period' in request.POST:
        save_periode = request.POST.get('periode')
        if save_periode != '':
            if Periode.objects.filter(name=save_periode, admin=admin.id):
                 return JsonResponse({'error': 'Ces donnees existent deja!'})
            else:
                save_periode = Periode(name=save_periode, admin_id=admin.id)
                save_periode.save()
                return JsonResponse({"error": "Les données enregistrées avec succès"})
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})


    elif request.method == 'POST' and 'input_save_payment' in request.POST:
        level = request.POST.get('select_level1')
        classe = request.POST.get('select_classe1')
        faculty =  request.POST.get('selected_facutly1')
        fee_type = request.POST.get('select_fee_type')
        periode = request.POST.get('periode')
        tot_amount = request.POST.get('tot_amount')
        intervalle = request.POST.get('fixe_payment_periode')
        if level != '' and classe != '' and faculty != '' and fee_type != '' and periode != '' and\
            tot_amount != '' and intervalle != '':
            if FixePayment.objects.filter(admin_id=admin.id , level_id=level, classe_id=classe, periode=periode ):
                return JsonResponse({'error': 'Ces donnees existent deja!'})

            else: 
                if faculty == None:
                    fixe_payment = FixePayment(amount=intervalle, tot_amount=tot_amount, admin_id=admin.id,
                        classe_id=classe, faculty_id='', feetype_id=fee_type, level_id=level, periode_id=periode)
                    fixe_payment.save()
                    return JsonResponse({"error": "Les données enregistrées avec succès"})
                else:
                    fixe_payment = FixePayment(amount=intervalle, tot_amount=tot_amount, admin_id=admin.id,
                        classe_id=classe, faculty_id=faculty, feetype_id=fee_type, level_id=level, periode_id=periode)
                    fixe_payment.save()
                    return JsonResponse({"error": "Les données enregistrées avec succès"})
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})

    elif request.method == 'POST' and 'fee_search1' in request.POST:
        search_fee = request.POST.get('fee_search1')
        if search_fee != '':
            payment_details =  FeePayment.displayPayementDetails(admin.id, search_fee)
            return JsonResponse(payment_details, safe=False)
        
        else:
            return JsonResponse({'error': 'La list est vide'})

    # Add personnele

    elif request.method == 'POST' and 'personnel' in request.POST:
        save_personnel = request.POST.get('personnel')
        if save_personnel != '':
            if EmployFunction.objects.filter(title=save_personnel, shulde_admin_id=admin.id):
                return JsonResponse({'error': 'Ces donnees existent deja!'})
            else:
                personnel  = EmployFunction(title=save_personnel, shulde_admin_id=admin.id)
                personnel.save()
                return JsonResponse({"error": "Les données enregistrées avec succès"})
        return JsonResponse({'error':'Toutes les cases doivent etre remplis'})
        
    return JsonResponse({'msg': ''})


@login_required
@admin_required
def adminHome(request):
    school_name = request.user.first_name
    school_id = request.user.id
    admin = Admin.objects.get(user_id=school_id)
    template_name =  "shule/admin/home.html"
    cachier_form = RegisterCachierForm(request.POST)
    sec_form = RegisterSecretaryForm(request.POST)
    staff_list = AdminRequestData()
    fee_type = displayFeeType(admin.id)
    periode = displayPaymentPeriode(admin.id)
    emplyfunction = displayEmployeeFunction(admin.id)

    return render(request, template_name, {'school_name': school_name,'school_id':school_id,
                'cachier_form': cachier_form, 'sec_form': sec_form, 'fee_type': fee_type, 'payment_periode': periode ,
                'employeFunc': emplyfunction,
                'fonctions': staff_list.dict_functions, 'notice': NOTIFICATION , 'notice1': NOTIFICATION1})



