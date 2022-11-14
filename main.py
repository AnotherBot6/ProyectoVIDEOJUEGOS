import csv
import matplotlib.pyplot as plt
import math as mt

# Function which returns the Top 10 best-sellers.
def top_10(data):
    print('\nThe top 10 best-sellers are: ')
    top10 = ''
    top_10 = data[1][1:11]
    cont = 1
    for j in top_10:
      top10 = top10 + ' ' + data[0][cont] + '. ' + j + ' [' + data[2][cont] + ']' + '\n'
      cont = cont + 1
    
    top10 = top10 + f'The best seller sold {data[10][1]} million copies.\n '

    print(top10)

    print('¿Desea ver la grafica de sus ventas?')
    res = -1
    while res != 0 or res != 0:
        res=int(input('Presione 1 para SI y 0 para NO. \n'))
        if res == 1 or res == 0:
            break
    if (res==1):
        #[float(i) for i in data[6][1:11]]
        plt.figure(figsize=(25,7))
        x=data[1][1:11]
        lista_ventas=data[10][1:11]
        y=[float(i) for i in lista_ventas]
        
        
        plt.bar(x,y)
        plt.xlabel('Juegos')
        plt.ylabel('Ventas Globales')
        plt.title('Top 10 de ventas')
        plt.show()
        
    
    else:
        return ''

def worst_sellers(data):
    print('\nThe top 10 worst-sellers are: ')
    worst = ''
    worst_10 = data[1][len(data[2])-10:len(data[2])]
    cont = len(data[2])- 10
    for j in worst_10:
      worst = worst + ' ' + data[0][cont] + '. ' + j + ' [' + data[2][cont] + ']' + '\n'
      cont = cont + 1
    worst = worst + f"All of these games got ~{data[10][cont-1]} million copies sold\n"
    return worst

def graficas(data):
    print('Grafica de ventas por region. \n')
    print('6. NA_Sales')
    print('7. EU_Sales')
    print('8. JP_Sales')
    print('9. Other_Sales')
    print('10. Global_Sales')
    res_1= 0
    while res_1 < 6 or res_1 > 10:
        res_1=int(input('Selecciona el primer elemento a graficar. \n'))
        if not (res_1 < 6 or res_1 > 10):
            break
        
    plt.figure(figsize=(24,7))
    x=data[0][1:100]
    lista_ventas=data[res_1][1:100]
    y=[float(i) for i in lista_ventas]
    
    
    
    plt.plot(x,y, marker='o',label=data[res_1][0])
    plt.xlabel('Juegos (solo el numero)')
    plt.ylabel('Ventas')
    plt.title('Ventas por region')
    plt.legend() 
    plt.show()
        
    print('¿Quieres agregar otra grafica')
    print('Presione 1 para SI y 0 para NO')
    res_2=int(input())
    
    if res_2==1:
        print('Selecciona el segundo elemento a graficar')
        print('6. NA_Sales')
        print('7. EU_Sales')
        print('8. JP_Sales')
        print('9. Other_Sales')
        print('10. Global_Sales')
        res_4=int(input())
    
        plt.figure(figsize=(25,7))
        x=data[0][1:100]
        lista_ventas=data[res_1][1:100]
        y=[float(i) for i in lista_ventas]
        

        x2=data[0][1:100]
        lista_ventas=data[res_4][1:100]
        y2=[float(i) for i in lista_ventas]
        
        
        plt.plot(x,y, marker='o',label=data[res_1][0])
        plt.plot(x2,y2, marker='o',label=data[res_4][0])
        plt.xlabel('Juegos (solo el numero)')
        plt.ylabel('Ventas')
        plt.title('Ventas por region')
        plt.legend() 
        plt.show()
        
        print('¿Quieres agregar otra grafica')
        print('Presione 1 para SI y 0 para NO')
        res_5=int(input())
        
        if res_5==1:
            print('Selecciona el tercer elemento a graficar')
            print('6. NA_Sales')
            print('7. EU_Sales')
            print('8. JP_Sales')
            print('9. Other_Sales')
            print('10. Global_Sales')
            res_6=int(input())
        
            plt.figure(figsize=(25,7))
            x=data[0][1:100]
            lista_ventas=data[res_1][1:100]
            y=[float(i) for i in lista_ventas]
            
            
            x2=data[0][1:100]
            lista_ventas=data[res_4][1:100]
            y2=[float(i) for i in lista_ventas]
            

            x3=data[0][1:100]
            lista_ventas=data[res_6][1:100]
            y3=[float(i) for i in lista_ventas]
            
            plt.plot(x,y, marker='o',label=data[res_1][0])
            plt.plot(x2,y2, marker='o',label=data[res_4][0])
            plt.plot(x3,y3, marker='o',label=data[res_6][0])
            plt.xlabel('Juegos (solo el numero)')
            plt.ylabel('Ventas')
            plt.title('Ventas por region')
            plt.legend() 
            plt.show()
            
            
            print('¿Quieres agregar otra grafica')
            print('Presione 1 para SI y 0 para NO')
            res_7=int(input())
            
            if res_7==1:
                print('Selecciona el cuarto elemento a graficar')
                print('6. NA_Sales')
                print('7. EU_Sales')
                print('8. JP_Sales')
                print('9. Other_Sales')
                print('10. Global_Sales')
                res_9=int(input())
            
                plt.figure(figsize=(25,7))
                x=data[0][1:100]
                lista_ventas=data[res_1][1:100]
                y=[float(i) for i in lista_ventas]
                
                
                x2=data[0][1:100]
                lista_ventas=data[res_4][1:100]
                y2=[float(i) for i in lista_ventas]
                

                x3=data[0][1:100]
                lista_ventas=data[res_6][1:100]
                y3=[float(i) for i in lista_ventas]
                    
                x4=data[0][1:100]
                lista_ventas=data[res_9][1:100]
                y4=[float(i) for i in lista_ventas]
                
                plt.plot(x,y, marker='o',label=data[res_1][0])
                plt.plot(x2,y2, marker='o',label=data[res_4][0])
                plt.plot(x3,y3, marker='o',label=data[res_6][0])
                plt.plot(x4,y4, marker='o',label=data[res_9][0])
                plt.xlabel('Juegos (solo el numero)')
                plt.ylabel('Ventas')
                plt.title('Ventas por region')
                plt.legend() 
                plt.show()

