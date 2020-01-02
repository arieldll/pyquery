from connection import *
import psycopg2.extras
from datetime import datetime

class TQuery:
    def __init__(self):
        self.connection = None
        self.sql = None
        self.EOF = True 
        self.parameters = {}
        self.fields = {}
        self.sql = TSQL()
        self.records = None
        self.index = 0
        self.datetimeformat = '%Y-%m-%dT%h:%m:%s'
        self.dateformat = '%Y-%m-%d'
        self.timeformat = '%h:%m:%s'


    def ParamByName(self, paramname):
        if(not paramname in self.parameters.keys()):
            self.parameters[paramname] = TParameter(paramname)
        return self.parameters[paramname]
    
    def FieldByName(self, fieldname):
        if(not fieldname in self.fields.keys()):
            self.fields[fieldname] = TField(fieldname)
        return self.fields[fieldname]

    def First(self):
        self.index = 0
        self.isEOF()
        self.ChangeDataSetPosition()        
    
    def Last(self):
        self.index = len(self.records)
        self.isEOF()
        self.ChangeDataSetPosition()
        
    
    def Clear(self):
        self.index = 0
        self.records = None
        self.EOF = True

    def Next(self):
        if self.index < len(self.records):
            self.index += 1
        self.isEOF()
        self.ChangeDataSetPosition()        
    
    def Prior(self):        
        self.index -= 1
        self.isEOF()
        self.ChangeDataSetPosition()        

    def ChangeDataSetPosition(self):
        if not self.EOF: 
            if not self.records is None:    
                record = self.records[self.index]        
                for name in record.keys():
                    self.FieldByName(name).Value = record[name]

    def RecordCount(self):
        count = 0
        if not self.records is None:
            count = len(self.records)
        return count

    def isEOF(self):
        self.EOF = False
        if self.index >= self.RecordCount():
            self.EOF = True                                

    def DictParams(self):
        dict_params = {}
        for param in self.parameters.keys():
            dict_params[param] = self.parameters[param].__dict__['value']
        return dict_params

    def Con(self):
        return self.connection.conn()
    
    def Cursor(self):
        return self.connection.conn().cursor(cursor_factory=psycopg2.extras.DictCursor)

    def Commit(self):
        self.Con().commit()

    def Open(self, sql = ''):
        sql_processing = self.sql.text
        if len(sql) > 0:        
            sql_processing = sql
        cursor = self.Cursor()
        dict_params = self.DictParams()
        cursor.execute(sql_processing, dict_params)
        records = cursor.fetchall()
        self.records = records
        self.First()

    def ExecSQL(self, autocommit=True, sql = ''):
        sql_processing = self.sql.text        
        if len(sql) > 0:        
            sql_processing = sql
        dict_params = self.DictParams()
        cursor = self.Cursor()
        cursor.execute(sql_processing, dict_params)
        rowcount = cursor.rowcount
        if autocommit:
            self.Commit()
        return rowcount

        

class TParameter:
    def __init__(self, name):
        self.name = name

    def __setattr__(self, name, value):                
        if name == 'AsString':
            self.__dict__['value'] = str(value)
        elif name == 'AsInteger':
            self.__dict__['value'] = int(value)
        elif name == 'AsFloat':
            self.__dict__['value'] = float(value)
        elif name == 'AsDate':
            self.__dict__['value'] = value
        elif name == 'AsTime':
            self.__dict__['value'] = value
        elif name == 'AsDateTime':
            self.__dict__['value'] = value
        elif name == 'AsCurrency':
            self.__dict__['value'] = '{:.4f}'.format(value)
        

    def __getattr__(self, name):
        if name == 'AsString':
            return str(self.__dict__['value'])
        elif name == 'AsInteger':
            return int(self.__dict__['value'])
        elif name == 'AsFloat':
            return float(self.__dict__['value'])
        elif name == 'AsDate':
            return self.__dict__['value']
        elif name == 'AsTime':
            return self.__dict__['value']
        elif name == 'AsDateTime':
            return self.__dict__['value']
        elif name == 'AsCurrency':
            return ('{:.4f}'.format(self.__dict__['value']))
        

class TField:
    def __init__(self, name):
        self.name = name

    def __setattr__(self, name, value):                
        if name == 'Value':
            self.__dict__['value'] = value

    def __getattr__(self, name):
        if name == 'AsString':
            return str(self.__dict__['value'])
        elif name == 'AsInteger':
            return int(self.__dict__['value'])
        elif name == 'AsFloat':
            return float(self.__dict__['value'])
        elif name == 'AsDate':
            return self.__dict__['value']
        elif name == 'AsTime':
            return self.__dict__['value']
        elif name == 'AsDateTime':
            return self.__dict__['value']
        elif name == 'AsCurrency':
            return ('{:.4f}'.format(self.__dict__['value']))
    
class TSQL:
    def __init__(self):
        self.text = ''

    def Add(self, text):
        self.text = self.text + text

    def Text(self, text = ''):
        if(len(text)):
            self.text = text
        return self.text

    def SaveTofile(self, filename):
        f = open(filename,"a+")
        f.write(self.text)
        f.close()

    def LoadFromFile(self, filename):
        f = open(filename,"r")
        self.text = f.read()
        f.close()
    


    



