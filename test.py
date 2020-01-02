import pyximport; pyximport.install()
from query import *
from connection import *
import time


Connection = TConnection(user = "postgres", 
                                  password = "",
                                  host = "",
                                  port = "5432",
                                  database = "postgres")                                  
Q1 = TQuery()
time_ini = time.time()
Q1.connection = Connection

#Q1.sql.text = 'select codigo, valor_total from fin_contas where codigo > 10 limit 100'
#Q1.sql.SaveTofile('C:\\testes\\sql1.sql')

#Q1.sql.text = 'select * from cad_pessoas where codigo < %(codigo)s'
#Q1.ParamByName('codigo').AsInteger = 30
#Q1.Open()

Q1.sql.text = 'select * from cad_pessoas where data_nascimento < %(data_nascimento)s';
Q1.ParamByName('data_nascimento').AsDate = datetime.date(2000,01,01)
Q1.Open()

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


print(Q1.RecordCount())
i = 0
while not Q1.EOF:    
    i += 1
    #print('Nome da pessoa: ', Q1.FieldByName('nome').AsString, 'Data Nascimento: ', Q1.FieldByName('data_nascimento').AsDateTime)
    Q1.Next()

time_fim = time.time()

print(i, time_fim - time_ini)
#Q1.sql.LoadFromFile('C:\\testes\\sql1.sql')
#Q1.sql.Add(' and 1 = 2')
#print(Q1.sql.text)

