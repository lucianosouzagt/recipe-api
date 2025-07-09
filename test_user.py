import pytest
from uuid import UUID
import uuid

from user import User


class TestUser:
    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            User(username='teste01', email='test@gmail.com', password='senha123', password_confirm='ValidPass1$')

    def test_name_must_have_less_than_255_characters(self):
        with pytest.raises(ValueError, match="name cannot be longer then 255 characters"):
            User(name='a'*256 , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')

    def test_user_must_be_created_with_id_as_uuid(self):
        user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')
        assert isinstance(user.id, UUID)

    def test_user_must_be_created_with_is_active_as_true(self):
        user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', is_active=True)
        assert user.is_active is True

    def test_created_user_with_default_values(self):
        user_id= uuid.uuid4()
        user_salt= uuid.uuid4()

        user = User(id= user_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', salt= user_salt, is_active=True)
        assert user.id == user_id
        assert user.name == 'test001'        
        assert user.username == 'teste01'
        assert user.email == 'test@gmail.com'
        assert user.password == 'ValidPass1$'
        assert user.is_active is True
        assert user.salt == user_salt

    def test_created_user_with_name_empty_value(self):
        with pytest.raises(ValueError, match="name cannot be empty"):
            User(name="" , username="teste01", email="test@gmail.com", password="ValidPass1$", password_confirm='ValidPass1$')
     
    def test_created_user_with_username_empty_value(self):
        with pytest.raises(ValueError, match="username cannot be empty"):
            User(name="teste01" ,username="",  email="test@gmail.com", password="ValidPass1$", password_confirm='ValidPass1$')
    
    def test_created_user_with_email_empty_value(self):
        with pytest.raises(ValueError, match="email cannot be empty"):
            User(name="teste01" , username="teste01", email="", password="ValidPass1$", password_confirm='ValidPass1$')
    
    def test_created_user_with_password_empty_value(self):
        with pytest.raises(ValueError, match="password cannot be empty"):
            User(name="teste01" , username="teste01", email="test@gmail.com", password="", password_confirm='ValidPass1$')

    def test_created_user_with_password_and_password_confirmation_different(self):
        with pytest.raises(ValueError, match="password and password confirmation are different"):
            User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1')

    def test_password_too_short(self):
        with pytest.raises(ValueError, match="password with at least 8 characters"):
            User(name="teste01" , username="teste01", email="test@gmail.com", password="Ab1$", password_confirm='ValidPass1$')

    def test_password_missing_uppercase(self):
        with pytest.raises(ValueError, match="password with at least one uppercase letter"):
            User(name="teste01" , username="teste01", email="test@gmail.com", password="validpass1$", password_confirm='validpass1$')

    def test_password_missing_number(self):
        with pytest.raises(ValueError, match="password with at least one number"):
            User(name="teste01" , username="teste01", email="test@gmail.com", password="ValidPass$", password_confirm='ValidPass$')

    def test_password_missing_special_character(self):
        with pytest.raises(ValueError, match="password with at least one special character"):
            User(name="teste01" , username="teste01", email="test@gmail.com", password="ValidPass1", password_confirm='ValidPass1')

    def test_valid_password(self):
        user = User(name="teste01" , username="teste01", email="test@gmail.com", password="ValidPass1$", password_confirm='ValidPass1$')
        assert user.password == "ValidPass1$"    
        
    def test_use_func__str__(self):
        user_id= uuid.uuid4()
        user_salt= uuid.uuid4()

        user = User(id= user_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', salt= user_salt, is_active= True)
        res = str(user)
        test = f"id: {user_id}, name: test001, username: teste01, email: test@gmail.com, password: ValidPass1$, salt: {user_salt}, is_active: True"
        print(res)
        print(test)
        assert res == test
    
    def test_use_func__repr__(self):
        user_id= uuid.uuid4()
        user_salt= uuid.uuid4()

        user = User(id= user_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', salt= user_salt, is_active= True)
        res = repr(user)
        test = f"<User id: {user_id}, name: test001, username: teste01, email: test@gmail.com, password: ValidPass1$, salt: {user_salt}, is_active: True>"
        assert res == test

class TestUpdateUser:
    def test_update_user_with_name_and_username_and_email(self):
        user_id= uuid.uuid4()
        user_salt= uuid.uuid4()

        user = User(id= user_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', salt= user_salt, is_active=True)
        user.update_user(name="nome_alterado", username="username_alterado", email="email@alterado")

        assert user.name == "nome_alterado"
        assert user.username == "username_alterado"
        assert user.email == "email@alterado"

    def test_update_user_with_name(self):
        user_id= uuid.uuid4()
        user_salt= uuid.uuid4()

        user = User(id= user_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', salt= user_salt, is_active=True)
        user.update_user(name="nome_alterado")

        assert user.name == "nome_alterado"
        assert user.username == "teste01"
        assert user.email == "test@gmail.com"

    def test_update_user_with_name_raises_exception(self):
        user = User(name='teste001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')

        with pytest.raises(ValueError, match="name cannot be longer then 255 characters"):
            user.update_user(name='a'*256)

    def test_update_user_with_username(self):
        user_id= uuid.uuid4()
        user_salt= uuid.uuid4()

        user = User(id= user_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', salt= user_salt, is_active=True)
        user.update_user(username="username_alterado")

        assert user.name == "test001"
        assert user.username == "username_alterado"
        assert user.email == "test@gmail.com"

    def test_update_user_with_email(self):
        user_id= uuid.uuid4()
        user_salt= uuid.uuid4()

        user = User(id= user_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', salt= user_salt, is_active=True)
        user.update_user(email="email@alterado")

        assert user.name == "test001"
        assert user.username == "teste01"
        assert user.email == "email@alterado"

class TestChangePassword:
    def test_change_password_with_password_too_short(self):
        with pytest.raises(ValueError, match="password with at least 8 characters"):
            user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')
            user.change_password(password='VdPas1$', password_confirm='VdPas1$')
            
    def test_password_with_password_missing_uppercase(self):
        with pytest.raises(ValueError, match="password with at least one uppercase letter"):
            user = User(name="teste01" , username="teste01", email="test@gmail.com", password='ValidPass1$', password_confirm='ValidPass1$')
            user.change_password(password="validpass1$", password_confirm='validpass1$')

    def test_password_with_password_missing_number(self):
        with pytest.raises(ValueError, match="password with at least one number"):
            user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')
            user.change_password(password="ValidPass$", password_confirm='ValidPass$')

    def test_password_with_password_missing_special_character(self):
        with pytest.raises(ValueError, match="password with at least one special character"):
            user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')
            user.change_password(password="ValidPass1", password_confirm='ValidPass1')

    def test_password_with_password_and_password_confirmation_different(self):
        with pytest.raises(ValueError, match="password and password confirmation are different"):
            user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')
            user.change_password(password="ValidPass", password_confirm='ValidPass1')

class TestActivate:
    def test_activate_inactive_user(self):
        user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')
        assert user.is_active is False
        user.activate()
        assert user.is_active is True    

    def test_activate_active_user(self):
        user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', is_active=True)
        assert user.is_active is True
        user.activate()
        assert user.is_active is True   

class TestDeactivate:
    def test_deactivate_inactive_user(self):
        user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$')
        assert user.is_active is False
        user.deactivate()
        assert user.is_active is False   

    def test_deactivate_active_user(self):
        user = User(name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', is_active=True)
        assert user.is_active is True
        user.deactivate()
        assert user.is_active is False

class TestEquality:
    def test_when_users_have_same_id_they_are_equal(self):
        common_id = uuid.uuid4()
        user_1 = User(id=common_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', is_active=True)
        user_2 = User(id=common_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', is_active=True)
        
        assert user_1 == user_2

    def test_equality_different_classes(self):
        class Dummy:
            pass

        common_id = uuid.uuid4()
        user = User(id=common_id, name='test001' , username='teste01', email='test@gmail.com', password='ValidPass1$', password_confirm='ValidPass1$', is_active=True)
        dummy = Dummy()
        dummy.id = common_id

        assert user != dummy