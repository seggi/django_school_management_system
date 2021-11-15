from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect , render

from shule.nkcore.decorators import cachier_required
from shule.nkmodels import defaultdata , secmodels, cachiermodels, extendcachiermodels
from shule.nkcore.compute import *
from shule.nkcore.autodata import ManageEmployeeSalay, SellProduct, ManagePayment
from shule.models import EmployeeSalary


EXTEND_CACHIER = extendcachiermodels.Outlay()
SAVE_PAYMENT = EmployeeSalary()


@login_required
@cachier_required
def searchStudent(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    query = cachiermodels.StudentPayment()
    if request.method == "POST" and 'result_hidden' in request.POST:
        student_level = request.POST.get('student_level')
        student_classe = request.POST.get('student_classe')
        student_facutly = request.POST.get('student_facutly')
        searchinput1 =  request.POST.get('searchinput1')
        searchinput2 = request.POST.get('searchinput2')
        searchinput3 = request.POST.get('searchinput3')

        if student_level != '' and student_classe != '' and student_facutly != '' and \
            searchinput1 != '' and searchinput2 != '' :

            result = query.displayStudentContent(get_id, student_level, student_classe, student_facutly, 
                    searchinput1, searchinput2, searchinput3)
            return JsonResponse(result, safe=False)
        return JsonResponse({'error':'Toutes les cases doivent etre remplis'})

    elif request.method == 'POST' and 'get_student_id' in request.POST:
        paymenttype  =  request.POST.get('payementtype_id')
        designation = request.POST.get('designation_amount')
        amount = request.POST.get('save_student_payment')
        student_id = request.POST.get('get_student_id')

        if paymenttype != '' and designation != '' and amount != '':
            record_amount = RecordPayment(student_id, get_id, paymenttype, amount, designation)
            display = record_amount.amountComputer()
            return JsonResponse(display, safe=False)
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})

    elif request.method == 'POST' and 'result_hidden1' in request.POST:
        student_details_id = request.POST.get('result_hidden1')
        if student_details_id != '':
            query_student_histo = QueryStudentPayment.retrieveStudentHistoriqueGlobal(student_details_id)
            if len(query_student_histo) > 0:
                return JsonResponse(query_student_histo, safe=False)
            else:
                return JsonResponse({'error':'Desole!, il ya une erreur de communication avec le serveur!'}, safe=False)
        else:
            return JsonResponse({'error':'Error no data!'})

    elif request.method == 'POST' and 'fee_type_cachier' in request.POST:
        student_level1 = request.POST.get('student_level1')
        if student_level1 != '':
            if student_level1 != None:
                query_fee_category = QueryStudentPayment.displayLevelCachier(get_id, student_level1)
                return JsonResponse(query_fee_category, safe=False)
            else:
                return JsonResponse({'error': 'Vous devez faire un choix'})
        else:
            return JsonResponse({'error': 'Vous devez faire un choix'})

    elif request.method == 'POST' and 'range_student_u' in request.POST:
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        student_id = request.POST.get('range_student_u')
        print(date1, date2, student_id,'//////////')

        if date1 != '' and date2 != '':
            query_fee_histo  =  QueryStudentPayment.retrieveStudentHistoPeriode(student_id, date1, date2)
            if len(query_fee_histo) > 0:
                return JsonResponse(query_fee_histo, safe=False)
            else :
                return JsonResponse({'error':"Desole!, pas des donnes enregistre pour ce periode."}, safe=False)

        else:
            return JsonResponse({'error':'Error no data!'})

    elif request.method == 'POST' and 'range_student_r' in request.POST:
        date1 = request.POST.get('date1')
        date2 = request.POST.get('date2')
        student_level1 =  request.POST.get('student_level1')
        student_classe1 = request.POST.get('student_classe1')
        student_facutly1 = request.POST.get('student_facutly1')
        amount_to_search = request.POST.get('amount_to_search')
        ranges = request.POST.get('ranges')

        if date1 != '' and date2 != '' and student_level1 != '' and student_classe1 !=''\
            and student_level1 != '' and student_classe1 != '' and student_facutly1  != '' and ranges != '': 
            
            recorver_student = ComputePayment(level=student_level1, classe=student_classe1, faculty=student_facutly1,
                    date1=date1, date2=date2, user_id=get_id, amount_max=amount_to_search, ranges=ranges)
            print(recorver_student.computeData())
            return JsonResponse(recorver_student.computeData(), safe=False)
        
        else:
            return JsonResponse({'error':'Toutes les cases doivent etre remplis'})


    return JsonResponse({'error': ''})


