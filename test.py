from query import *
from connection import *

Connection = TConnection(user = "", 
                                  password = "",
                                  host = "",
                                  port = "",
                                  database = "")                                  
Q1 = TQuery()
Q1.connection = Connection

#Q1.sql.text = 'select codigo, valor_total from fin_contas where codigo > 10 limit 100'
#Q1.sql.SaveTofile('C:\\testes\\sql1.sql')

#Q1.sql.text = 'select * from cad_pessoas where codigo < %(codigo)s'
#Q1.ParamByName('codigo').AsInteger = 30
#Q1.Open()

#Q1.sql.text = 'select * from cad_pessoas where data_nascimento > %(data_nascimento)s';
#Q1.ParamByName('data_nascimento').AsDate = datetime.date(2000,01,01)
#Q1.Open()

#Q1.sql.text = 'select codigo, valor_total from fin_contas where codigo > 10 limit 100'
#Q1.Open()

#while not Q1.EOF:
#    print('Codigo', Q1.FieldByName('codigo').AsInteger, ' >> Valor: ', Q1.FieldByName('valor_total').AsCurrency)
#    Q1.Next()


#Q1.sql.text = 'update cad_pessoas set nome = %(nome)s where codigo = %(codigo)s'
#Q1.ParamByName('nome').AsString = 'Teste'
#Q1.ParamByName('codigo').AsInteger = 1
#k = Q1.ExecSQL()

#print(k)


#Q1.Last()
#while not Q1.EOF:    
#print('Nome da pessoa: ', Q1.FieldByName('nome').AsString, 'Data Nascimento: ', Q1.FieldByName('data_nascimento').AsDateTime)
#    Q1.Next()

#Q1.sql.LoadFromFile('C:\\testes\\sql1.sql')
#Q1.sql.Add(' and 1 = 2')
#print(Q1.sql.text)

