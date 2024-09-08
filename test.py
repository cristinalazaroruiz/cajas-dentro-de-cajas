#En este fichero  comprobamos que la función cajas() hace exactamente lo que queremos usando un test unitario 
import unittest
import pandas as pd 
from funcion_definitiva import cajas

class Prueba(unittest.TestCase):
    #nuestra función devuelve dos listas, una con todas las combinaciones y otra con las diez mejores. Debemos generar dos listas de prueba que contenga  lo mismo. 
    def setUp(self):
        self.lista_prueba = []
        self.ranking_prueba = []
        
        # Leer el archivo Excel en el que hemos preparado los datos de prueba, con todas las combinaciones para una caja de 100x100x100mm y el ranking de las 10 mejores
        df = pd.read_excel("cajas_pruebas.xlsx",sheet_name="combinaciones", header=None)
        
        # Seleccionar solo las filas de la 2 a la 36 (índice 1 a 35 en pandas) Los datos del excel solo están en esas filas. 
        df = df.iloc[1:36]

        # Recorrer cada fila y convertirla en una sublista con la nomenclatura específica que hemos usado en la función original. 
        for index, row in df.iterrows():
            L = row[0]
            W = row[1]
            H = row[2]
            volumen_total = row[3]
            volumen_ocupado = row[4]
            volumen_vacio = row[5]
            numero_cajas = row[6]
            peso_total = row[7]
            volumen_pale_vacio = row[8]
            n_horiz = row[9]
            n_lado = row[10]
            num_cajas_palet = row[11]
            
            # Crear la sublista con la nomenclatura
            sublista = [
                L, W, H, volumen_total, volumen_ocupado, volumen_vacio,
                numero_cajas, peso_total, volumen_pale_vacio,
                f"horizontal: {n_horiz}, de lado: {n_lado}", num_cajas_palet
            ]
            
            # Agregar la sublista a self.lista_prueba
            self.lista_prueba.append(sublista)

        #ahora hacemos lo mismo pero con el excel con las mejores combinaciones, que está en otra hoja del fichero excel
        #Primero abrimos la hoja excel con las combinaciones  ordenadas según la función del ranking
        df2 = pd.read_excel("cajas_pruebas.xlsx",sheet_name="ranking", header=None)

        #seleccionamos solo las diez primeras posiciones del ranking 
        df2 = df2.iloc[1:11]
        
        # Recorrer cada fila y convertirla en una sublista con la nomenclatura específica que hemos usado en la función original. 
        for index, row in df2.iterrows():
            L = row[0]
            W = row[1]
            H = row[2]
            volumen_total = row[3]
            volumen_ocupado = row[4]
            volumen_vacio = row[5]
            numero_cajas = row[6]
            peso_total = row[7]
            volumen_pale_vacio = row[8]
            n_horiz = row[9]
            n_lado = row[10]
            num_cajas_palet = row[11]
            
            # Crear la sublista con la nomenclatura
            sublista = [
                L, W, H, volumen_total, volumen_ocupado, volumen_vacio,
                numero_cajas, peso_total, volumen_pale_vacio,
                f"horizontal: {n_horiz}, de lado: {n_lado}", num_cajas_palet
            ]
            
            # Agregar la sublista a self.lista_prueba
            self.ranking_prueba.append(sublista)


    def test(self):
        combinaciones, ranking = cajas(100, 100, 100, 0.1, max_altura=200, min_estuches=1, Lmax=200, Wmax=200)
        #pruebbas porque salían errores al principio
        """ for s in combinaciones:
            print (s)
        print("================================================================================================")
        for i in ranking:
            print (i) 
        print(cajas(100, 100, 100, 0.1, max_altura=200, min_estuches=1, Lmax=200, Wmax=200))
        print(len(ranking))
        print(len(self.ranking_prueba))
        todoOk = [0] * len(ranking)
        for i,c in enumerate(self.ranking_prueba):
            for f,l in enumerate(ranking):
                if c == l:
                    todoOk[f]+=1
        print(todoOk)  """
        self.assertEqual(combinaciones, self.lista_prueba)
        self.assertEqual(ranking, self.ranking_prueba)

if __name__ == "__main__":
    unittest.main()

#TODO: terminar las pruebas