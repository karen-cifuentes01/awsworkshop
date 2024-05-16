import pymysql

db_host = 'db-awscourse.ch2mia4mgchf.us-east-1.rds.amazonaws.com'
db_user = 'admin'
db_passw = 'awsCurso1'
db_name = 'db_recipes'

def connectionSQL():
    try:
        connection = pymysql.connect(
            host = db_host,
            user = db_user,
            password = db_passw,
            database = db_name
            )
        print("succesfull connection")
        return connection
    except Exception as err:
        print("failed connection", err)
        return None
        
def insert_reciperecord(RecipeName, Description, CategorySelected, PreparationTime, Servings, Ingredients, Steps):
    query = "INSERT INTO Recipes (RecipeName, Description, Category, PreparationTime, Servings, Ingredients, Steps, CreationDate) VALUES ('"+RecipeName+"', '"+Description+"', '"+CategorySelected+"', '"+PreparationTime+"', '"+Servings+"', '"+Ingredients+"', '"+Steps+"', NOW())"
    try:
        connection = connectionSQL()
        if connection != None:
            cursor = connection.cursor()
            cursor.execute(query)
            connection.commit()
            print("Recipe added")
            return True
        else:
            print("Error in the connection")
            return False
    except Exception as err:
        print("Error creating the recipe", err)
        return False


def consult_recipeInformation(recipeName):
    query = "SELECT * FROM Recipes WHERE RecipeName = '" + recipeName + "'"
    try:
        connection = connectionSQL()
        cursor = connection.cursor()
        if connection != None:
            cursor.execute(query)
            result = cursor.fetchall()
            return result
        else:
            print("Error in the connection")
            return None
    except Exception as err:
        print("Error consulting the recipe", err)
        return None