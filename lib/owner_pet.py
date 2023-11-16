class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []




    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def pet_type(self):
        return self._pet_type
    
    @pet_type.setter
    def pet_type(self, new_pet_type):
        if new_pet_type not in Pet.PET_TYPES:
            raise Exception("Not a valid pet type")
        else:
            self._pet_type = new_pet_type
        


class Owner:
    def __init__(self,name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner ==self]
    
    def add_pet(self, new_pet):
        if isinstance(new_pet, Pet):
            new_pet.owner = self
        else:
            raise Exception("NO")

    def get_sorted_pets(self):

        my_pets = self.pets()
        
        return sorted(my_pets, key = lambda each_pet: each_pet.name.lower() )
       
        

        
