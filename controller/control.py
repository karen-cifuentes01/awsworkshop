from flask import render_template, request, jsonify
from database.db import connectionSQL, insert_reciperecord, consult_recipeInformation
from controller.s3_control import connection_s3, upload_file_s3, save_file

def func_insert_recipe():
    data_recipe = request.form
    photo = request.files["photo"]
    RecipeName, Description, CategorySelected, PreparationTime, Servings, Ingredients, Steps = data_recipe["RecipeName"], data_recipe["Description"], data_recipe["CategorySelected"], data_recipe["PreparationTime"], data_recipe["Servings"], data_recipe["Ingredients"], data_recipe["Steps"]
    recipeOnDB = consult_recipeInformation(RecipeName)
    if recipeOnDB != None and len(recipeOnDB) != 0:
        return"<h1> Error creating the Recipe: The recipe already exists! </h1>"
    else:
        insertResponse = insert_reciperecord(RecipeName, Description, CategorySelected, PreparationTime, Servings, Ingredients, Steps)
        if insertResponse: 
            s3_connection = connection_s3()
            photo_path = save_file(RecipeName, photo)
            upload_file_s3(s3_connection, photo_path)
            return "<h1> Recipe added </h1>"
        else:
            return"<h1> Error creating the Recipe </h1>"
   

def func_consult_recipedata():
    data_information = request.get_json()
				  
    result = consult_recipeInformation(data_information["recipeName"])
    if result != None and len(result) != 0:
        description = result[0][2]
        categoryText = result[0][3]
        preparationtime = result[0][4]
        servings = result[0][5]
        ingredients = result[0][6]
        steps = result[0][7]
        resp_data = {"status":"ok",
            "description": description,
            "categoryText": categoryText,
            "preparationtime": preparationtime,
            "servings": servings,
            "ingredients": ingredients,
            "steps": steps
        }
    else:
        resp_data = {"status":"error"}
				 
    return jsonify(resp_data)
    