def portables(data):
  print('\nThe top 20 best-sellers in Portable consoles are: ')

  nova = [] 
  novacol0 = []
  novacol1 = []
  novacol2 = []
  novacol3 = []
  novacol4 = []
  novacol5 = []
  novacol6 = []
  novacol7 = []
  novacol8 = []
  novacol9 = []
  novacol10 = []


  for row_i in range(len(data[2][:])): # For each row in column "Platform"
    
    if '3DS' == data[2][row_i] or 'DS' == data[2][row_i] or 'PSV' == data[2][row_i] or 'PSP' == data[2][row_i]: 
      # Check if the row includes Wii or NES
      # If it does, append all the columns of that row. 
      novacol0.append(data[0][row_i])
      novacol1.append(data[1][row_i])
      novacol2.append(data[2][row_i])
      novacol3.append(data[3][row_i])
      novacol4.append(data[4][row_i])
      novacol5.append(data[5][row_i])
      novacol6.append(data[6][row_i])
      novacol7.append(data[7][row_i])
      novacol8.append(data[8][row_i])
      novacol9.append(data[9][row_i])
      novacol10.append(data[10][row_i])
  # Combine all into one database    
  nova.append(novacol0)
  nova.append(novacol1)
  nova.append(novacol2)
  nova.append(novacol3)
  nova.append(novacol4)
  nova.append(novacol5)
  nova.append(novacol6)
  nova.append(novacol7)
  nova.append(novacol8)
  nova.append(novacol9)
  nova.append(novacol10)
  
  top_portN = nova[1][1:21]  
  cont = 0
  top20Port = ''

  for j in top_portN:
    top20Port = top20Port + f'[{cont+1}]' + ' ' + nova[0][cont] + '. ' + j + ' [' + nova[2][cont] + ']' + '\n'
    cont = cont + 1
  
  top20Port += f'\nThe best selling game, {nova[1][1]}, sold {nova[10][1]} million copies.\n'

  return top20Port


def test2(data):
  x=len(data[1][1])
  return x



