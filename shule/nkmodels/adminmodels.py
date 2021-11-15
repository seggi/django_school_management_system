from django.db import connection


class RequestStaff:
    def displayStaffListdb(self, admin, fonction):
        if fonction != None:
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_staff.id, shule_shuleuser.first_name as name, shule_shuleuser.last_name as last_name, 
                shule_shuleuser.username, shule_shuleuser.email as email, shule_shuleuser.phone, shule_staff.gender, 
                shule_staff.address  FROM shule_shuleuser LEFT JOIN shule_staff ON 
                shule_staff.user_id = shule_shuleuser.id LEFT JOIN  shule_admin ON 
                shule_admin.user_id = shule_shuleuser.id WHERE shule_shuleuser.{fonction}={1} AND
                shule_staff.admin_id ={admin}""")
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for col, val in zip(colnames, row):
                        newdict[col] = val
                    rowdicts.append(newdict)
                return rowdicts
        else:
            return []

    
    def showEMployeeDetails(self, school_id, function):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_registrationemployee.id, shule_registrationemployee.name, shule_registrationemployee.lastname, 
            shule_registrationemployee.nickname, shule_registrationemployee.sex, shule_fixeemployeesalary.salary
            FROM shule_registrationemployee
            LEFT JOIN shule_fixeemployeesalary ON shule_fixeemployeesalary.employee_id = shule_registrationemployee.id
            LEFT JOIN shule_employfunction ON shule_employfunction.id = shule_registrationemployee.function_id 
            WHERE shule_registrationemployee.function_id = {function}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for col, val in zip(colnames, row):
                    newdict[col] = val
                rowdicts.append(newdict)
            return rowdicts

    def removeEmployee(self, employee_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""DELETE FROM shule_fixeemployeesalary WHERE employee_id ={employee_id}""")
        with connection.cursor() as cursor:
            cursor.execute(f"""DELETE FROM shule_employeesalary WHERE employee_id ={employee_id}""")
        with connection.cursor() as cursor:
            cursor.execute(f"""DELETE FROM shule_registrationemployee WHERE id ={employee_id}""")

        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_registrationemployee.id, shule_registrationemployee.name, shule_registrationemployee.lastname, 
            shule_registrationemployee.nickname, shule_registrationemployee.sex, shule_fixeemployeesalary.salary
            FROM shule_registrationemployee
            LEFT JOIN shule_fixeemployeesalary ON shule_fixeemployeesalary.employee_id = shule_registrationemployee.id """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for col, val in zip(colnames, row):
                    newdict[col] = val
                rowdicts.append(newdict)
            return rowdicts

            

    def getItemToEdit(self, employee_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_registrationemployee.id, shule_registrationemployee.name, shule_registrationemployee.lastname, 
            shule_registrationemployee.nickname, shule_registrationemployee.sex, shule_fixeemployeesalary.salary
            FROM shule_registrationemployee
            LEFT JOIN shule_fixeemployeesalary ON shule_fixeemployeesalary.employee_id = shule_registrationemployee.id
            WHERE shule_registrationemployee.id={employee_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for col, val in zip(colnames, row):
                    newdict[col] = val
                rowdicts.append(newdict)
            return rowdicts

    def updateEmployeeItem(self, name, lastname, nickname, salary, getitemid):
        with connection.cursor()  as cursor:
            cursor.execute("""UPDATE shule_fixeemployeesalary SET salary=%s WHERE employee_id=%s """,(salary, getitemid))
        
            if True:
                cursor.execute(f"""SELECT shule_registrationemployee.id, shule_registrationemployee.name, shule_registrationemployee.lastname, 
                shule_registrationemployee.nickname, shule_registrationemployee.sex, shule_fixeemployeesalary.salary
                FROM shule_registrationemployee
                LEFT JOIN shule_fixeemployeesalary ON shule_fixeemployeesalary.employee_id = shule_registrationemployee.id
                WHERE shule_registrationemployee.id = {getitemid}""")
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for col, val in zip(colnames, row):
                        newdict[col] = val
                    rowdicts.append(newdict)
                return rowdicts






class AddLeveldb:
    @staticmethod
    def saveLeveldb(school_id,level):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO shule_level(title, shulde_admin_id) VALUES(%s, %s)""", 
            (level, school_id))
        
        def printLeveldb(classes):
            with connection.cursor() as cursor:
                cursor.execute("""SELECT id FROM shule_level WHERE id=(SELECT LAST_INSERT_ID())""")
                for row in cursor.fetchall():
                    for classe in classes:
                        cursor.execute("""INSERT INTO shule_classe(title, level_id) VALUES(%s, %s)""", (classe, row[0]))
                    print(classe, row)
        return printLeveldb

    
    @staticmethod
    def selectLeveldb(school_id):
        if school_id != '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_level.id, shule_level.title as level 
                        FROM shule_level WHERE shule_level.shulde_admin_id={school_id}""")
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
    def selectClassedb(school_id):
        if school_id != '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_classe.id, shule_classe.title as classe, 
                        shule_classe.level_id as levels FROM shule_level LEFT JOIN shule_classe 
                        ON shule_level.id = shule_classe.level_id WHERE shule_level.shulde_admin_id={school_id}""")
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
    def selectFacultydb(school_id):
        if school_id != '':
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_faculty.id, shule_faculty.title as faculty, 
                        shule_faculty.classe_id as classes FROM shule_faculty LEFT JOIN shule_classe
                        ON shule_classe.id = shule_faculty.classe_id LEFT JOIN shule_level ON 
                        shule_level.id = shule_classe.level_id WHERE shule_level.shulde_admin_id={school_id}""")
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
    def saveLevelClassedb(faculty, classe_id):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO shule_faculty(title, classe_id) VALUES(%s, %s)""", (faculty, classe_id))


    @staticmethod
    def displayLevelClasseFacultydb(school_id, level):
        if school_id != None and level != None:
            with connection.cursor() as cursor:
                cursor.execute(f"""SELECT shule_level.title as level, shule_classe.title as classe, shule_faculty.title as faculty
                        FROM shule_level LEFT JOIN shule_classe ON shule_classe.level_id = shule_level.id  LEFT JOIN shule_faculty 
                        ON shule_faculty.classe_id = shule_classe.id WHERE shule_level.shulde_admin_id = {school_id} 
                        AND shule_level.id = {level} """)
                colnames = [desc[0] for desc in cursor.description]
                rowdicts = []
                for row in cursor.fetchall():
                    newdict = {}
                    for col, val in zip(colnames, row):
                        newdict[col] = val
                    rowdicts.append(newdict)
                return rowdicts
        return []


