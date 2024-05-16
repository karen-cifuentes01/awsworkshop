from flask import render_template, request
from server import app
from controller.control import func_insert_recipe, func_consult_recipedata

@app.route('/')
def home_page():
    return render_template("home.html")
    
@app.route('/addRecipe')
def addRecipe_page():
    return render_template("addRecipe.html")
    
@app.route('/consultRecipe')
def consultRecipe_page():
    return render_template("consultRecipe.html")
    
@app.route('/insert_recipe', methods=["post"])
def insert_recipe():
    return func_insert_recipe()

@app.route("/consult_recipedata", methods=["post"])
def consult_recipedata():
    return func_consult_recipedata()