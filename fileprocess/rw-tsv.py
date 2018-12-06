import pandas as pd

df=pd.read_csv('df/lunarena1.csv',delimiter='\t',encoding='utf-16')

data2 = df.rename({'first_name':'Nombre', 'last_name':'Apellido', 'phone_number':'Numero', 'email':'Correo', 'adset_name':'Campaña', "created_time" : "Hora" }, axis='columns')

data3 = data2[['Nombre','Apellido','Numero',"Correo", "Campaña","Hora"]] 

print(data3)

gdrivepath = "gdrive/lunarena1.xlsx"

data3.to_excel(gdrivepath)