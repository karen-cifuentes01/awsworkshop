function add_recipe(){
    alert("Recipe Added successfully")
}

function load_dropdowns()
{
    var myArrayCategories = new Array("Appetisers", "Baking", "Breakfast", "Brunch", "Dinner", "Drinks", "Lunch", "Pancakes",
    "Pastas", "Rice", "Salads", "Sides", "Smoothies", "Snacks", "Soups", "Vegetarian");

    var myArrayIngredients = new Array ("Almonds", "Apple", "Avocado", "Bacon", "Banana", "Beans", "Beef", "Beef ribs", 
    "Brisket", "Brown sugar", "Cheese", "Chicken breast", "Chicken legs", "Chicken thighs", "Chicken wings"
    , "Chocolate", "Cinnamon", "Coconut", "Corn", "Eggs", "Fish", "Flour", "Garlic", "Honey", "Ketchup"
    , "Lemons", "Mangos", "Milk", "Oats", "Olive oil", "Onions", "Peaches", "Peanuts", "Peas", "Pears"
    , "Pepper", "Pineapples", "Pork ribs", "Pork tenderloin", "Potatoes", "Quinua", "Rice", "Salt", "Sausage", "Seafood"
    , "Steak", "Sugar", "Tomato", "Turkey", "Zucchini");

    // Get dropdown element from DOM
    var dropdownCategory = document.getElementById("selectCategory");
   
    // Loop through the array
    for (var i = 0; i < myArrayCategories.length; ++i) {
        // Append the element to the end of Array list
        dropdownCategory[dropdownCategory.length] = new Option(myArrayCategories[i], myArrayCategories[i]);
    }
    
    var dropdownIngredients = document.getElementById("selectIngredient");
   
    // Loop through the array
    for (var i = 0; i < myArrayIngredients.length; ++i) {
        // Append the element to the end of Array list
        dropdownIngredients[dropdownIngredients.length] = new Option(myArrayIngredients[i], myArrayIngredients[i]);
    }
    
}

function add_ingredient()
{
  var x = document.getElementById("selectIngredient").value;
  if(x !='Choose a Ingredient')
    {
        if(!document.getElementById("Ingredients").value.includes(x))
        {
            if(document.getElementById("Ingredients").value !='')
            {
                document.getElementById("Ingredients").value = document.getElementById("Ingredients").value+", "+x;
            }
            else
            {
                document.getElementById("Ingredients").value = x;
            }
        }
    }
}

