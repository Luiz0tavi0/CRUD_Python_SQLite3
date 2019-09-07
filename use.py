from dml import db_insert,db_delete, db_select, db_update,db_delete_all
from pprint import pprint

def ins():
    db_insert('regis','9897162','regis_asd@yhoo.com.br')
    db_insert('fabricio','98978162','fabrici)@gmail.com')
    db_insert('Lucas','9975161','lcas_2_@gmail.com')
    db_insert('diego','945955','din_@mail.com')
    db_insert('Ricar','9871162','rick23@oulook.com.br')
    db_insert('Caoi','9157162','caio@outlok.com.br')


#ins()
db_delete_all(reset_table=True)

#pprint(db_select('phone','99758161'))
pprint(db_select('id',1))