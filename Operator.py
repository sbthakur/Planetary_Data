from collections import Counter


class Operator:
    def __init__(self,data):
        self.data=data
    def count_moons_with_rings(self):
        c=0
        for planet in self.data:
            if planet.rings=='Yes':
                c+=planet.num_of_moons
        return c



    def gas_max_planets(self):
        arr=[]
        for planet in self.data:
            arr.extend(planet.surface_gases)

        C=Counter(arr)

        return C.most_common(1)
