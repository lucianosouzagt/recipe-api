import pytest
from uuid import UUID
import uuid

from ingredient import Ingredient

class TestIngredient:
    def test_name_is_requared(self):
        ingredient_category_id= uuid.uuid4()
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Ingredient(category_id= ingredient_category_id)
    
    def test_category_is_requared(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'category_id'"):
            Ingredient(name= 'ingredient_test')

    def test_created_ingredient_with_name_empty_value(self):
        ingredient_category_id= uuid.uuid4()
        with pytest.raises(ValueError, match="name cannot be empty"):
            Ingredient(name= '', category_id= ingredient_category_id)

    def test_created_ingredient_with_category_empty_value(self):
        with pytest.raises(ValueError, match="category id cannot be empty"):
            Ingredient(name= 'ingredient_test', category_id= '')

    def test_ingredient_must_be_created_with_id_as_uuid(self):
        ingredient_category_id= uuid.uuid4()
        ingredient_id= uuid.uuid4()
        ingredient= Ingredient(id= ingredient_id, name= 'ingredient_test', category_id= ingredient_category_id)
        
        assert isinstance(ingredient.id, UUID)
        assert ingredient.id == ingredient_id

class TestUpdateIngredient:
    def test_update_ingredient_with_name_and_category_id(self):
        ingredient_id= uuid.uuid4()
        ingredient_category_id= uuid.uuid4()
        ingredient_category_id_alterada= uuid.uuid4()
        ingredient= Ingredient(id= ingredient_id, name= 'nome_test', category_id= ingredient_category_id)
        ingredient.update_ingredient(name= 'nome_alterado', category_id= ingredient_category_id_alterada)
        assert ingredient.name == 'nome_alterado'
        assert ingredient.category_id == ingredient_category_id_alterada

    def test_update_ingredient_with_name (self):
        ingredient_id= uuid.uuid4()
        ingredient_category_id= uuid.uuid4()
        ingredient= Ingredient(id= ingredient_id, name= 'nome_test', category_id= ingredient_category_id)
        ingredient.update_ingredient(name= 'nome_alterado')
        assert ingredient.name == 'nome_alterado'

    def test_update_ingredient_with_category_id(self):
        ingredient_id= uuid.uuid4()
        ingredient_category_id= uuid.uuid4()
        ingredient_category_id_alterada= uuid.uuid4()
        ingredient= Ingredient(id= ingredient_id, name= 'nome_test', category_id= ingredient_category_id)
        ingredient.update_ingredient(category_id= ingredient_category_id_alterada)
        assert ingredient.category_id == ingredient_category_id_alterada

class TestActivate:
    def test_activate_inactive_ingredient(self):
        ingredient_category_id= uuid.uuid4()
        ingredient= Ingredient(name= 'nome_test', category_id= ingredient_category_id)
        assert ingredient.is_active is False
        ingredient.activate()
        assert ingredient.is_active is True
 
    def test_activate_active_ingredient(self):
        ingredient_category_id= uuid.uuid4()
        ingredient= Ingredient(name= 'nome_test', category_id= ingredient_category_id, is_active= True)
        assert ingredient.is_active is True
        ingredient.activate()
        assert ingredient.is_active is True

class TestDeactivate:
    def test_deactivate_inactive_ingredient(self):
        ingredient_category_id= uuid.uuid4()
        ingredient= Ingredient(name= 'nome_test', category_id= ingredient_category_id)
        assert ingredient.is_active is False
        ingredient.deactivate()
        assert ingredient.is_active is False
 
    def test_deactivate_active_ingredient(self):
        ingredient_category_id= uuid.uuid4()
        ingredient= Ingredient(name= 'nome_test', category_id= ingredient_category_id, is_active= True)
        assert ingredient.is_active is True
        ingredient.deactivate()
        assert ingredient.is_active is False

class TestEquality:
    def test_when_ingredients_have_same_id_they_are_equal(self):
        common_id= uuid.uuid4()
        common_category_id= uuid.uuid4()
        ingredient_1= Ingredient(id= common_id, name= 'test_name', category_id= common_category_id)
        ingredient_2= Ingredient(id= common_id, name= 'test_name', category_id= common_category_id)

        assert ingredient_1 == ingredient_2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id= uuid.uuid4()
        common_category_id= uuid.uuid4()
        ingredient= Ingredient(id= common_id, name= 'test_name', category_id= common_category_id)
        dummy= Dummy()
        dummy.id = common_id
        assert ingredient != dummy
        
