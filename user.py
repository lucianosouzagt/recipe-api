import re
import uuid

class User:
    def __init__(
            self,
            name, 
            username, 
            email, 
            password,
            password_confirm, 
            id = "",             
            salt = "", 
            is_active = False, 
    ):
        self.id = id or uuid.uuid4()
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.password_confirm = password_confirm
        self.salt = salt or uuid.uuid4()
        self.is_active = is_active

        self.validade()

    def update_user(self, name= "", username = "", email= ""):
        if name != "":
            self.name = name
            self.validade()

        if username != "":
            self.username = username

        if email != "":
            self.email = email

    def change_password(self, password, password_confirm):
        self.password = password
        self.password_confirm = password_confirm
        self.validade()

    def activate(self):
        self.is_active = True
        self.validade()

    def deactivate(self):
        self.is_active = False
        self.validade()

    def validade(self):
        if len(self.name) > 255:
            raise ValueError("name cannot be longer then 255 characters")
        
        if not self.name:
            raise ValueError("name cannot be empty")
        
        if not self.username:
            raise ValueError("username cannot be empty")
        
        if not self.email:
            raise ValueError("email cannot be empty")
        
        if not self.password:
            raise ValueError("password cannot be empty")
        
        if len(self.password) < 8:
            raise ValueError("password with at least 8 characters")
        
        if self.password != self.password_confirm:
            raise ValueError("password and password confirmation are different")
        
        if not re.search(r"[A-Z]", self.password):
            raise ValueError("password with at least one uppercase letter")
        
        if not re.search(r"[0-9]", self.password):
            raise ValueError("password with at least one number")
        
        if not re.search(r"[^a-zA-Z0-9]", self.password):
            raise ValueError("password with at least one special character")
        
    def __str__(self):
        return f"id: {self.id}, name: {self.name}, username: {self.username}, email: {self.email}, password: {self.password}, salt: {self.salt}, is_active: {self.is_active}"
    
    def __repr__(self):
        return f"<User id: {self.id}, name: {self.name}, username: {self.username}, email: {self.email}, password: {self.password}, salt: {self.salt}, is_active: {self.is_active}>"
    
    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        
        return self.id == other.id        


