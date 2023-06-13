class person:
    def __init__(self, naam, occ, networ):   # constructor method (dunder init)
        self.name = naam
        self.occupation = occ
        self.networth = networ

    def info(self):
        print("Name: ", self.name)
        print("Occupation: ", self.occupation)
        print("Networth: ", self.networth)

a = person("Khalid", "Data Scientist", 1000000)
b = person("Rahim", "Data Engineer", 10000000)
c = person("Karim", "Data Analyst", 100000000)
a.info()
b.info()
c.info()