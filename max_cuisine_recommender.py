#Max Martin III
#301117493

from apyori import apriori
from apyori import load_transactions
import json

recipes = json.load(open('recipies.json'))
cuisines = list(set(map(lambda recipe: recipe["cuisine"], recipes)))

cuisines_ingredients = {}
cuisines_association_rules = {}
cuisine_result_lists = {}

for recipe in recipes:
  if (recipe["cuisine"] not in cuisines_ingredients):
    cuisines_ingredients[recipe["cuisine"]] =  [recipe["ingredients"]]
  else: 
    cuisines_ingredients[recipe["cuisine"]].append(recipe["ingredients"])

for cuisine in cuisines:
  cuisines_association_rules[cuisine] =  apriori(cuisines_ingredients[cuisine], min_support=100/len(cuisines_ingredients[cuisine]), min_confidence=0.05)
  cuisine_result_lists[cuisine] = {}

  for item in cuisines_association_rules[cuisine]:
    if len(item[0]) < 2: continue
    for k in item[2]:
      baseItemList = list(k[0])
      if not baseItemList: continue
      baseItemList.sort()
      baseItemList_key = tuple(baseItemList)
      if baseItemList_key not in cuisine_result_lists[cuisine].keys():
          cuisine_result_lists[cuisine][baseItemList_key] = []
      cuisine_result_lists[cuisine][baseItemList_key].append((list(k[1]), k[3]))
  for ruleList in cuisine_result_lists[cuisine]:
      cuisine_result_lists[cuisine][ruleList].sort(key=lambda x: x[1], reverse=True)



is_continue = True
while (is_continue):
  cuisine = input("Enter cuisine (or type 'exit' to quit): ")
  if (cuisine not in cuisines):
    print("Invalid cuisine")
    continue
  if (cuisine == "exit"):
    is_continue = False
    print("Thank you for using our recipe recommender")
    continue
 
  top_item = None
  high_lift_items = []
  for item in cuisine_result_lists[cuisine].items():
                
    ingredient_group = item[1][0][0]
    lift = item[1][0][1]
    if (top_item is None):
      top_item = (ingredient_group, lift)
    if (lift > 2):
      high_lift_items.append((ingredient_group, lift))
  print(f"Top ingredient group for {cuisine} is {ingredient_group} with lift {lift}")
  for item in high_lift_items:
    print(f"We also recommend {item[0]} with lift {item[1]}")