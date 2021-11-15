from django.db import connection


class CheckOutDb:
    def recordAmount(self, designation, update_debit, update_credit, update_balance, chachier_id):
        with connection.cursor()  as cursor:
           cursor.execute("""INSERT INTO shule_rapportcaisse(designation, debit, credit, balance, cachier_id)
            VALUES(%s, %s, %s, %s, %s)""",(designation, update_debit, update_credit, update_balance, chachier_id))

    def checkBalance(self, cachier_id):
        with connection.cursor() as cursor:
            getamount = []
            cursor.execute(f"""SELECT balance FROM shule_rapportcaisse WHERE cachier_id={cachier_id} 
            ORDER BY date DESC LIMIT 1 """)
            for final_amount in cursor.fetchall():
                for amount in final_amount:
                    getamount.append(amount)
            return getamount
