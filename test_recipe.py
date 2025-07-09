import pytest
from uuid import UUID
import uuid

from recipe import Recipe


class TestRecipe:
    def test_name_is_required(self):
        recipe_category_id= uuid.uuid4()
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Recipe(description='teste01', preparation_method='teste_method', preparation_time='30m', portions= '4', category_id= recipe_category_id)
    
    def test_name_must_have_less_than_255_characters(self):
        recipe_category_id= uuid.uuid4()
        with pytest.raises(ValueError, match="name cannot be longer then 255 characters"):
            Recipe(name= 'a'*256, description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id)
    
    def test_recipe_must_be_created_with_id_as_uuid(self):
        recipe_category_id= uuid.uuid4()
        recipe = Recipe(name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id)
        assert isinstance(recipe.id, UUID)

    def test_recipe_must_be_created_with_is_active_as_true(self):
        recipe_category_id= uuid.uuid4()
        recipe = Recipe(name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True)
        assert recipe.is_active is True

    def test_created_recipe_with_default_values(self):
        recipe_id = uuid.uuid4()
        recipe_category_id = uuid.uuid4()

        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id)
        assert recipe.id == recipe_id
        assert recipe.name == 'teste01'
        assert recipe.preparation_method == 'teste_method'
        assert recipe.preparation_time == '30m'
        assert recipe.portions == '4'
        assert recipe.category_id == recipe_category_id        
        assert recipe.is_active is False

    def test_created_recipe_with_name_empty_value(self):
        recipe_category_id = uuid.uuid4()
        with pytest.raises(ValueError, match="name cannot be empty"):
            Recipe(name= '', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id)

    def test_created_recipe_with_description_empty_value(self):
        recipe_category_id = uuid.uuid4()
        with pytest.raises(ValueError, match="description cannot be empty"):
            Recipe(name= 'teste01', description= '', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id)

    def test_created_recipe_with_preparation_method_empty_value(self):
        recipe_category_id = uuid.uuid4()
        with pytest.raises(ValueError, match="preparation method cannot be empty"):
            Recipe(name= 'teste01', description= 'teste01', preparation_method= '', preparation_time= '30m', portions= '4', category_id= recipe_category_id)

    def test_created_recipe_with_category_id_empty_value(self):
        with pytest.raises(ValueError, match="category id cannot be empty"):
            Recipe(name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= '')

    def test_use_func__str__(self):
        recipe_id= uuid.uuid4()
        recipe_category_id= uuid.uuid4()

        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        res = str(recipe)
        test = f"id: {recipe_id}, name: teste01, description: teste01, preparation_method: teste_method, preparation_time: 30m, portions: 4, category_id: {recipe_category_id}, is_active: True, image_url: https://localhost:8000/image/001.jpg"
        print(res)
        print(test)
        assert res == test
    
    def test_use_func__repr__(self):
        recipe_id= uuid.uuid4()
        recipe_category_id= uuid.uuid4()

        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        res = repr(recipe)
        test = f"<Recipe id: {recipe_id}, name: teste01, description: teste01, preparation_method: teste_method, preparation_time: 30m, portions: 4, category_id: {recipe_category_id}, is_active: True, image_url: https://localhost:8000/image/001.jpg>"
        print(res)
        print(test)
        assert res == test

class TestUpdateRecipe:
    def test_update_recipe_with_name_and_description_and_preparation_method_and_preparation_time_and_portions_and_category_id(self):
        recipe_id= uuid.uuid4()
        recipe_category_id= uuid.uuid4()
        recipe_category_id_alterada= uuid.uuid4()
        recipe= Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        recipe.update_recipe(name="nome_alterado", description= 'description_alterada', preparation_method= 'method_alterado', preparation_time= '45m', portions= '2', category_id= recipe_category_id_alterada)

        assert recipe.name == "nome_alterado"
        assert recipe.description == "description_alterada"
        assert recipe.preparation_method == "method_alterado"
        assert recipe.preparation_time == "45m"
        assert recipe.category_id == recipe_category_id_alterada

    def test_update_recipe_with_name(self):
        recipe_id = uuid.uuid4()
        recipe_category_id = uuid.uuid4()
        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        recipe.update_recipe(name="nome_alterado")

        assert recipe.name == "nome_alterado"

    def test_update_recipe_with_description(self):
        recipe_id = uuid.uuid4()
        recipe_category_id = uuid.uuid4()
        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        recipe.update_recipe(description= 'description_alterada')

        assert recipe.description == "description_alterada"

    def test_update_recipe_with_preparation_method(self):
        recipe_id = uuid.uuid4()
        recipe_category_id = uuid.uuid4()
        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        recipe.update_recipe(preparation_method= 'method_alterado')

        assert recipe.preparation_method == "method_alterado"

    def test_update_recipe_with_preparation_time(self):
        recipe_id = uuid.uuid4()
        recipe_category_id = uuid.uuid4()
        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        recipe.update_recipe(preparation_time= '45m')

        assert recipe.preparation_time == "45m"

    def test_update_recipe_with_portions(self):
        recipe_id = uuid.uuid4()
        recipe_category_id = uuid.uuid4()
        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        recipe.update_recipe(portions= '2')

        assert recipe.portions == "2"

    def test__update_recipe_with_category(self):
        recipe_id = uuid.uuid4()
        recipe_category_id = uuid.uuid4()
        recipe_category_id_alterada = uuid.uuid4()
        recipe = Recipe(id= recipe_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True, image_url= 'https://localhost:8000/image/001.jpg')
        recipe.update_recipe(category_id= recipe_category_id_alterada)

        assert recipe.category_id == recipe_category_id_alterada

class TestActivate:
    def test_activate_inactive_recipe(self):
        recipe_category_id= uuid.uuid4()
        recipe = Recipe(name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id)
        assert recipe.is_active is False
        recipe.activate()
        assert recipe.is_active is True
    
    def test_activate_active_recipe(self):
        recipe_category_id= uuid.uuid4()
        recipe = Recipe(name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True)
        assert recipe.is_active is True
        recipe.activate()
        assert recipe.is_active is True        

class TestDeactivate:
    def test_deactivate_incative_recipe(self):
        recipe_category_id= uuid.uuid4()
        recipe = Recipe(name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id)
        assert recipe.is_active is False
        recipe.deactivate()
        assert recipe.is_active is False 

    def test_deactivate_active_recipe(self):
        recipe_category_id= uuid.uuid4()
        recipe = Recipe(name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= recipe_category_id, is_active= True)
        assert recipe.is_active is True
        recipe.deactivate()
        assert recipe.is_active is False 

class TestEquality:
    def test_when_recipes_have_same_id_they_are_equal(self):
        common_id = uuid.uuid4()
        common_category_id = uuid.uuid4()
        recipe_1 = Recipe(id= common_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= common_category_id, is_active= True)
        recipe_2 = Recipe(id= common_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= common_category_id, is_active= True)
        
        assert recipe_1 == recipe_2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id = uuid.uuid4()
        common_category_id = uuid.uuid4()
        recipe = Recipe(id= common_id, name= 'teste01', description= 'teste01', preparation_method= 'teste_method', preparation_time= '30m', portions= '4', category_id= common_category_id, is_active= True)
        dummy = Dummy()
        dummy.id = common_id

        assert recipe != dummy