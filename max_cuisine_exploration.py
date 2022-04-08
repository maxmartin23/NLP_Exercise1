#Max Martin III
#301117493

from apyori import apriori
from apyori import load_transactions
import json

recipes = json.load(open('recipies.json'))
cuisines = list(set(map(lambda recipe: recipe["cuisine"], recipes)))

print(f"There are {len(cuisines)} cuisines")
print(f"There are {len(recipes)} recipes")

cuisines_recipes = {}
for recipe in recipes:
  if (recipe["cuisine"] not in cuisines_recipes):
    cuisines_recipes[recipe["cuisine"]] =  [recipe["ingredients"]]
  else:
    cuisines_recipes[recipe["cuisine"]].append(recipe["ingredients"])

for cuisine_recipe in cuisines_recipes.items():
  print(f"{cuisine_recipe[0]} has {len(cuisine_recipe[1])} recipes")