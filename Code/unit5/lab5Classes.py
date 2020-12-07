class pet():
    def __init__(self, type, name, breed):
        self.type = type
        self.name = name
        self.breed = breed
        self.petType = 'cage free pet'

    def whatIsIt(self):
        print(self.type + ' ' + self.name + ' ' + self.breed + ' is a ' + self.petType)

class cage():
    def __init__(self, type, danger):
        self.type = type
        self.danger = danger
        self.petType = 'caged pet'

    def whatDanger(self):
        if self.danger:
            print('danger')
        else:
            print('not danger')