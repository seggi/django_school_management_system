from shule.nkcore.compute import ComputeCredit, ComputeCheckOut


AUTO_FILL_CLASSES_EN = ['']
AUTO_FILL_CLASSES_FR = ['première','deuxième', 'troisième', 'quatrième', 
            'cinquième', 'sixième', 'septième',
            'huitième', 'neuvième' , 'dixième', 'onzième', 'douzième']


class GenerateClasses:
    def __init__(self, lang=None):
        pass

    def generatorClasseWord(self, number):
        classe_in_word = []
        numbers = int(number)
        for word in AUTO_FILL_CLASSES_FR[:numbers]:
            classe_in_word.append(word)
        return classe_in_word


class ManageEmployeeSalay:
    defaultdesignation = "Affectation du salaire"
    defaultamount = 0
    def __init__(self, db, jsonify,user_id, employee_id, amount, designation):
        self.employee = employee_id
        self.db = db
        self.jsonify = jsonify
        self.employee_id = employee_id
        self.amount = amount
        self. designation = designation
        self.user_id = user_id
        
    def salaryChecking(self):
        checkemployeesalary = self.db.manageEmployeeSalary(self.employee_id)
        if len(checkemployeesalary) > 0:
            for employee in checkemployeesalary[0]:
                if checkemployeesalary[0][employee] > 0:
                    self.checkBalance(self.user_id, self.employee_id, self.amount, 
                            self.designation, checkemployeesalary[0][employee])
                    return self.jsonify(self.db.desplayBalance(self.employee_id), safe=False)

                else:
                    return self.jsonify({'error': "Le salaire de cet'employee ne pas encore fixer!"})
        else:
            return self.jsonify({'error': "La liste d'employee est vide!"})

    def checkBalance(self, user_id, employee_id, amount, designation, fixedsalary):
        checkbalance = self.db.paymentbalace(employee_id)
        if len(checkbalance) > 0:
            # for employeebalance in checkbalance:
            if checkbalance[0] > 0:
                asign_amount = ComputeCredit(checkbalance[0])
                tot_payment = asign_amount - self.amount
                self.db.modelRecordAmount(designation, tot_payment.new_balance, user_id, employee_id, amount)
                ComputeCheckOut.computeNewRecord(designation=designation, cachier_id=user_id, new_credit=amount)
            
            elif checkbalance[0] == 0:
                self.db.modelRecordAmount(self.defaultdesignation, fixedsalary, user_id, employee_id, self.defaultamount,) 
        else:
            self.db.modelRecordAmount(self.defaultdesignation, fixedsalary, user_id, employee_id, self.defaultamount,)
            


class SellProduct(ComputeCheckOut):
    remove = 1
    def __init__(self, article , designation, entre_amount, jsonify, db, user_id):
        self.article = article
        self.designation = designation
        self.entre_amount = entre_amount
        self.jsonify = jsonify
        self.db = db
        self.user_id = user_id

    def manageSelling(self):
        remaing = self.db.getRemainingProduct(self.article)
        if len(remaing) > 0:
            for prix in  self.db.showArticleSelling(self.article):  
                if int(self.entre_amount) <= prix['unit_amount']:
                    sub = remaing[0] - self.remove
                    self.db.saveSoldeProduct(self.article, self.designation, self.entre_amount, sub)
                    ComputeCheckOut.computeNewRecord(self.designation, self.user_id, self.entre_amount)
                    return self.jsonify(self.db.showArticleSelling(self.article), safe=False)

                elif float(self.entre_amount) > prix['unit_amount']:
                    return self.jsonify({'error': "Le montant entre est superieur au prix unitaire!"})
        else:
            return self.jsonify({'error': "Le stock pour ce produit est vide!"})


class ManagePayment(ComputeCheckOut):
    def __init__(self, db, jsonify, user_id, amount, designation):
        self.db = db
        self.jsonify = jsonify
        self.user_id = user_id
        self.amount = amount
        self.designation = designation

    def computePayment(self):
        ComputeCheckOut.computeNewRecord(designation=self.designation, cachier_id=self.user_id, new_credit=self.amount)
       
            
