from django.db import connection
from shule.nkmodels.adminmodels import FeePayment

class StudentPayment:
    @staticmethod
    def paymentType(user_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_feetype.id, shule_feetype.title FROM shule_feetype LEFT JOIN 
                    shule_admin ON shule_admin.id = shule_feetype.admin_id LEFT JOIN shule_staff ON 
                    shule_staff.admin_id = shule_admin.id WHERE shule_staff.id = {user_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                rowdicts.append(newdict)
            return rowdicts

    @staticmethod
    def getAdminId(user_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT admin_id from shule_staff WHERE id={user_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                for ids in newdict:
                    rowdicts.append(StudentPayment.displayStudentNames(newdict[ids]))
            return rowdicts[0]

    @staticmethod
    def displayStudentNames(admin_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_registerstudent.name, shule_registerstudent.lastname FROM shule_registerstudent 
                LEFT JOIN shule_staff ON shule_staff.id = shule_registerstudent.secretary_id 
                LEFT JOIN shule_admin ON shule_admin.id = shule_staff.admin_id WHERE shule_staff.admin_id = {admin_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                rowdicts.append(newdict)
               
            return rowdicts

    @staticmethod
    def displayStudentContent(user_id, student_level, student_classe, student_facutly, 
                    searchinput1, searchinput2, searchinput3):

         with connection.cursor() as cursor:
            cursor.execute(f"""SELECT admin_id from shule_staff WHERE id={user_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                for ids in newdict:
                    rowdicts.append(StudentPayment.getData(newdict[ids], student_level, student_classe, student_facutly, 
                            searchinput1, searchinput2, searchinput3))
            return rowdicts[0]


    @staticmethod
    def getData(admin, student_level, student_classe, student_facutly, 
                    searchinput1, searchinput2, searchinput3):
        
        if student_facutly != None :
            with connection.cursor() as cursor:
                cursor.execute("""SELECT shule_registerstudent.id, shule_registerstudent.name, shule_registerstudent.lastname,
                shule_registerstudent.nickname , shule_level.title as classe , shule_classe.title as classe, shule_feetype.title as lib,
                shule_faculty.title as faculty, SUM(shule_studentpayment.amount) as amount, shule_studentpayment.totfee as totamount,
                min(shule_studentpayment.date) as first, max(shule_studentpayment.date) as second, shule_studentpayment.date 
                FROM  shule_registerstudent LEFT JOIN shule_level ON shule_level.id=shule_registerstudent.level_id
                LEFT JOIN shule_classe ON shule_classe.id = shule_registerstudent.classe_id 
                LEFT JOIN shule_faculty ON shule_faculty.id = shule_registerstudent.faculty_id 
                LEFT JOIN shule_studentpayment ON shule_studentpayment.student_id = shule_registerstudent.id  
                LEFT JOIN shule_feetype ON shule_feetype.id = shule_studentpayment.payment_id
                LEFT JOIN shule_staff ON shule_staff.id=shule_registerstudent.secretary_id 

                WHERE shule_staff.admin_id=%s AND shule_registerstudent.name=%s AND shule_registerstudent.lastname=%s AND 
                shule_registerstudent.nickname=%s AND shule_registerstudent.level_id=%s AND 
                shule_registerstudent.classe_id=%s AND shule_registerstudent.faculty_id=%s""",
                (admin, searchinput1, searchinput2, searchinput3, student_level, student_classe, student_facutly))

                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for name, city in zip(colnames, row):
                        newdict[name] = city
                    rowdicts.append(newdict)
                
                return rowdicts

        elif student_facutly == None:
            with connection.cursor() as cursor:
                cursor.execute("""SELECT shule_registerstudent.id, shule_registerstudent.name, shule_registerstudent.lastname,
                shule_registerstudent.nickname , shule_level.title as classe , shule_classe.title as classe, shule_feetype.title as lib,
                shule_faculty.title as faculty, SUM(shule_studentpayment.amount) as amount, shule_studentpayment.totfee as totamount,
                shule_studentpayment.totfee as list_amount ,
                min(shule_studentpayment.date) as first, max(shule_studentpayment.date) as second,shule_studentpayment.date 
                FROM  shule_registerstudent LEFT JOIN shule_level ON shule_level.id=shule_registerstudent.level_id
                LEFT JOIN shule_classe ON shule_classe.id =shule_registerstudent.classe_id 
                LEFT JOIN shule_faculty ON shule_faculty.id = shule_registerstudent.faculty_id 
                LEFT JOIN shule_studentpayment ON shule_studentpayment.student_id= shule_registerstudent.id 
                LEFT JOIN shule_feetype ON shule_feetype.id = shule_studentpayment.payment_id
                LEFT JOIN shule_staff ON shule_staff.id=shule_registerstudent.secretary_id 

                WHERE shule_staff.admin_id=%s AND shule_registerstudent.name=%s AND shule_registerstudent.lastname=%s AND 
                shule_registerstudent.nickname=%s AND shule_registerstudent.level_id=%s AND 
                shule_registerstudent.classe_id=%s """,
                (admin, searchinput1, searchinput2, searchinput3, student_level, student_classe))

                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for name, city in zip(colnames, row):
                        newdict[name] = city
                    rowdicts.append(newdict)
                
                return rowdicts



class QueryStudentPayment:

    @staticmethod
    def queryBalance(student_id, paymenttype_id, user_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT admin_id from shule_staff WHERE id={user_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                for ids in newdict:
                    rowdicts.append(QueryStudentPayment.requestData(student_id, paymenttype_id, newdict[ids]))
            return rowdicts[0]

    @staticmethod
    def requestData(student_id, paymenttype_id, admin_id):
        with connection.cursor() as cursor:
            amount = []
            cursor.execute("""SELECT shule_studentpayment.totfee as balance, shule_studentpayment.date as date FROM
            shule_studentpayment LEFT JOIN shule_feetype ON shule_feetype.id = shule_studentpayment.payment_id 
            LEFT JOIN shule_registerstudent ON shule_registerstudent.id = shule_studentpayment.student_id 
            LEFT JOIN shule_staff ON shule_staff.id = shule_registerstudent.secretary_id 
            WHERE shule_staff.admin_id = %s AND shule_studentpayment.student_id=%s AND 
            shule_studentpayment.payment_id=%s ORDER BY date DESC LIMIT 1 """,(admin_id, student_id, paymenttype_id))

            for balance in cursor.fetchall():
                for final_amount in balance:
                    amount.append(final_amount)
            print(admin_id, student_id, paymenttype_id)
            return amount
            
           

    @staticmethod
    def recordAmount(designation, student_id, paymenttype_id, new_balance, amount=0):
        with connection.cursor()  as cursor:
            cursor.execute("""INSERT INTO shule_studentpayment(designation, amount, totfee, payment_id, student_id) 
                VALUES(%s, %s, %s, %s, %s)""", (designation, amount, new_balance, paymenttype_id, student_id))
            return QueryStudentPayment.retrieveStudentHistorique(student_id)


    @staticmethod
    def retrieveStudentHistorique(student_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_registerstudent.name, shule_registerstudent.lastname, shule_registerstudent.nickname,
            shule_level.title as level, shule_classe.title as classe, shule_faculty.title as faculty, shule_studentpayment.amount as amount, 
            shule_studentpayment.totfee as balance, shule_feetype.title as feetype, shule_studentpayment.date as date
            FROM shule_registerstudent
            LEFT JOIN shule_studentpayment ON shule_studentpayment.student_id=shule_registerstudent.id
            LEFT JOIN shule_level ON shule_level.id=shule_registerstudent.level_id 
            LEFT JOIN shule_classe ON shule_classe.id=shule_registerstudent.classe_id
            LEFT JOIN shule_faculty ON shule_faculty.id=shule_registerstudent.faculty_id
            LEFT JOIN shule_feetype ON shule_feetype.id=shule_studentpayment.payment_id 
            WHERE shule_registerstudent.id = {student_id} AND shule_studentpayment.id=(SELECT LAST_INSERT_ID())""" )
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                rowdicts.append(newdict)
            
            return rowdicts

    @staticmethod
    def retrieveStudentHistoriqueGlobal(student_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_registerstudent.name, shule_registerstudent.lastname, shule_registerstudent.nickname,
            shule_level.title as level, shule_classe.title as classe, shule_faculty.title as faculty, shule_studentpayment.amount as amount, 
            shule_studentpayment.totfee as balance, shule_feetype.title as feetype, shule_studentpayment.date as date
            FROM shule_registerstudent
            LEFT JOIN shule_studentpayment ON shule_studentpayment.student_id=shule_registerstudent.id
            LEFT JOIN shule_level ON shule_level.id=shule_registerstudent.level_id 
            LEFT JOIN shule_classe ON shule_classe.id=shule_registerstudent.classe_id
            LEFT JOIN shule_faculty ON shule_faculty.id=shule_registerstudent.faculty_id
            LEFT JOIN shule_feetype ON shule_feetype.id=shule_studentpayment.payment_id 
            WHERE shule_registerstudent.id = {student_id} """ )
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            
            return rowdicts

    @staticmethod
    def displayLevelCachier(user_id, level):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT admin_id FROM shule_staff WHERE id={user_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
                for ids in newdict:
                    rowdicts.append(FeePayment.displayPayementDetails(newdict[ids], level))
            return rowdicts[1]
                    
    @staticmethod
    def retrieveStudentHistoPeriode(student_id, date1, date2):
        with connection.cursor()  as cursor:
            cursor.execute("""SELECT shule_studentpayment.amount, shule_studentpayment.totfee, shule_studentpayment.date,
                        shule_feetype.title as type FROM shule_studentpayment 
                        LEFT JOIN  shule_fixepayment ON shule_fixepayment.id = shule_studentpayment.payment_id 
                        LEFT JOIN  shule_feetype ON shule_feetype.id = shule_fixepayment.feetype_id 
                        LEFT JOIN shule_registerstudent ON shule_registerstudent.id = shule_studentpayment.student_id 
                        WHERE shule_studentpayment.date >= %s AND shule_studentpayment.date <= %s AND
                        shule_studentpayment.student_id=%s """,(date1, date2, student_id))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            
            return rowdicts

    # RECOVERY STUDENTS /////////////////////////////////////////////////////////////////////////////////
    
    @staticmethod
    def paymentRecovery(level, classe, faculty, dateone, datetwo, user_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT admin_id FROM shule_staff WHERE id={user_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
                for ids in newdict:
                    rowdicts.append(QueryStudentPayment.getRecovery(newdict[ids], level, classe, faculty, dateone, datetwo))
                    rowdicts.append(QueryStudentPayment.getRecoveryBalance(newdict[ids], level, classe, faculty))
                    rowdicts.append(QueryStudentPayment.getNumberStudent(newdict[ids], level, classe, faculty))
            return rowdicts


    @staticmethod
    def getNumberStudent(admin, level, classe, faculty):
        if faculty != None:
            with connection.cursor()  as cursor:
                cursor.execute("""SELECT COUNT(shule_registerstudent.id) as student FROM shule_registerstudent
                        LEFT JOIN shule_level ON shule_level.id = shule_registerstudent.level_id
                        LEFT JOIN shule_classe ON shule_classe.id = shule_registerstudent.classe_id
                        LEFT JOIN shule_faculty ON shule_faculty.id = shule_registerstudent.faculty_id
                        LEFT JOIN shule_staff ON shule_staff.id  = shule_registerstudent.secretary_id
                        WHERE shule_staff.admin_id = %s AND shule_registerstudent.level_id = %s AND 
                        shule_registerstudent.classe_id=%s AND shule_registerstudent.faculty_id =%s
                        GROUP BY shule_registerstudent.faculty_id ORDER BY shule_registerstudent.level_id DESC"""
                        ,(admin, level, classe, faculty))
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for key, val in zip(colnames, row):
                        newdict[key] = val
                    rowdicts.append(newdict)
                return rowdicts
        
        else:
            with connection.cursor()  as cursor:
                cursor.execute("""SELECT COUNT(shule_registerstudent.id) as student FROM shule_registerstudent
                        LEFT JOIN shule_staff ON shule_staff.id = shule_registerstudent.secretary_id
                        LEFT JOIN shule_level ON shule_level.id = shule_registerstudent.level_id
                        LEFT JOIN shule_classe ON shule_classe.id = shule_registerstudent.classe_id
                        LEFT JOIN shule_faculty ON shule_faculty.id = shule_registerstudent.faculty_id
                        WHERE shule_staff.admin_id = %s AND shule_registerstudent.level_id = %s AND
                        shule_registerstudent.classe_id= %s 
                        GROUP BY shule_registerstudent.classe_id ORDER BY shule_registerstudent.level_id DESC"""
                        ,(admin, level, classe))
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for key, val in zip(colnames, row):
                        newdict[key] = val
                    rowdicts.append(newdict)
                return rowdicts


    @staticmethod
    def getRecoveryBalance( admin, level, classe, faculty):
        if faculty != None:
            with connection.cursor()  as cursor:
                cursor.execute("""SELECT shule_level.title as level, shule_classe.title as classe, shule_faculty.title as faculty, 
                    SUM(shule_fixepayment.tot_amount) as balance FROM shule_fixepayment 
                    LEFT JOIN shule_level ON shule_level.id = shule_fixepayment.level_id 
                    LEFT JOIN shule_classe ON shule_classe .id = shule_fixepayment.classe_id
                    LEFT JOIN shule_faculty ON shule_faculty.id = shule_fixepayment.faculty_id
                    LEFT JOIN shule_admin ON shule_admin.id = shule_fixepayment.admin_id
                    WHERE shule_admin.id =%s AND shule_fixepayment.level_id=%s AND 
                    shule_fixepayment.classe_id=%s AND shule_fixepayment.faculty_id =%s 
                    GROUP BY shule_fixepayment.faculty_id ORDER BY  shule_fixepayment.level_id DESC """,
                    (admin, level, classe, faculty))
                    
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for key, val in zip(colnames, row):
                        newdict[key] = val
                    rowdicts.append(newdict)
                return rowdicts

        else:
            with connection.cursor()  as cursor:
                cursor.execute("""SELECT shule_level.title as level, shule_classe.title as classe,
                    SUM(shule_fixepayment.tot_amount) as balance  FROM shule_fixepayment
                    LEFT JOIN shule_level ON shule_level.id = shule_fixepayment.level_id 
                    LEFT JOIN shule_classe ON shule_classe .id = shule_fixepayment.classe_id
                    LEFT JOIN shule_faculty ON shule_faculty.id = shule_fixepayment.faculty_id
                    LEFT JOIN shule_admin ON shule_admin.id = shule_fixepayment.admin_id
                    WHERE shule_admin.id =%s AND shule_fixepayment.level_id=%s AND 
                    shule_fixepayment.classe_id=%s 
                    GROUP BY shule_fixepayment.classe_id ORDER BY  shule_fixepayment.level_id DESC """,
                    (admin, level, classe))
                    
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for key, val in zip(colnames, row):
                        newdict[key] = val
                    rowdicts.append(newdict)
                return rowdicts


    @staticmethod
    def getRecovery( admin, level, classe, faculty, dateone, datetwo):

        if faculty != None:
            with connection.cursor()  as cursor:
                cursor.execute("""SELECT shule_registerstudent.name, shule_registerstudent.lastname, shule_registerstudent.nickname, 
                    shule_level.title as level, shule_classe.title as classe, shule_faculty.title as faculty, 
                    SUM(shule_studentpayment.amount) as totamount FROM shule_studentpayment 
                    LEFT JOIN shule_registerstudent ON shule_registerstudent.id = shule_studentpayment.student_id
                    LEFT JOIN shule_level ON shule_level.id = shule_registerstudent.level_id 
                    LEFT JOIN shule_classe ON shule_classe .id = shule_registerstudent.classe_id
                    LEFT JOIN shule_faculty ON shule_faculty.id = shule_registerstudent.faculty_id
                    LEFT JOIN shule_staff ON shule_staff.id = shule_registerstudent.secretary_id
                    WHERE shule_studentpayment.date >= %s AND shule_studentpayment.date <= %s AND
                    shule_staff.admin_id =%s AND shule_registerstudent.level_id=%s AND 
                    shule_registerstudent.classe_id=%s AND shule_registerstudent.faculty_id =%s 
                    GROUP BY shule_studentpayment.student_id ORDER BY shule_studentpayment.amount DESC """,
                    (dateone, datetwo, admin, level, classe, faculty))
                    
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for key, val in zip(colnames, row):
                        newdict[key] = val
                    rowdicts.append(newdict)
                return rowdicts

        else:
            with connection.cursor()  as cursor:
                cursor.execute("""SELECT shule_registerstudent.name, shule_registerstudent.lastname, shule_registerstudent.nickname, 
                    shule_level.title as level, shule_classe.title as classe, shule_faculty.title as faculty, 
                    SUM(shule_studentpayment.amount) as totamount FROM shule_studentpayment 
                    LEFT JOIN shule_registerstudent ON shule_registerstudent.id = shule_studentpayment.student_id
                    LEFT JOIN shule_level ON shule_level.id = shule_registerstudent.level_id 
                    LEFT JOIN shule_classe ON shule_classe .id = shule_registerstudent.classe_id
                    LEFT JOIN shule_faculty ON shule_faculty.id = shule_registerstudent.faculty_id
                    LEFT JOIN shule_staff ON shule_staff.id = shule_registerstudent.secretary_id
                    WHERE shule_studentpayment.date >= %s AND shule_studentpayment.date <= %s AND
                    shule_staff.admin_id =%s AND shule_registerstudent.level_id=%s AND shule_registerstudent.classe_id=%s 
                    GROUP BY shule_studentpayment.student_id ORDER BY shule_studentpayment.amount DESC """,
                    (dateone, datetwo, admin, level, classe))
                    
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for key, val in zip(colnames, row):
                        newdict[key] = val
                    rowdicts.append(newdict)
                return rowdicts


def getEmplyeeFunction(user_id):
    with connection.cursor() as cursor:
        cursor.execute(f'''SELECT shule_employfunction.id , shule_employfunction.title as function FROM shule_employfunction 
        LEFT JOIN shule_staff ON shule_staff.admin_id = shule_employfunction.shulde_admin_id WHERE shule_staff.id = {user_id}''')
        colnames = [desc[0] for desc in cursor.description]
        rowdicts = []
        for row in cursor.fetchall():
            newdict = {}
            for key, val in zip(colnames, row):
                newdict[key] = val
            rowdicts.append(newdict)
        return rowdicts
    