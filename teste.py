from query import *
from connection import *

Connection = TConnection(user = "", 
                                  password = "",
                                  host = "",
                                  port = "",
                                  database = "")                                  
Q1 = TQuery()
Q1.connection = Connection
Q1.sql.text = 'select * from cad_pessoas where codigo < %(codigo)s'
Q1.ParamByName('codigo').AsInteger = 30
Q1.Open()

#Q1.sql.text = 'update cad_pessoas set nome = %(nome)s where codigo = %(codigo)s'
#Q1.ParamByName('nome').AsString = 'Teste'
#Q1.ParamByName('codigo').AsInteger = 1
#k = Q1.ExecSQL()

#print(k)


Q1.Last()
while not Q1.EOF:    
    print('Nome da pessoa: ', Q1.FieldByName('nome').AsString)
    print('Nascimento: ', Q1.FieldByName('data_nascimento').AsDate)
    Q1.Next()

