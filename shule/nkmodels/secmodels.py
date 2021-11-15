from django.db import connection


class GetLevel:
    @staticmethod
    def selectLeveldb(user_id):
        if user_id != '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_level.id, shule_level.title as level 
                        FROM shule_level LEFT JOIN shule_staff ON shule_staff.admin_id = shule_level.shulde_admin_id
                        WHERE shule_staff.id={user_id}""")
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for col, val in zip(colnames, row):
                        newdict[col] = val
                    rowdicts.append(newdict)
                return rowdicts
        return []

    @staticmethod
    def selectClassedb(user_id):
        if user_id != '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_classe.id, shule_classe.title as classe, 
                        shule_classe.level_id as levels FROM shule_level LEFT JOIN shule_classe 
                        ON shule_level.id = shule_classe.level_id LEFT JOIN shule_staff ON 
                        shule_staff.admin_id = shule_level.shulde_admin_id WHERE shule_staff.id={user_id}""")
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for col, val in zip(colnames, row):
                        newdict[col] = val
                    rowdicts.append(newdict)
                return rowdicts
        return []

    @staticmethod
    def selectFacultydb(user_id):
        if user_id != '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_faculty.id, shule_faculty.title as faculty, 
                        shule_faculty.classe_id as classes FROM shule_faculty LEFT JOIN shule_classe
                        ON shule_classe.id = shule_faculty.classe_id LEFT JOIN shule_level ON 
                        shule_level.id = shule_classe.level_id LEFT JOIN shule_staff ON 
                        shule_staff.admin_id = shule_level.shulde_admin_id WHERE shule_staff.id={user_id}""")
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for col, val in zip(colnames, row):
                        newdict[col] = val
                    rowdicts.append(newdict)
                return rowdicts
        return []

def extendProduct(secretary_id,remaing):
    designation = 'RAS'
    sold_amount = 0
    with connection.cursor() as cursor:
        cursor.execute(f"""SELECT id FROM shule_product WHERE id=(SELECT LAST_INSERT_ID()) AND secretary_id={secretary_id}""")
        colnames = [desc[0] for desc in cursor.description]
        rowdicts = []
        for row in cursor.fetchall():
            newdict = {}
            for name, city in zip(colnames, row):
                newdict[name] = city
            for key in newdict:
                rowdicts.append(newdict[key])
        if len(rowdicts) > 0:
            ids = rowdicts[0]
            cursor.execute("""INSERT INTO shule_productsell(product,designation, sold_amount, remaing) 
                    VALUES(%s, %s, %s, %s)""", (ids, designation, sold_amount, remaing))
        else:
            return []
    
class RequestProductDetails:
    @staticmethod
    def getProduct(secretary_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT id, article FROM shule_product WHERE secretary_id={secretary_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                rowdicts.append(newdict)
            return rowdicts

    @staticmethod
    def displayProductDetails(secretary_id, article ):
        with connection.cursor() as cursor:
            cursor.execute(f""" SELECT shule_product.id, shule_product.article , shule_product.quantity, shule_product.unit_amount, 
                shule_product.tot_amount, shule_productsell.remaing, shule_product.date FROM shule_product LEFT JOIN shule_staff ON 
                shule_staff.id = shule_product.secretary_id LEFT JOIN shule_productsell ON shule_productsell.product = shule_product.id 
                WHERE shule_product.secretary_id = {secretary_id}  AND shule_product.id = {article}""")

            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                rowdicts.append(newdict)
            return rowdicts


class StudentRegisterdb:
    @staticmethod
    def extendstudentregistration(secretary_id, parent_name, lastname, sex, address, phone, level, classe, faculty ):
        nickname = 'RAS'
        occupation = 'RAS'
        quater = 'RAS'
        avenue = 'RAS'
        age = 'RAS'
        designation = 'Montant a payer'
        amount = 0
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT id FROM shule_registerstudent WHERE id=(LAST_INSERT_ID()) 
                AND secretary_id={secretary_id} """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                for key in newdict:
                    rowdicts.append(newdict[key])
            if len(rowdicts) > 0:
                ids = rowdicts[0]
                cursor.execute("""INSERT INTO shule_parents(name, lastname, nickname, sex, age,
                        occupation, city, quater, avenue, phone, student_id) 
                        VALUES(%s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s)""", 
                        (parent_name, lastname, nickname, sex, age, occupation, address, quater, avenue, phone, ids))

                if faculty != None:
                    
                    cursor.execute(f"""SELECT shule_fixepayment.tot_amount , shule_fixepayment.feetype_id FROM
                        shule_fixepayment LEFT JOIN shule_staff ON shule_staff.admin_id = shule_fixepayment.admin_id 
                        WHERE shule_staff.id={secretary_id} AND shule_fixepayment.level_id={level} AND 
                        shule_fixepayment.classe_id={classe} AND shule_fixepayment.faculty_id={faculty}""")
                    colnames = [desc[0] for desc in cursor.description]
                    rowdicts = []
                    for row in cursor.fetchall():
                        newdict = {}
                        for key, value in zip(colnames, row):
                            newdict[key] = value
                        rowdicts.append(newdict)
                    for x in rowdicts:
                        cursor.execute("""INSERT INTO shule_studentpayment(designation, amount, totfee, payment_id, student_id) 
                        VALUES(%s, %s, %s, %s, %s)""",(designation, amount, x['tot_amount'], x['feetype_id'], ids ))
                       

                elif faculty == None:
                    cursor.execute(f"""SELECT shule_fixepayment.tot_amount , shule_fixepayment.feetype_id FROM
                        shule_fixepayment LEFT JOIN shule_staff ON shule_staff.admin_id = shule_fixepayment.admin_id 
                        WHERE shule_staff.id={secretary_id} AND shule_fixepayment.level_id={level} AND 
                        shule_fixepayment.classe_id={classe} """)
                    colnames = [desc[0] for desc in cursor.description]
                    rowdicts = []
                    for row in cursor.fetchall():
                        newdict = {}
                        for name, city in zip(colnames, row):
                            newdict[name] = city
                        rowdicts.append(newdict)
                    for x in rowdicts:
                        print(x['tot_amount'], x['feetype_id'])
                        cursor.execute("""INSERT INTO shule_studentpayment(designation, amount, totfee, payment_id, student_id) 
                        VALUES(%s, %s, %s, %s, %s)""",(designation, amount, x['tot_amount'], x['feetype_id'], ids ))

                # else:
                #      cursor.execute("""INSERT INTO shule_studentpayment(designation, amount, totfee, payment_id, student_id) 
                #         VALUES(%s, %s, %s, %s, %s)""",(designation, amount,  0,  0, ids ))
            else:
                return []

    
    @staticmethod
    def studentPayment(secretary_id, level, classe, faculty ):
        designation = 'Montant a payer'
        amount = 0
        print(secretary_id)
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT id FROM shule_registerstudent WHERE id=(LAST_INSERT_ID()) 
                AND secretary_id={secretary_id} """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                for key in newdict:
                    rowdicts.append(newdict[key])
            if len(rowdicts) > 0:
                ids = rowdicts[0]
                if faculty != None:
                    cursor.execute(f"""SELECT shule_fixepayment.tot_amount , shule_fixepayment.feetype_id FROM
                        shule_fixepayment LEFT JOIN shule_staff ON shule_staff.admin_id = shule_fixepayment.admin_id 
                        WHERE shule_staff.id={secretary_id} AND shule_fixepayment.level_id={level} AND 
                        shule_fixepayment.classe_id={classe} AND shule_fixepayment.faculty_id={faculty}""")
                    colnames = [desc[0] for desc in cursor.description]
                    rowdicts = []
                    for row in cursor.fetchall():
                        newdict = {}
                        for name, city in zip(colnames, row):
                            newdict[name] = city
                        
                        cursor.execute("""INSERT INTO shule_studentpayment(designation, amount, totfee, payment_id, student_id) 
                        VALUES(%s, %s, %s, %s, %s)""",(designation, amount,  newdict['tot_amount'],  newdict['feetype_id'], ids ))
                else:
                    cursor.execute(f"""SELECT shule_fixepayment.tot_amount , shule_fixepayment.feetype_id FROM
                        shule_fixepayment LEFT JOIN shule_staff ON shule_staff.admin_id = shule_fixepayment.admin_id 
                        WHERE shule_staff.id={secretary_id} AND shule_fixepayment.level_id={level} AND 
                        shule_fixepayment.classe_id={classe} """)
                    colnames = [desc[0] for desc in cursor.description]
                    rowdicts = []
                    for row in cursor.fetchall():
                        newdict = {}
                        for name, city in zip(colnames, row):
                            newdict[name] = city
                        
                        cursor.execute("""INSERT INTO shule_studentpayment(designation, amount, totfee, payment_id, student_id) 
                        VALUES(%s, %s, %s, %s, %s)""",(designation, amount,  newdict['tot_amount'],  newdict['feetype_id'], ids ))
            else:
                return [""]
            

    

    @staticmethod
    def displayRegisteredStudent(secretary_id, level):
        if secretary_id != None and level != None:
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_registerstudent.id, shule_registerstudent.name, shule_registerstudent.lastname, shule_registerstudent.nickname, 
                    shule_registerstudent.sex, shule_registerstudent.age, shule_classe.title as classe, shule_faculty.title as faculty, 
                    shule_level.title as level, shule_parents.name as parent_name, shule_parents.lastname as parent_last, 
                    shule_parents.city as address, shule_parents.phone as phone FROM shule_registerstudent LEFT JOIN 
                    shule_classe ON shule_classe.id = shule_registerstudent.classe_id LEFT JOIN shule_faculty ON
                    shule_faculty.id = shule_registerstudent.faculty_id LEFT JOIN shule_level ON 
                    shule_level.id = shule_registerstudent.level_id LEFT JOIN shule_parents ON 
                    shule_parents.student_id = shule_registerstudent.id WHERE shule_registerstudent.secretary_id = {secretary_id} AND
                    shule_level.id = {level}""")
                
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for name, city in zip(colnames, row):
                        newdict[name] = city
                    rowdicts.append(newdict)
                return rowdicts
        else:
            return []
        

