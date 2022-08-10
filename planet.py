class planet:
    def __init__(self, name, surface_gasses, number_of_moons, rings):
        self.name = name
        self.surface_gasses = surface_gasses
        self.number_of_moons = number_of_moons
        self.rings = rings



p1 = planet("Mercury", 0, 0, "No")
p2 = planet("Venus", "Carbon Dioxide, Nitrogen", 0, "No")
p3 = planet("Earth", "Nitrogen, Oxygen", 1, "No")
p4 = planet("Jupiter", "Hydrogen, Helium", 79, "Yes")
p5 = planet("Saturn", "Hydrogen, Helium", 83, "Yes")
p6 = planet("Uranus", "Hydrogen, Helium, Methane", 27, "Yes")
Planets=[p1,p2,p3,p4,p5,p6]
count1=0

def count_moons(self):
  for i in Planets:
      if self.rings=="Yes":
        count1=Self.number_of_moons++;
        print(count1);

count_moons();