def Analitica(data):
    a=0
    while a==0:
        print('¿Que tipo de analisis deseas hacer?')
        print('Para finalizar presione 0')
        print('1. Promedio')
        print('2. Maximos y minimos')
        print('3. Desviacion estandar')
        ana=int(input())
        print('¿Sobre que columna quieres hacer analisis?')
        print('6. NA_Sales')
        print('7. EU_Sales')
        print('8. JP_Sales')
        print('9. Other_Sales')
        print('10. Global_Sales')
        op=int(input())
        if ana==0 or op==0:
            a=a+1
            print('Finalizo la opcion')

        elif ana==1:
            suma=0
            lista_largo=len(data[op][1:300])
            lista_ventas=data[op][1:300]
            y=[float(i) for i in lista_ventas]
            suma=sum(y)
            promedio=suma/lista_largo
            print('-'*80)
            print('El promedio de la columna ',data[op][0] , 'es de ', str(promedio))
            print('-'*80)
            
            
        elif ana==2:
            print('-'*80)
            print('El valor maximo de la columna de', data[op][0] ,'es de ',data[op][1])
            lista_ventas=data[op][1:300]
            y=[float(i) for i in lista_ventas]
            y.sort()
            print('El valor maximo de la columna de', data[op][0] ,'es de ',y[0])
            print('-'*80)
        
        
        elif ana==3:
            suma=0
            suma_Total=0
            lista_largo=len(data[op][1:300])
            lista_ventas=data[op][1:300]
            y=[float(i) for i in lista_ventas]
            suma=sum(y)
            promedio=suma/lista_largo
            for n in lista_ventas:
                a=0
                s=y[a]
                razon=(s-promedio)**2
                suma_Total=suma_Total+razon
                a=a+1
            res=suma_Total/lista_largo
            desviacion=mt.sqrt(res)
            print('La desviacion estandar de la columna ', data[op][0] ,'es de ',str(desviacion))
            
            
            
        elif ana<0 or ana>2 or op<6 or op>10:
            print('Opcion no valida, intente otra vez')


# Main function (Home)
def Options():
    res = '*'
    while res == '*':
        res = input('Presione cualquier tecla para regresar al menu o "*" para salir. \n')
        if res != '*':
            main()
        elif res == '*':
            print('Fin del programa. \n')
            break
def main():
    # Declare matrix (dataframe)
    vg_matrix = []
    # Declare lists (columns)
    l_rank = []
    l_name = []
    l_platf = []
    l_year = []
    l_genre = []
    l_publish = []
    l_GLSales = []
    l_NASales = []
    l_EUSales = []
    l_JPSales = []
    l_OtherSales = []
    l_Rating = []
    
    # Read vgsales.csv
    with open('vgsales.csv', newline='') as csvfile:
        variable = csv.reader(csvfile)
        for row in variable:
            # Column indexes
            l_rank.append(row[0])
            l_name.append(row[1])
            l_platf.append(row[2])
            l_year.append(row[3])
            l_genre.append(row[4])
            l_publish.append(row[5])
            l_NASales.append(row[6])
            l_EUSales.append(row[7])
            l_JPSales.append(row[8])
            l_OtherSales.append(row[9])
            l_GLSales.append(row[10])
            l_Rating.append(row[15])
            # Append columns
            vg_matrix.append(l_rank)
            vg_matrix.append(l_name)
            vg_matrix.append(l_platf)
            vg_matrix.append(l_year)
            vg_matrix.append(l_genre)
            vg_matrix.append(l_publish)
            vg_matrix.append(l_NASales)
            vg_matrix.append(l_EUSales)
            vg_matrix.append(l_JPSales)
            vg_matrix.append(l_OtherSales)
            vg_matrix.append(l_GLSales)
            vg_matrix.append(l_Rating)

    # Home, sweet home.    
   
    print('-'*80)
    print('~   Bienvenid@   ~')
    print('Seleccione alguna opcion:\n')
    print('1. Top 10 de juegos mas vendidos ')
    print('2. Top 10 de juegos peor vendidos')
    print('3. Gráficas de ventas')
    print('4. Datos estadisticos')
    print('5. Top 20 juegos de consolas portátiles recientes. ')
    print('\nPor favor, Ingrese solo el numero de opción.')
    print('-'*80)
    
    # Ask for option
    opcion = int(input())
    # Call functions
    if opcion== 1:
      print(top_10(vg_matrix))
    elif opcion==2:
      print(worst_sellers(vg_matrix))
    elif opcion==3:
      print(graficas(vg_matrix))
    elif opcion==4:
      print(Analitica(vg_matrix))
    elif opcion==5:
      print(portables(vg_matrix))
    else: 
      print('¿Quieres salir del programa? ')
    Options()
    
# Run the program
if True == True:
    main()
