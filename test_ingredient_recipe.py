import pytest
from uuid import UUID
import uuid

from ingredient_recipe import IngredientRecipe

class TestIngredientRecipe:
    def test_recipe_is_required(self):
        ingredient_recipe_id= uuid.uuid4()
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'recipe_id'"):
            IngredientRecipe(ingredient_id= ingredient_recipe_id)

    def test_ingredient_is_required(self):
        ingredient_recipe_id= uuid.uuid4()
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'ingredient_id'"):
            IngredientRecipe(recipe_id= ingredient_recipe_id)

    def test_created_ingredient_recipe_with_recipe_id_empty_value(self):
        ingredient_recipe_id= uuid.uuid4()
        with pytest.raises(ValueError, match="recipe id cannot be empty"):
            IngredientRecipe(recipe_id= '', ingredient_id= ingredient_recipe_id)

    def test_created_ingredient_recipe_with_ingredient_id_empty_value(self):
        ingredient_recipe_id= uuid.uuid4()
        with pytest.raises(ValueError, match="ingredient id cannot be empty"):
            IngredientRecipe(recipe_id= ingredient_recipe_id, ingredient_id= '')

class TestUpdateIngredientRecipe:
    def test_update_ingredient_recipe_with_ingredient_id_and_recipe_id(self):
        recipe_ingredient_id= uuid.uuid4()
        recipe_ingredient_id_alterado= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredient_recipe_id_alterado= uuid.uuid4()
        ingredientRecipe = IngredientRecipe(recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id)        
        ingredientRecipe.update_ingredient_recipe(recipe_id= recipe_ingredient_id_alterado, ingredient_id= ingredient_recipe_id_alterado)
        assert ingredientRecipe.recipe_id == recipe_ingredient_id_alterado
        assert ingredientRecipe.ingredient_id == ingredient_recipe_id_alterado

    def test_update_ingredient_recipe_with_recipe_id(self):
        recipe_ingredient_id= uuid.uuid4()
        recipe_ingredient_id_alterado= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredientRecipe = IngredientRecipe(recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id)        
        ingredientRecipe.update_ingredient_recipe(recipe_id= recipe_ingredient_id_alterado)
        assert ingredientRecipe.recipe_id == recipe_ingredient_id_alterado
        
    def test_update_ingredient_recipe_with_ingredient_id(self):
        recipe_ingredient_id= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredient_recipe_id_alterado= uuid.uuid4()
        ingredientRecipe = IngredientRecipe(recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id)        
        ingredientRecipe.update_ingredient_recipe(ingredient_id= ingredient_recipe_id_alterado)

        assert ingredientRecipe.ingredient_id == ingredient_recipe_id_alterado

class TestActivate:
    def test_activate_inactive_ingredient_recipe(self):    
        recipe_ingredient_id= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredientRecipe = IngredientRecipe(recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id, is_active= False)        

        assert ingredientRecipe.is_active is False
        ingredientRecipe.activate()
        assert ingredientRecipe.is_active is True

    def test_activate_active_ingredient_recipe(self):    
        recipe_ingredient_id= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredientRecipe = IngredientRecipe(recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id, is_active= True)        

        assert ingredientRecipe.is_active is True
        ingredientRecipe.activate()
        assert ingredientRecipe.is_active is True

class TestDeactivate:
    def test_deactive_inactive_ingredient_recipe(self):
        recipe_ingredient_id= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredientRecipe = IngredientRecipe(recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id, is_active= False)        

        assert ingredientRecipe.is_active is False
        ingredientRecipe.deactivate()
        assert ingredientRecipe.is_active is False

    def test_deactive_active_ingredient_recipe(self):
        recipe_ingredient_id= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredientRecipe = IngredientRecipe(recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id, is_active= True)        

        assert ingredientRecipe.is_active is True
        ingredientRecipe.deactivate()
        assert ingredientRecipe.is_active is False
class TestEquality:
    def test_when_ingredient_recipe_have_same_id_they_are_equal(self):
        common_id= uuid.uuid4()
        recipe_ingredient_id= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredientRecipe_1 = IngredientRecipe(id= common_id, recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id)
        ingredientRecipe_2 = IngredientRecipe(id=common_id, recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id)

        assert ingredientRecipe_1 == ingredientRecipe_2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id= uuid.uuid4()
        recipe_ingredient_id= uuid.uuid4()
        ingredient_recipe_id= uuid.uuid4()
        ingredientRecipe = IngredientRecipe(id= common_id, recipe_id= recipe_ingredient_id, ingredient_id= ingredient_recipe_id)

        dummy = Dummy()
        dummy.id = common_id

        assert ingredientRecipe != dummy