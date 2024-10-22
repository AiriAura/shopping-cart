class Person():
    def give_name(self, name , lastname):
        self.name = name
        self.lastname = lastname
    
    def dates(self, rut,fecha_nacimiento, sexo):
        self.rut = rut
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo

    




geraldine = Person()
yaritza = Person()
bruno = Person ()

geraldine.give_name("geraldine", "garces")
yaritza.give_name ("yaritza", "díaz")
bruno.give_name("bruno", "araya")
bruno.dates("20.190.033-6", "18 junio 1996", "masculino")

print(geraldine.name,geraldine.lastname)
print(yaritza.name, yaritza.lastname)
print(bruno.name, bruno.lastname)

print (bruno.sexo)