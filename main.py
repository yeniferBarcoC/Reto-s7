"""Reto semana 7
    Yenifer Barco Castrilón
    20-06-2021
"""

#------------- Librerias -------------------------
import pandas as pd

#------------- Abriendo el archivo de excel-------------------------

#Se carga el archivo en un Dataframe
df=pd.read_csv("D:/Documents/Mision tic/Fundamento de programacion/Modulo 7 - Redes y data frames/reto semana 7/Casos_positivos_de_COVID-19_en_Colombia.csv")    

#Obtener la informacion general del archivo
df.info()

#Numero de elementos
num = df.size
print("\nNumero de elementos: ",num,"\n")

#Primeros 7 casos a que municipio corresponden
print(df["Nombre municipio"].head(7),"\n")

#Cuantas Sexo==F Edad<2 AND Nombre municipio==CALI AND Recuperado==Activo
print("Numero de niñas: ", len(df[(df["Edad"]<2)&(df["Nombre municipio"]=="CALI")&(df["Recuperado"]=="Activo")&(df["Sexo"]=="F")].index),"\n")

#Nombre de las columnas
print(df.columns,"\n")

#cantidad de Sexo==M AND Sexo==F 
print("Numero hombres: ", len(df[df["Sexo"]=="M"].index),"\tNumero mujeres: ", len(df[df["Sexo"]=="F"].index), "\n")

#Cuantos Sexo==M AND Edad<8 AND Nombre municipio=="ARMENIA" AND Recuperado=="Activo"
print("Numero de niños: ", len(df[(df["Edad"]<8)&(df["Nombre municipio"]=="ARMENIA")&(df["Recuperado"]=="Activo")&(df["Sexo"]=="M")].index),"\n")

#Cuantos Sexo==M AND Edad<40 AND Nombre del país=="ITALIA"
print("Numero de hombres de italia: ", len(df[(df["Edad"]<40)&(df["Nombre del país"]=="ITALIA")&(df["Sexo"]=="M")].index),"\n")


    