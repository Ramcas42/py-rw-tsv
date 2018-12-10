import pandas as pd

#with open('df/luna.csv',encoding='UTF-16') as fin, open('df/luna1.csv', 'w',encoding='UTF-16') as fout:
   #for line in fin:
       # fout.write(line.replace('\t', ','))

df = pd.read_csv("df/luna.csv", encoding='ISO-8859-1')

data2 = df.rename({'first_name':'Nombre', 'last_name':'Apellido', 'phone_number':'Numero', 'email':'Correo', 'adset_name':'Campaña', "created_time" : "Hora" }, axis='columns')

data3 = data2[['Nombre','Apellido','Numero',"Correo", "Campaña","Hora"]] 

print(data3)

data3.to_excel("df/to_merge/luna.xlsx")