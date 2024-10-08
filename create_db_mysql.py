# Conectar 

import pymysql



# Crear la coneccion
mybd = pymysql.connect(

    # puede ser difente al de la base de datos
    user= "root",
    password = "mysql@123", 

    # tiene que ser igual al de la base de datos
    database = "w3school",
    host="localhost",
    port= 3306,
)


cursor = mybd.cursor()
print("Todo Correcto !")


# 

# otra forma General de W3school
# import mysql.connector --- SI NO FUNCIONA PUES : import pymysql
# mysql.connector - pymysql
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )

# print(mydb)