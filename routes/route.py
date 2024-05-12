from flask import render_template, request, jsonify
from server import app
from database.db import connectionSQL, insert_reciperecord, consult_recipeInformation

@app.route('/')
def home_page():
    connectionSQL()
    return render_template("home.html")
    
@app.route('/addRecipe')
def addRecipe_page():
    return render_template("addRecipe.html")
    
@app.route('/consultRecipe')
def consultRecipe_page():
    return render_template("consultRecipe.html")
    
    
@app.route('/insert_recipe', methods=["post"])
def insert_recipe():
    data_recipe = request.form
    RecipeName, Description, CategorySelected, PreparationTime, Servings, Ingredients, Steps = data_recipe["RecipeName"], data_recipe["Description"], data_recipe["CategorySelected"], data_recipe["PreparationTime"], data_recipe["Servings"], data_recipe["Ingredients"], data_recipe["Steps"]
    insert_reciperecord(RecipeName, Description, CategorySelected, PreparationTime, Servings, Ingredients, Steps)
    return render_template("addRecipe.html")

@app.route("/consult_recipedata", methods=["post"])
def consult_recipedata():
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