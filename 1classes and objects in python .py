class person:
    name = "Asif" 
    occupation = "Data Scientist"
    networth = 1000000
    def info(self):
        print("Name: ", self.name)
        print("Occupation: ", self.occupation)
        print("Networth: ", self.networth)

    
a = person()
b = person()
c= person()
a.name =  "Khalid"
a.occupation = "Data Scientist"
a.networth = 1000000
b.name = "Rahim"
b.occupation = "Data Engineer"
b.networth = 10000000
c.name = "Karim"
c.occupation = "Data Analyst"
c.networth = 100000000
a.info()
b.info()
c.info()

# self is a pointer that points to the current object for a given method.