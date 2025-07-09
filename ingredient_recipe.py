import uuid

class IngredientRecipe:
    def __init__(
           self,
           recipe_id,
           ingredient_id,
           id = "",
           is_active = False,

    ):
        self.id = id or uuid.uuid4()
        self.recipe_id = recipe_id
        self.ingredient_id = ingredient_id
        self.is_active = is_active

        self.validation()
    def update_ingredient_recipe(self, recipe_id= "", ingredient_id= ""):
        if recipe_id != "":
            self.recipe_id = recipe_id

        if ingredient_id != "":
            self.ingredient_id = ingredient_id

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

    def validation(self):
        if not self.recipe_id:
            raise ValueError('recipe id cannot be empty')
        
        if not self.ingredient_id:
            raise ValueError('ingredient id cannot be empty')
        
    def __str__(self):
        return f"id: {self.id}, recipe_id: {self.recipe_id}, ingredient_id: {self.ingredient_id}, is_active: {self.is_active}"
    
    def __repr__(self):
        return f"<IngredientRecipe id: {self.id}, recipe_id: {self.recipe_id}, ingredient_id: {self.ingredient_id}, is_active: {self.is_active}>"
    
    def __eq__(self, other):
        if not isinstance(other, IngredientRecipe):
            return False
        return self.id == other.id        