class FeePayment:
    def displayFeetype(self, school_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT id , title FROM shule_feetype WHERE admin_id={school_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for col, val in zip(colnames, row):
                    newdict[col] = val
                rowdicts.append(newdict)
            return rowdicts

    def displayPriode(self, school_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT id, name FROM shule_periode WHERE admin_id = {school_id} """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for col, val in zip(colnames, row):
                    newdict[col] = val
                rowdicts.append(newdict)
            return rowdicts

    @staticmethod
    def displayPayementDetails(school_id, fee_search):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_fixepayment.id, shule_fixepayment.amount as tranche,shule_fixepayment.tot_amount as
            totamount, shule_level.title as level, shule_classe.title as classe, shule_faculty.title as faculty, shule_periode.name as periode, 
            shule_feetype.title as type FROM shule_fixepayment LEFT JOIN shule_level ON shule_level.id = shule_fixepayment.level_id
            LEFT JOIN shule_classe ON shule_classe.id = shule_fixepayment.classe_id 
            LEFT JOIN shule_faculty ON shule_faculty.id = shule_fixepayment.faculty_id 
            LEFT JOIN shule_feetype ON shule_feetype.id = shule_fixepayment.feetype_id 
            LEFT JOIN shule_periode ON shule_periode.id = shule_fixepayment.periode_id 
            LEFT JOIN shule_admin ON shule_admin.id = shule_fixepayment.admin_id 
            WHERE shule_admin.id = {school_id} AND shule_level.id = {fee_search} """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for col, val in zip(colnames, row):
                    newdict[col] = val
                rowdicts.append(newdict)
            return rowdicts

    # display employee category

    @staticmethod
    def displayEmployeeFunctiondb(school_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT id , title FROM shule_employfunction WHERE shulde_admin_id={school_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for col, val in zip(colnames, row):
                    newdict[col] = val
                rowdicts.append(newdict)
            return rowdicts


   
            

    

    