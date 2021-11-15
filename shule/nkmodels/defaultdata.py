from django.db import connection


# Request default data from db

class DefaultLocation:
    def countries(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT id, name as country FROM shule_country """ )
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, country in zip(colnames, row):
                    newdict[name] = country
                rowdicts.append(newdict)
            return rowdicts

    
    def states(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT id, name as state, country_id as countries FROM shule_state """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, state in zip(colnames, row):
                    newdict[name] = state
                rowdicts.append(newdict)
            return rowdicts

    def cities(self):
        with connection.cursor() as cursor:
            cursor.execute("""SELECT id, name as city, city_id as states FROM shule_city """)
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                rowdicts.append(newdict)
            return rowdicts

        

class AccountStaff:
    @staticmethod
    def secobject(user_id):
        with connection.cursor() as cursor:
            cursor.execute(f'''SELECT shule_staff.id FROM shule_staff LEFT JOIN shule_admin ON
            shule_admin.id = shule_staff.admin_id WHERE shule_staff.user_id = {user_id}''')
            colnames = [desc[0] for desc in cursor.description]
            rowdicts = []
            for row in cursor.fetchall():
                newdict = {}
                for name, city in zip(colnames, row):
                    newdict[name] = city
                for key in newdict:
                    rowdicts.append(newdict[key])
            if len(rowdicts) > 0:
                return rowdicts[0]
            else:
                return []


