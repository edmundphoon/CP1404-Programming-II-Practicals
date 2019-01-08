"""CP1404/CP5632 Practical - Client code to use the Guitars! class."""
# Note that the import has a folder (module) in it.

class Guitar:

    def __init__(self, name='', year=0, cost=0):
        """Initialise a Guitar instance.
                """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        print("{} ({}) : ${:,.2f}".format(self.name,self.year,self.cost))

    def get_age(self):
        age_of_guitar = 2017 - self.year
        return age_of_guitar

    def is_vintage(self):
        if self.get_age() >= 50:
            return True
        else:
            return False