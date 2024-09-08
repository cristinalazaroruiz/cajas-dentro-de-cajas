import math
def cajas(a, b, c, peso_estuche, Lmax=2100, Wmax=800, max_peso=25, max_altura=2100, min_estuches=10, max_estuches=75,r=10):
    #argumentos dentro de la función:
    #a,b,c = largo, ancho y alto de  la caja pequeña (en mm)
    #peso_estuche: peso de la caja pequeña (en kg)
    #max_peso = peso máximo de todo el conjunto de cajas grandes (en kg)
    #Lmax, Wmax, max_altura = largo, ancho y alto máximo del soporte de la caja grande (dimensiones del palé) (en mm)
    #min_estuches y  max_estuches: cantidad  mínima y  máxima de cajas pequeñas a considerar en cada caja grande
    #estos argumentos los recuperamos de la interfaz gráfica de tkinter:

    combinaciones_posibles = []
    ranking_mejores_cajas = []
    

    dimensiones_palet = (Lmax, Wmax)  # Dimensiones estándar del palé europeo en mm (L x W)
    
    # Recorrer todas las posibles dimensiones de la caja grande dentro de las restricciones
    for L in range(a if a<b else b, Lmax+1, math.gcd(a,b)):  
        for W in range(a if a<b else b, Wmax+1, math.gcd(a,b)):
            print(f"Probando W={W}")
            for H in range(c, max_altura + 1, c):
                print(f"Probando H={H}")
                
                # Número de estuches en cada orientación
                num_cajas_horiz = (L // a) * (W // b) * (H // c)
                num_cajas_lado = (L // b) * (W // a) * (H // c)
                
                # Probar todas las combinaciones posibles de estuches en ambas orientaciones
                for n_horiz in range(num_cajas_horiz + 1):
                    n_lado = num_cajas_lado - n_horiz

                    if n_lado < 0:
                        continue
                    
                    numero_cajas = n_horiz + n_lado
                    print(f"Combinación: Horizontal={n_horiz}, Lado={n_lado}, Total={numero_cajas}")

                    #Condiciones a la hora de sacar todas las combinaciones posibles 
                    
                    if min_estuches <= numero_cajas <= max_estuches:
                        peso_total = numero_cajas * peso_estuche
                        if peso_total <= max_peso:
                            volumen_total = L * W * H #volumen cada caja grande 
                            volumen_ocupado = (n_horiz * a * b * c) + (n_lado * b * a * c) #volumen de cada caja grande ocupado por los estuches
                            volumen_vacio = volumen_total - volumen_ocupado #volumen vacío de cada caja grande (volumen no ocupado por los estuches)
                            
                            
                            # Calcular cuántas cajas grandes caben en un palé
                            num_cajas_L = dimensiones_palet[0] // L
                            num_cajas_W = dimensiones_palet[1] // W
                            num_cajas_H = max_altura // H
                            num_cajas_palet = num_cajas_L * num_cajas_W * num_cajas_H
                            volumen_pale_vacio = (Lmax*Wmax*max_altura)-(volumen_total*num_cajas_palet) #volumen del pale - volumen que ocupan todas las cajas grandes 
                        
                            #condiciones finales para las combinacines seleccionadas 

                            if num_cajas_palet > 0 and volumen_vacio >= 0:
                                combinacion = [
                                    L, W, H, volumen_total, volumen_ocupado, 
                                    volumen_vacio, numero_cajas, peso_total, volumen_pale_vacio,
                                    f"horizontal: {n_horiz}, de lado: {n_lado}", num_cajas_palet,
                                ]
                                combinaciones_posibles.append(combinacion)
                                ranking_mejores_cajas.append(combinacion)
    
    #ordenar la lista de combinaciones_posibles (para luego poder hacer los tests, no por otra cosa)
    #ordenamos primero L de  menor a mayor, luego W, luego H, luego n estuches y finalmente n cajas horizontal (todo de menor a mayor)
    ranking_mejores_cajas.sort(key=lambda x: (x[0],x[1],x[2], x[6],x[9]) )
    
    # Ordenar las combinaciones por número de estuches (descendente) y luego por volumen total (ascendente)
    #TODO: se puede ordenar en basae a otro criterio también. En este, se proriza primero el máximo número posible de estuches por caja grande, luego el mínimo volumen vacío por caja grande y finalmente el mínimo volumen vacío por palé (o caja más grande donde caben las cajas grandes)
    ranking_mejores_cajas.sort(key=lambda x: (-x[6], x[5], x[8]))

    # Mantener solo las 10 mejores combinaciones (las r cominaciones elegidas)
    mejores_combinaciones = ranking_mejores_cajas[:r]

    # Guardar todas las combinaciones posibles en un archivo
    with open("todas_combinaciones.txt", "w") as fichero_todas:
        for combinacion in combinaciones_posibles:
            resultado = "L:{}, W:{}, H:{}, Volumen Total:{}, Volumen Ocupado:{}, Volumen Vacio:{}, Estuches: {}, Peso Total:{}kg, Volumen pale vacio: {}, Orientaciones:{}, Cajas por Palé:{}\n".format(
                combinacion[0], combinacion[1], combinacion[2], combinacion[3], combinacion[4], combinacion[5], 
                combinacion[6], combinacion[7], combinacion[8], combinacion[9], combinacion[10])
            fichero_todas.write(resultado)
    
    # Guardar las mejores combinaciones en otro archivo
    with open("ranking_priorizar_minimo_volumen.txt", "w") as fichero_mejores:
        for combinacion in mejores_combinaciones:
            resultado = "L:{}, W:{}, H:{}, Volumen Total:{}, Volumen Ocupado:{}, Volumen Vacio:{}, Estuches: {}, Peso Total:{}kg, Volumen pale vacio: {}, Orientaciones:{}, Cajas por Palé:{}\n".format(
                combinacion[0], combinacion[1], combinacion[2], combinacion[3], combinacion[4], combinacion[5], 
                combinacion[6], combinacion[7], combinacion[8], combinacion[9], combinacion[10])
            fichero_mejores.write(resultado)
            print("Mejor combinación:", resultado)

    # Retornar las listas de combinaciones para los unitests 
    return combinaciones_posibles, mejores_combinaciones
# Ejemplo de uso de la función
if __name__ == "__main__":
    cajas(200, 250, 100, peso_estuche=0.3)  # Supón que cada estuche pesa 0.3 kg
    #cajas(100,100,100,0.1, max_altura=200, min_estuches=1, Lmax=200, Wmax=200)
    

