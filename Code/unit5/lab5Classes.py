#Matthew Vandeberg
#Python
#Period 2

class pet():
    #List out and assign the pet class's parameters and attributes 
    def __init__(self, type, name, breed):
        self.type = type
        self.name = name
        self.breed = breed
        self.petType = 'cage free pet'

    #Function for pet objects to print out all of their attributes
    def whatIsIt(self):
        print(self.type + ' ' + self.name + ' (' + self.breed + ') is a ' + self.petType)

class cage():
    #List out and assign the cage class's parameters and attributes
    def __init__(self, type, danger):
        self.type = type
        self.danger = danger
        self.petType = 'caged pet'

    #Function for cage objects to print out the danger of the caged pet
    def whatDanger(self):
        if self.danger:
            print('this pet is dangerous')
        else:
            print('this pet is not dangerous')


class pet1():
    def __init__(self, color, name, hair):
        self.type = 'house pet'
        self.color = color
        self.name = name
        self.hair = hair

    def activity(self):
        return self.type + ' that walks on 4 legs'

class dog(pet1):
    def __init__(self, color, name, hair):
        pet1.__init__(self, color, name, hair)
        self.noise = 'barks'

    def activity(self):
        return self.type + ' that walks on 4 legs and ' + self.noise

class cat(pet1):
    def __init__(self, color, name, hair):
        pet1.__init__(self, color, name, hair)
        self.skill = 'hunts mice'

    def activity(self):
        return self.type + ' that walks on 4 legs and ' + self.skill