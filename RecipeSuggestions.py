# Define example recipes
recipes = [
    { 'Name': 'Overnight Oats', 'Ingredients': ['Oats', 'Milk', 'Protein Powder', 'Honey', 'Cinnamon']},
    { 'Name': 'Fresh Pasta', 'Ingredients': ['00 Flour', 'Eggs']},
    { 'Name': 'Rosemary Focaccia', 'Ingredients': ['Bread FLour', 'Yeast', 'Water', 'Salt', 'Rosemary', 'Olive Oil']},
    { 'Name': 'Chicken Curry', 'Ingredients': ['Chicken', 'Onion', 'Garlic', 'Ginger', 'Tomato', 'Curry Powder', 'Coconut Milk']},
    { 'Name': 'Chocolate Cake', 'Ingredients': ['Flour', 'Sugar', 'Cocoa Powder', 'Baking Powder', 'Baking Soda', 'Eggs', 'Milk', 'Oil', 'Vanilla Extract']},
]

# Get a user input
user_input = input('Enter the ingredients in your kitchen, separated by commas: ')

# Split the user input into a list
user_ingredients = user_input.split(',')

# Check for matching recipes
print('Here are some recipes you could try: ')
found = False
for recipe in recipes:
    if any(ingredient in user_ingredients for ingredient in recipe['Ingredients']):
        print(recipe['Name'])
        found = True
if not found:
    print('Sorry, no matching recipes found with those ingredients!')

