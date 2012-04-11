import sqlite3

from resources.sqlite.pokemon_sqlite_helper import CheckForType, GetID
from resources.sqlite.db_adder import DBAdder

class DBAddDamage(DBAdder):
    """  """
    delegateType = "Damage"
    variantTable = "DamageDelegateVariants"
    
    def __init__(self, connection, cursor):
        DBAdder.__init__(self, connection, cursor)
        self.getIDForType = {'CORE':self.buildCore}
        
    def buildCore(self, params):
        """  """
        type = "CORE"
        table = "CoreDamageDelegate"
        power = int(params[0])
        physical = int(params[1])
        
        toAdd = (power, physical,)
        where = "power = ? and physical = ?"
        params = "power, physical"
        
        return self.buildDelegate(type, table, where, toAdd, params)