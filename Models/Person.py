class Person():
    def __init__(self):
        self.gender = None
        self.salutation = None
        self.titles = []
        self.prename = None
        self.name = None
        self.name_extra = None

    def __str__(self):
        return '{gender=' + str(self.gender) + ';address=' + str(self.salutation) + ';titles=[' + ', '.join(self.titles) + '];prename=' + str(self.prename) + ';name=' + str(self.name) + ';name_extra=' + str(self.name_extra) + '}'
