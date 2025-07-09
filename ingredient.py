import uuid

class Ingredient:
    def __init__(
           self,
           name,
           category_id,
           id = "",
           is_active = False,
    ):
        self.id = id or uuid.uuid4()
        self.name = name
        self.category_id = category_id
        self.is_active = is_active

        self.validade()

    def update_ingredient(self, name= "", category_id= ""):
        if name != "":
            self.name = name
            self.validade()

        if category_id != "":
            self.category_id = category_id
    
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
    
        if not self.category_id:
            raise ValueError("category id cannot be empty")

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, category_id: {self.category_id}, is_active: {self.is_active}"
    
    def __repr__(self):
        return f"<Ingredient id: {self.id}, name: {self.name}, category_id: {self.category_id}, is_active: {self.is_active}>"
    
    def __eq__(self, other):
        if not isinstance(other, Ingredient):
            return False
        return self.id == other.id        