@login_required
@cachier_required
def outlay(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    if request.method == 'POST' and 'employee_function' in request.POST:
        employee = request.POST.get('employee_function')
        if employee != '':
            display_employee = EXTEND_CACHIER.displayEmployee(user_id=get_id, employee_id=employee)
    
            return JsonResponse(display_employee, safe=False)
        else:
            return JsonResponse({'error':'Vous devez faire une selection'})
    
    elif request.method == 'POST' and 'employee_detail' in request.POST:
        employeedetails = request.POST.get('employee_detail')
        details = EXTEND_CACHIER.employeeDetails(get_id, employeedetails)
        if len(details) > 0:
            return JsonResponse(details, safe=False)
        else:
            return JsonResponse({'error': "Rien a signale sur cette personne."})
    
    elif request.method == 'POST' and 'histo_employee' in request.POST:
        histo = request.POST.get("histo_employee")
        display_histo = EXTEND_CACHIER.employeeHistory(get_id, histo)
        if len(display_histo) > 0 :
            return JsonResponse(display_histo, safe=False)
        else:
            return JsonResponse({'error': "Aucune historique sur cette personne."})

    elif request.method == 'POST' and "employee_id_avance" in request.POST:
        employee_id = request.POST.get("employee_id_avance")
        avance_amount = request.POST.get("entre_amount")
        designation = request.POST.get("designation")
        
        if employee_id != "" and avance_amount != "" and designation != "":
            manage = ManageEmployeeSalay(db=EXTEND_CACHIER, jsonify=JsonResponse,user_id=get_id, 
                    employee_id=employee_id, amount=avance_amount, designation=designation)
            return manage.salaryChecking()

        else:
            return JsonResponse({'error': 'La case ne doit pas rester vide!'})

    elif request.method == 'POST' and 'dps_id_avance' in request.POST:
        avance_amount = request.POST.get("entre_amount")
        designation = request.POST.get("designation")

        if designation != "" and avance_amount != "":
            manage = ManagePayment(db=EXTEND_CACHIER, jsonify=JsonResponse, user_id=get_id, 
                amount=avance_amount, designation=designation)
            manage.computePayment()
            payment =  EXTEND_CACHIER.displayCredit(get_id)
            sumpayment = EXTEND_CACHIER.displaySumCredit(get_id)
            bind = [payment, sumpayment]
            if len(payment) > 0 and len(sumpayment) > 0:
                return JsonResponse(bind, safe=False)
            else:
                return JsonResponse({'error': "Le stock pour ce produit est vide!"})
        else:
            return JsonResponse({'error': 'La case ne doit pas rester vide!'})
    
    elif request.method == 'POST' and 'dps-histo' in request.POST:
        payment =  EXTEND_CACHIER.displayCredit(get_id)
        sumpayment = EXTEND_CACHIER.displaySumCredit(get_id)
        bind = [payment, sumpayment]
        if len(payment) > 0 and len(sumpayment) > 0:
            return JsonResponse(bind, safe=False)
        else:
            return JsonResponse({'error': "Le stock pour ce produit est vide!"})
       
    return JsonResponse({'error': ''})


@login_required
@cachier_required
def sellArticle(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    if request.method == "POST" and 'article_hidden' in request.POST:
        article = request.POST.get("article_function")
        
        if article != "":
            show_article = EXTEND_CACHIER.showArticleSelling(article)
            show_sum = EXTEND_CACHIER.getProductSoldBalance(article)
            bind = [show_article, show_sum]
            if len(show_article) > 0  and len(show_sum)  > 0:
                return JsonResponse(bind, safe=False)
            else:
                return JsonResponse({'error': "Aucun article deja enregistre."})
        else:
            return JsonResponse({'error': 'La case ne doit pas rester vide!'})
    
    elif request.method == "POST" and "article_sold_amount" in request.POST:
        article_function = request.POST.get("article_function")
        designation = request.POST.get("designation")
        entre_amount = request.POST.get("entre_amount")

        if article_function != '' and designation != '' and entre_amount != '':
            manage_product = SellProduct(article=article_function , designation=designation, 
                entre_amount=entre_amount, jsonify=JsonResponse, db=EXTEND_CACHIER, user_id=get_id)
            manage_product.manageSelling()
            show_article = EXTEND_CACHIER.showArticleSelling(article_function)
            show_sum = EXTEND_CACHIER.getProductSoldBalance(article_function)
            bind = [show_article, show_sum]
            if len(show_article) > 0 and len(show_sum) > 0:
                return JsonResponse(bind, safe=False)
            else:
                return JsonResponse({'error': "Aucun article deja enregistre."})
        else:
            return JsonResponse({'error': 'La case ne doit pas rester vide!'})

    return JsonResponse({'error': ''})    


@login_required
@cachier_required
def Rapport(request):
    sec_session = request.user.id
    get_id = defaultdata.AccountStaff.secobject(sec_session)

    if request.method == "POST" and "stdpaiements" in request.POST:
        stdpaiements = request.POST.get("stdpaiements")
        if stdpaiements != None:
            displaypayement = EXTEND_CACHIER.getStudentPaymentHisto(stdpaiements)
            displaysum = EXTEND_CACHIER.getStudentPaymentSum(stdpaiements)
            bind = [displaypayement, displaysum]
            if len(displaypayement) > 0 and len(displaysum) > 0:
                return JsonResponse(bind, safe=False)
            else:
                return JsonResponse({'error': "Pas d'elements a montre"})
        else:
            return JsonResponse({'error': "Error"}) 
    
    elif request.method == "POST" and "mixhisto" in request.POST:
        displayMixhisto = EXTEND_CACHIER.repportAllHistoMix(get_id)
        displaySumix = EXTEND_CACHIER.repportAllSumMix(get_id)
        bind = [displayMixhisto, displaySumix]

        if len(displayMixhisto) > 0 and len(displaySumix) > 0:
            return JsonResponse(bind, safe=False)
        else:
            return JsonResponse({'error': "Pas d'elements a montre"})

    elif request.method == "POST" and "repportSell" in request.POST:
        displaysellsum = EXTEND_CACHIER.repportSellArticleSum()
        displaysellAll = EXTEND_CACHIER.repportSellArticleAll()
        bind = [displaysellAll, displaysellsum]

        if len(displaysellsum) > 0 and len(displaysellAll) > 0:
            return JsonResponse(bind, safe=False)
        else:
            return JsonResponse({'error': "Pas d'elements a montre"})

    return JsonResponse({'error': ''})

        


@login_required
@cachier_required
def getdisplayLevelClasse(request):
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
@cachier_required
def mainCachier(request):
    sec_user = request.user.username 
    sec_session =  request.user.id 
    get_id = defaultdata.AccountStaff.secobject(sec_session)
    MSPAY = 'Pas de mouvement!'
    
    template_name = 'shule/staffs/cachier/mainpage.html'
    show_student = cachiermodels.StudentPayment.getAdminId(get_id)
    payementtype = cachiermodels.StudentPayment.paymentType(get_id)
    show_employee = cachiermodels.getEmplyeeFunction(get_id)
    displayarticle = EXTEND_CACHIER.displayAticle(get_id)

    studentTodaypayement =  EXTEND_CACHIER.sumUpStudentPayment()
    sellTodaypayment =  EXTEND_CACHIER.sumUpSellPayment()
    todypayements  =  EXTEND_CACHIER.sumUpPayment()
    showlevel = EXTEND_CACHIER.showAllLevel()
    dpsToday = EXTEND_CACHIER.getTodayPayment()

    contents = {'username': sec_user, 'payementtype': payementtype, 'show_employee': show_employee, 
         'articleCategory': displayarticle, 'studentTodaypayement': studentTodaypayement,
         'sellTodaypayment': sellTodaypayment, 'todypayements': todypayements, 'msgpay': MSPAY,
         'showlevel': showlevel, 'dpsToday': dpsToday
        }
    return render(request, template_name, contents)