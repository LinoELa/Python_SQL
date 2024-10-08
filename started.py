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

