function consult_recipedata(){
    
    let recipeName = document.getElementById("recipeName").value
    
    if(recipeName=="")
    {
        alert("Recipe name is empty!")
    }
    else
    {
        let obj_information = {"recipeName":recipeName}
        fetch('/consult_recipedata', {
            "method":"post",
            "headers":{"content-type":"application/json"},
            "body": JSON.stringify(obj_information)
        })
        .then(resp => resp.json())
        .then(data => {
            if (data.status == "ok") {
                descriptionText.innerText = data.description;
                categoryText.innerText = data.categoryText;
                preparationTime.innerText = data.preparationtime;
                servingsInformation.innerText = data.servings;
                ingredientsList.innerText = data.ingredients;
                stepsInformation.innerText = data.steps;
            }
            else {
                alert("The recipe was not found")
                document.getElementById("recipeName").value = "";
                descriptionText.innerText = "";
                descriptionText.innerText = "";
                categoryText.innerText = "";
                preparationTime.innerText = "";
                servingsInformation.innerText = "";
                ingredientsList.innerText = "";
                stepsInformation.innerText = "";
            }
        })
        .catch(err => alert(err))
    }
}
