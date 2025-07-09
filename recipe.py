import uuid

class Recipe:
    def __init__(
           self,
           name,
           description,
           preparation_method,
           category_id,
           id = "",
           preparation_time = "",
           portions = "",
           is_active = False,
           image_url = "",
    ):
        self.id = id or uuid.uuid4()
        self.name = name
        self.description = description
        self.preparation_method = preparation_method
        self.preparation_time = preparation_time
        self.portions = portions
        self.category_id = category_id
        self.image_url = image_url
        self.is_active = is_active

        self.validation()

    def update_recipe(
            self, 
            name = "", 
            description = "", 
            preparation_method = "", 
            preparation_time= "", 
            portions= "",
            category_id = ""
    ):

        if name != "":
            self.name = name
            self.validation()

        if description != "":
            self.description = description

        if preparation_method != "":
            self.preparation_method = preparation_method

        if preparation_time != "":
            self.preparation_time = preparation_time

        if portions != "":
            self.portions = portions
        
        if category_id != "":
            self.category_id = category_id

    def activate(self):
        self.is_active = True
        self.validation()

    def deactivate(self):
        self.is_active = False
        self.validation()

    def validation(self):
        if len(self.name) > 255:
            raise ValueError("name cannot be longer then 255 characters")
        
        if not self.name:
            raise ValueError("name cannot be empty")
        
        if not self.description:
            raise ValueError("description cannot be empty")
        
        if not self.preparation_method:
            raise ValueError("preparation method cannot be empty")
        
        if not self.category_id:
            raise ValueError("category id cannot be empty")

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, description: {self.description}, preparation_method: {self.preparation_method}, preparation_time: {self.preparation_time}, portions: {self.portions}, category_id: {self.category_id}, is_active: {self.is_active}, image_url: {self.image_url}"
    
    def __repr__(self):
        return f"<Recipe id: {self.id}, name: {self.name}, description: {self.description}, preparation_method: {self.preparation_method}, preparation_time: {self.preparation_time}, portions: {self.portions}, category_id: {self.category_id}, is_active: {self.is_active}, image_url: {self.image_url}>"
    
    def __eq__(self, other):
        if not isinstance(other, Recipe):
            return False
        return self.id == other.id        