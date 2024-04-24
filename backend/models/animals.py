class Animal:
  def __init__(self, edad, raza) -> None:
    self.edad = edad
    self.raza = raza

class Perro(Animal):
  def __init__(self, edad, raza) -> None:
    super().__init__(edad, raza)
    self.tipo = 'Perro'

class Gato(Animal):
  def __init__(self, edad, raza) -> None:
    super().__init__(edad, raza)
    self.tipo = 'Gato'

class Conejo(Animal):
  def __init__(self, edad, raza) -> None:
    super().__init__(edad, raza)
    self.tipo = 'Conejo'