class RegisterEmployee:
    @staticmethod
    def employeeFunction(user_id):
        if user_id !=  '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_employfunction.id, shule_employfunction.title as function FROM shule_employfunction LEFT JOIN 
                shule_admin ON shule_admin.id = shule_employfunction.shulde_admin_id LEFT JOIN shule_staff ON
                shule_staff.admin_id WHERE shule_staff.id = {user_id}""")
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for name, city in zip(colnames, row):
                        newdict[name] = city
                    rowdicts.append(newdict)
                return rowdicts

        else:
            return []

    @staticmethod
    def displayEmployeeFunction(user_id):
        if user_id !=  '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_employfunction.id, shule_employfunction.title as function FROM shule_employfunction LEFT JOIN 
                shule_admin ON shule_admin.id = shule_employfunction.shulde_admin_id LEFT JOIN shule_staff ON
                shule_staff.admin_id WHERE shule_staff.id = {user_id}""")
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for name, city in zip(colnames, row):
                        newdict[name] = city
                    rowdicts.append(newdict)
                return rowdicts

        else:
            return []

    @staticmethod
    def displayRegisteredEmployee(user_id, search_emplayee):
        if user_id != '' and search_emplayee != '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_registrationemployee.id, shule_registrationemployee.name, shule_registrationemployee.lastname, 
                shule_registrationemployee.nickname, shule_registrationemployee.sex, shule_registrationemployee.age, 
                shule_registrationemployee.email, shule_registrationemployee.phone, shule_employfunction.title as function 
                FROM shule_registrationemployee LEFT JOIN shule_employfunction ON 
                shule_employfunction.id = shule_registrationemployee.function_id LEFT JOIN shule_staff ON
                shule_staff.admin_id = shule_employfunction.shulde_admin_id WHERE shule_staff.id = {user_id} AND
                shule_employfunction.id = {search_emplayee}""")
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for name, city in zip(colnames, row):
                        newdict[name] = city
                    rowdicts.append(newdict)
                return rowdicts
        else:
            return []
            

        



