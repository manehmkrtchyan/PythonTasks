'''Write a program that simulates a recipe sharing platform. 
The program should have classes for recipes, users, and ratings. 
Recipes should have attributes such as title, ingredients, and instructions. 
Users should have attributes such as name and contact information, 
and a list of their favorite recipes.
Ratings should have attributes such as the recipe being rated, 
the user making the rating, and the rating score. 
The program should allow users to browse and search for recipes, 
save and share their favorite recipes, and rate and comment on recipes. 
Use inheritance to implement classes for different types of recipes 
(e.g., vegetarian, dessert) and abstract classes for recipe sharing operations.'''
from abc import ABC, abstractmethod

class User:
    def __init__(self, name, info) -> None:
        self.name = name
        self.contact = info
        self.favorites = []
        self.shared = []
        self.browsed = []
        
    def send_to_favs(self, recipe):
        if recipe in self.browsed:
            self.favorites.append(recipe)
        else:
            print('Browse the recipe at first')
    def share(self, recipe):
        if recipe in self.browsed:
            self.shared.append(recipe)
        else:
            print('Browse the recipe at first')
        
    def brouse(self, recipe):
        self.browsed.append(recipe)
        
    def search(self, title):
        #print([recipe.title for recipe in RecipeList])
        for recipe in RecipeList:
            if recipe.title == title:
                return recipe
    
class Recipe(ABC):
    def __init__(self, title, ingredients: 'list', istructions: 'list') -> None:
        self.title = title
        self.ingredients = ingredients
        self.instructions = istructions
        
    def __repr__(self):
        return str((self.title, self.ingredients, self.instructions))
    
    @abstractmethod
    def get_type(self):
        pass
    
class VegeterianRecipe(Recipe):
    def get_type(self):
        return 'Vegeterian'

class Dessert(Recipe):
    def get_type(self):
        return 'Dessert'

class Rating:
    def __init__(self, user, recipe, score) -> None:
        self.user = user
        self.recipe = recipe
        self.score = score
        
RecipeList = []
recipe = VegeterianRecipe('Pizza', ['tomato, cheese'], ['dnel duxovka'])
recipe2 = VegeterianRecipe('Pizza', ['tomato, mis'], ['dnel duxovka'])
recipe3 = VegeterianRecipe('urish ban', ['tomato, cheese'], ['dnel duxovka'])
recipe = Dessert('Paxpaxak', ['qaxcr baner'], ['dnel duxovka'])
RecipeList.append(recipe2)
RecipeList.append(recipe3)
RecipeList.append(recipe)
user1 = User('Mane', 'sciuyha')
print(user1.search('Pizza'))
#print(RecipeList)