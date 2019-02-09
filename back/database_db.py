import sqlite3, csv

class Database():

    def connect_db(self):
        con = sqlite3.connect("FarmaJusta.db")
        return con


    def create_tables(self):
        createMedicamentoQuery = """CREATE TABLE medicamento (principioativo text,laboratorio text,
                                codggrem text, registro text, ean1 text, ean2 text, ean3 text,
                                produto text, apresentacao text, clsterapeutica txt, 
                                pmc20 text, iscomercializado text)"""

        createDenunciaQuery = """CREATE TABLE denuncia (nome text,cpf text, contato text,
                                estabelecimento text, localizacaoestabelecimento text)"""

        con= self.connect_db()
        cur = con.cursor()
        cur.execute(self.createMedicamentoQuery)
        cur.execute(self.createDenunciaQuery)
        con.commit()
        con.close()


    def popula_medicamento(self):
        con, cur = self.connect_db()


        # with open('teste_csv.csv', newline='') as csvfile:
        #      reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        #      print("ARQUIVO CSV:")
        #      for row in reader:
        #          print(', '.join(row))
        #          cur.execute('INSERT INTO testeCSV VALUES (?,?,?)', row)
        #          con.commit()
        #
        # cur.execute('SELECT * FROM testeCSV')
        # results = cur.fetchall()
        # for r in results:
        #      print(r)

        #con.close()
        pass

    def consulta_medicamento_registro(self, cod_registro):
        con = self.connect_db()
        cur = con.cursor()
        cur.execute('SELECT * FROM medicamento where registro = ?', [cod_registro])
        results = list(cur.fetchall())

        print(results)

        for row in results:
            print(row)

        print("SUCESS")
        return results
