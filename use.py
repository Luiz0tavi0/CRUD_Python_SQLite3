from dml import db_insert,db_delete, db_select, db_update
from pprint import pprint

#db_insert('regis','98978162','regis_asd@yahoo.com.br')
#db_insert('fabricio','98978162','fabricio)@gmail.com')
#db_insert('Lucas','98978162','lucas_2_@gmail.com')
#db_insert('diego','98978162','din_@gmail.com')
#db_insert('Ricar','98978162','rick23@outlook.com.br')

pprint(db_select('98978162','phone'))