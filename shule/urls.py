from django.urls import include, path

from . import views
from shule.nkviews import adminview, cachierview, secretaryview

# from shule.nkviews.cachierview import mainCachier

urlpatterns = [
    path('', views.shuleHome , name='shuleHome'), 

    path('admin/', include(([
        path('', adminview.adminHome, name='admin_home'),
        path('register_staff/', adminview.registerCachier, name="cachier"),
        path('register_sec/', adminview.registerSecretary, name='secretary'),
        path('get_staff/', adminview.postStaffList, name='staff_tbl'),
        path('country/state/city/', adminview.locationData, name="location"),
        path('request_admin_pk/', adminview.request_admin_pk, name='request_pk'),
        path('save_level/', adminview.addLevelClass, name='save_level'),
        path('select_level_classe/', adminview.selectLevelClasse, name='level_selection'),
        path('show_level_classe/', adminview.displayLevelClasse, name='display_level_classe'),
        path('show_level_details/', adminview.showLevelDetails, name='show_todo_level'),
        path('fee_type/', adminview.saveFeeCategory, name='feetype'),
        path('edit/employee/item/', adminview.editEmployeeItem, name="edit_employee_item"),
    ], 'shule'), namespace='admin')),



    path('cachier/', include(([
        path('', cachierview.mainCachier, name='cachier_home'),
        path('student_show_level_classe/', cachierview.getdisplayLevelClasse, name='display_level_classe'),
        path('search_student/', cachierview.searchStudent, name='searchstudent'),
        path('outlay/', cachierview.outlay, name='outlay'),
        path('outlay/sell/', cachierview.sellArticle, name="sellarticle"),
        path('outlay/repport/', cachierview.Rapport, name="checkoutrepport"),

    ], 'shule'), namespace='cachier')),

    path('secretary/', include(([
        path('', secretaryview.mainSecretary, name='secretary_home'),
        path('save_product/', secretaryview.saveProduct, name='saveproduct'),
        path('register_student/', secretaryview.registerStudent, name='studentregister'),
        path('show_level_classe/', secretaryview.displayLevelClasse, name='display_level_classe'),
        path('register_employee/', secretaryview.registerEmployee, name='employeeregister'),
        path('display_employee/', secretaryview.displayEmployee, name='displayemployee')

    ], 'shule'), namespace='secretary'))


]