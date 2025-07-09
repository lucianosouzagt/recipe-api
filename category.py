import uuid

class Category:
    def __init__(
           self,
           name,
           description,
           slug,
           id = "",
           is_active = False,
           image_url = "",
    ):
        self.id = id or uuid.uuid4()
        self.name = name
        self.description = description
        self.slug = slug
        self.image_url = image_url
        self.is_active = is_active

        self.validation()

    def update_category(
            self,
            name= '',
            description= '',
            slug= '',
            image_url= ''
    ):
        if name != '':
            self.name = name
            self.validation()
        
        if description != '':
            self.description = description

        if slug != '':
            self.slug = slug

        if image_url != '':
            self.image_url = image_url
        
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
        
        if not self.slug:
            raise ValueError('slug cannot be empty')

    def __str__(self):
        return f"id: {self.id}, name: {self.name}, description: {self.description}, slug: {self.slug}, is_active: {self.is_active}, image_url: {self.image_url}"
    
    def __repr__(self):
        return f"<Category id: {self.id}, name: {self.name}, description: {self.description}, slug: {self.slug}, is_active: {self.is_active}, image_url: {self.image_url}>"
    
    def __eq__(self, other):
        if not isinstance(other, Category):
            return False
        return self.id == other.id  