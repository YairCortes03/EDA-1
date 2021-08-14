#proycto final sistema indicador de semáforo Covid
import pandas as pd
import os
os.system("cls")
#Declarar las cadenas
op='0'
#
registros=[]
casospositivos=[]
casosnegativos=[]
print("\n\t\t Sistema de prevención sanitaria")
while(op!='2'):
		print(" 1) Agregar\n 2) resultados\n")
		op=input("elige una opción: ")
		if op=='1':
			edad=input("Edad: ")
			indice=float(input("indice: "))
			#casos negativos
			if indice<0.8:
				print("El usuario se encuentra sano :)")
				neg=edad+','+str(indice)+'\n'
				casosnegativos.append(neg)
				reg=edad+','+str(indice)+','+'0'+','+'1'
				prom=0
				reg=reg+','+str(prom)+'\n'
			#casos positivos
			elif indice>=0.8:
				print("el usuario tiene covid :c")
				pos=edad+','+str(indice)+'\n'
				casospositivos.append(pos)
				reg=edad+','+str(indice)+','+'1'+','+'0'
				prom=edad
				reg=reg+','+str(prom)+'\n'
				input("precione enter para obtener las recomendaciones adecuadas")
				os.system("Prueba_de_Antígenos_Covid.pdf")
			else:
				print("opción no valida")
			registros.append(reg)
		elif op=='2':
			print("gracias por usar mi programa")
		else:
			print("opción no valida :(")
#abre un archivo y recopila los datos
print(registros)
a=open("DattaBase.csv","a")
a.writelines(registros)
a.close()
#lectura de la base de datos con la libreria pandas
datos=pd.read_csv('DattaBase.csv',header=0)
#datos recopilados
print("\n\t\t\tDatos recopilados\n")
print("\n",datos[['EDAD','INDICE','CASOS POSITIVOS','CASOS NEGATIVOS']])
input("presione enter para continuar")
os.system("cls")
#promedio
pos=(datos[datos['EDADES POSITIVAS']>0])
pos=(pos['EDADES POSITIVAS'])
suma=sum(pos)
total=len(pos)
if(total!=0):#condición para cero casos de covid
	promedio=suma/total
else:
	promedio=0
print("\n\t\tEl promedio de las edades de los infectados es:",promedio)
#semáforo
todos=(datos['EDAD'])
todos=len(todos)
#porcentajes de referencia para el semáforo
p1=todos*.30 #representa el 30% de total de datos ingresados
p2=todos*.70 #representa el 70% del total de datos ingresados
print("\n\n\t\tNúmero de casos analizados:",todos,"\n")
print("\n\t\tCasos positivos a covid-19:",total,"\n")
porcentaje=(total*100)/todos
print("\n\t\tPorcentaje de infección:",porcentaje,"%")
#condiciones del semáforo
if(total==0):#Condición para el semáforo verde
	print("\n\t\t\tEl semáforo epidemiologico es VERDE") 
elif(total<=p1):#Condición para el semáforo Amarillo
	print("\n\t\t\tEl semáforo epidemiologico es AMARILLO")
elif(total>p1):
	if(total<=p2):#Condición para el semáforo naranja 
		print("\n\t\t\tEl semáforo epidemiologico es NARANJA")
	elif(total>p2):#Condición para el semáforo rojo
		print("\n\t\t\tEl semaforo epidemiologico es ROJO")
	else:
		print("valor no admitido")
else:
	print("valor no admitido")
input("Precione enter para acceder a la base de datos")
print("Accediendo a la base de datos...")

os.system("DattaBase.csv")
input("presione enter para finalizar")