import datetime

from django.db import connection



CURRENT_DATE = datetime.datetime.now()
TODAY = CURRENT_DATE.strftime("%Y-%m-%d")


class Outlay:
    def displayEmployee(self, user_id, employee_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_registrationemployee.id, shule_registrationemployee.name, 
            shule_registrationemployee.lastname, shule_registrationemployee.nickname FROM shule_registrationemployee 
            LEFT JOIN shule_employfunction ON shule_employfunction.id = shule_registrationemployee.function_id
            LEFT JOIN shule_staff ON shule_staff.admin_id = shule_employfunction.shulde_admin_id
            WHERE shule_registrationemployee.function_id ={employee_id} AND shule_staff.id = {user_id} """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts

    def employeeDetails(self, user_id, employee_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_fixeemployeesalary.amount, shule_fixeemployeesalary.salary, shule_employfunction.title,
            shule_registrationemployee.name, shule_registrationemployee.lastname, shule_registrationemployee.nickname,
            shule_registrationemployee.id 
            FROM shule_fixeemployeesalary
            LEFT JOIN shule_registrationemployee ON shule_registrationemployee.id = shule_fixeemployeesalary.employee_id 
            LEFT JOIN shule_employfunction ON shule_employfunction.id = shule_registrationemployee.function_id
            WHERE shule_fixeemployeesalary.employee_id={employee_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts

    def employeeHistory(self, user_id, employee_id):
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT shule_employeesalary.designation, shule_employeesalary.amount, shule_employeesalary.tot_payment,
            shule_employeesalary.date FROM shule_employeesalary LEFT JOIN shule_staff ON shule_staff.id = shule_employeesalary.cachier_id 
            WHERE shule_employeesalary.employee_id={employee_id}""")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts

    def manageEmployeeSalary(self, employee_id):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT salary from shule_fixeemployeesalary WHERE employee_id={employee_id}")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts


    def modelRecordAmount(self, designation, tot_payment, cachier_id, employee_id, amount = 0):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO shule_employeesalary(designation, amount, tot_payment, cachier_id, employee_id) 
                    VALUES (%s, %s, %s, %s, %s)""",(designation,amount,tot_payment,cachier_id,employee_id))

    def paymentbalace(self, employee_id):
        with connection.cursor() as cursor:
            getamount = []
            cursor.execute(f"""SELECT tot_payment from shule_employeesalary WHERE employee_id={employee_id} 
                ORDER BY date, time DESC LIMIT 1""")
            for final_amount in cursor.fetchall():
                for amount in final_amount:
                    getamount.append(amount)
            return getamount
            
    def desplayBalance(self, employee_id):
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * from shule_employeesalary WHERE employee_id={employee_id}")
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts

    # display product saved

    def displayAticle(self, secretary_id):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT shule_product.id, shule_product.article FROM shule_product LEFT JOIN 
            shule_staff ON shule_staff.id = shule_product.secretary_id """)  # TE BE CHANGED ADMIN AND SEC ID
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts

    def showArticleSelling(self, article_id):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT shule_product.article, shule_product.unit_amount, shule_productsell.designation, 
            shule_productsell.sold_amount, shule_productsell.remaing FROM shule_productsell 
            LEFT JOIN shule_product ON shule_product.id = shule_productsell.product 
            LEFT JOIN shule_staff ON shule_staff.id = shule_product.secretary_id WHERE shule_product.id = %s""", (article_id,))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts

    def saveSoldeProduct(self, article, designation, entre_amount, remaing):
        with connection.cursor() as cursor:
            cursor.execute("""INSERT INTO shule_productsell(product, designation, sold_amount, remaing) 
                    VALUES (%s, %s, %s, %s)""",(article, designation, entre_amount, remaing))

    def getRemainingProduct(self, article):
        with connection.cursor() as cursor:
            getamount = []
            cursor.execute(f"""SELECT remaing from shule_productsell WHERE product={article} 
                ORDER BY date, time DESC LIMIT 1""")
            for final_amount in cursor.fetchall():
                for amount in final_amount:
                    getamount.append(amount)
            return getamount

    def getProductSoldBalance(self, article):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT SUM(shule_productsell.sold_amount) as totself, shule_product.article as article FROM
            shule_productsell LEFT JOIN shule_product ON shule_product.id = shule_productsell.product 
            WHERE shule_productsell.product = %s """,(article,))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts

    # collect all secondary payment amount 
    # collect all primary amount
    # collect all nursery amount
    # get all level
    def sumUpStudentPayment(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT SUM(shule_studentpayment.amount) as sumamount FROM shule_studentpayment 
                        WHERE shule_studentpayment.date = %s""",(TODAY,))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts


    def sumUpSellPayment(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT SUM(shule_productsell.sold_amount) as sumamount FROM shule_productsell 
                        WHERE shule_productsell.date = %s""",(TODAY,))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts

    def sumUpPayment(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT SUM(shule_rapportcaisse.credit) as sumamount FROM shule_rapportcaisse 
                        WHERE shule_rapportcaisse.date = %s""",(TODAY,))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts

    def showAllLevel(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM shule_level """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts

    # Part by Part
    def getStudentPaymentHisto(self, stdpaiements):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT shule_studentpayment.amount, shule_studentpayment.designation as lbl, 
            shule_studentpayment.date FROM shule_studentpayment 
            LEFT JOIN shule_registerstudent ON shule_registerstudent.id = shule_studentpayment.student_id 
            WHERE shule_registerstudent.level_id = %s """, (stdpaiements, ))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts

    def getStudentPaymentSum(self, stdpaiements):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT SUM(shule_studentpayment.amount)as sum, COUNT(shule_studentpayment.id)as content
            FROM shule_studentpayment 
            LEFT JOIN shule_registerstudent ON shule_registerstudent.id = shule_studentpayment.student_id 
            WHERE shule_registerstudent.level_id = %s """, (stdpaiements, ))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts

    # All content 

    def repportAllHistoMix(self, user_id):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT shule_rapportcaisse.designation as lbl, shule_rapportcaisse.debit as debit, 
            shule_rapportcaisse.credit as credit, shule_rapportcaisse.balance as balance, shule_rapportcaisse.date as dates
            FROM shule_rapportcaisse WHERE shule_rapportcaisse.cachier_id= %s""",(user_id, ))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts

    def repportAllSumMix(self, user_id):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT COUNT(shule_rapportcaisse.id) as content, SUM(shule_rapportcaisse.debit) as debit, 
            SUM(shule_rapportcaisse.credit) as credit FROM shule_rapportcaisse WHERE shule_rapportcaisse.cachier_id= %s""",(user_id, ))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts
        

    # Sell sum up

    def repportSellArticleSum(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT COUNT(shule_productsell.id) as content, SUM(shule_productsell.sold_amount) as debit
            FROM shule_productsell """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts
        

    def repportSellArticleAll(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT shule_productsell.designation as lbl, shule_productsell.sold_amount as amount , 
            shule_productsell.date as date, shule_product.article as product
            FROM shule_productsell LEFT JOIN shule_product ON shule_product.id = shule_productsell.product """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts
        


    # Manage credit payment

    def displayCredit(self, user_id):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT designation, credit, date FROM shule_rapportcaisse WHERE cachier_id=%s""",(user_id, ))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts
            return []

    def displaySumCredit(self, user_id):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT SUM(credit) as credit, COUNT(id) as sum FROM shule_rapportcaisse 
            WHERE cachier_id=%s""",(user_id, ))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            return rowdicts

    def getTodayPayment(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT SUM(shule_rapportcaisse.credit) as sumamount FROM shule_rapportcaisse 
                        WHERE shule_rapportcaisse.date = %s""",(TODAY,))
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for key, val in zip(colnames, row):
                    newdict[key] = val
                rowdicts.append(newdict)
            print(rowdicts)
            return rowdicts
     



