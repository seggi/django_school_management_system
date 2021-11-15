import datetime
from shule.nkmodels.cachiermodels import *
from shule.nkmodels.checkoutmodels import CheckOutDb

CURRENT_DATE = datetime.datetime.now()
NOW = CURRENT_DATE.strftime("%Y-%m-%d %H:%M:%S")


REQUEST_STUDENT_SOLDE = QueryStudentPayment()
RECORD_AMOUNT = CheckOutDb()


class ComputeCredit:
	def __init__(self, balance):
		self.new_balance = balance

	def __sub__(self, amount):
		return ComputeCredit(self.new_balance - int(amount))

class ComputerDebit:
	def __init__(self, balance):
		self.new_balance = balance

	def __radd__(self, amount):
		return ComputerDebit(float(amount) + float(self.new_balance))


# CHECK OUT MANAGE

class ComputeCheckOut:
    @staticmethod
    def computeNewRecord(designation, cachier_id, new_debit=None, new_credit=None):
        if new_debit == None:
            debit_label = 0
            for balance in RECORD_AMOUNT.checkBalance(cachier_id):
                asign_amount = ComputeCredit(balance)
                calculate = asign_amount - new_credit
                RECORD_AMOUNT.recordAmount(designation, debit_label,new_credit, calculate.new_balance, cachier_id)
                
        elif new_debit != None:
            credit_label = 0
            for balance in RECORD_AMOUNT.checkBalance(cachier_id):
                asign_amount = ComputerDebit(balance)
                calculate  = new_debit + asign_amount
                RECORD_AMOUNT.recordAmount(designation, new_debit, credit_label, calculate.new_balance, cachier_id)
                

# STUDENT PAYMENT

class RecordPayment(ComputeCheckOut):
    def __init__(self, student_id, user_id, paymenttype, amount, designation):
        self.student_id = student_id
        self.user_id = user_id
        self.amount = amount 
        self.designation = designation
        self.paymenttype = paymenttype
        self.request_std_amount = REQUEST_STUDENT_SOLDE.queryBalance(self.student_id, self.paymenttype, self.user_id)
       
    def amountComputer(self):
        if len(self.request_std_amount) > 0:
            if self.request_std_amount[1] != NOW:
                asign_amount = ComputeCredit(self.request_std_amount[0])
                calcule = asign_amount - self.amount
                retrieve = REQUEST_STUDENT_SOLDE.recordAmount(self.designation, self.student_id, 
                                    self.paymenttype, calcule.new_balance, self.amount)
                ComputeCheckOut.computeNewRecord(self.designation, self.user_id, self.amount)
                return retrieve
        else:
            return "Ce type de frais ne pas encore ajouter dans cette classe!,\n"+\
                    "utilise le compte administrateur pour ajouter."


# STUDENT RECOVRY

class ComputePayment:
    SINGLE_TOT_AMOUNT = 'totamount'
    def __init__(self, level, classe, faculty, date1, date2, amount_max, user_id, ranges):
        self.level = level
        self.classe = classe
        self.faculty =  faculty
        self.dateone = date1
        self.datetwo = date2 
        self.amount_max = amount_max
        self.user_id = user_id
        self.ranges = ranges
        self.db_query = REQUEST_STUDENT_SOLDE.paymentRecovery(self.level, self.classe, self.faculty, 
                    self.dateone, self.datetwo, self.user_id)
        

    def computeData(self):
        collected=[]
        for x in self.db_query[1]:
            if int(self.ranges) == 1:
                if x[self.SINGLE_TOT_AMOUNT] >= float(self.amount_max):
                    for y in self.db_query[2]:
                        x['balance'] = y['balance'] 
                        x['remaining'] = y['balance'] - x[self.SINGLE_TOT_AMOUNT]
                        collected.append(x)
                
                  
            elif int(self.ranges) == 0:
                if x[self.SINGLE_TOT_AMOUNT] < float(self.amount_max):
                    for y in self.db_query[2]:
                        x['balance'] = y['balance'] 
                        x['remaining'] = y['balance'] - x[self.SINGLE_TOT_AMOUNT]
                        collected.append(x)

        return  [collected, self.db_query[2], self.db_query[3]]
       
        




