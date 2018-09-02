#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  count = 0;
  ingredients_list = [ingredient for ingredient in ingredients.values()]
  recipe_list = [item for item in recipe.values()]
  if (len(ingredients_list) is not len(recipe_list)):
      return count

  difference = [a-b for a,b in zip(ingredients_list, recipe_list)]
  while (all(inventory_differences >= 0 for inventory_differences in difference)):
      difference = [a-b for a,b in zip(ingredients_list, recipe_list)]
      print('difference', difference)
      count += 1
      ingredients_list = difference
  return count-1


if __name__ == '__main__':
  # Change the entries of these dictionaries to test
  # your implementation with different inputs
  # recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  # ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  recipe = { 'milk': 2, 'sugar': 40, 'butter': 20 }
  ingredients = { 'milk': 5, 'sugar': 120, 'butter': 500 }

  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
