from Planet import *
from Operator import *


def main():

    D=[
        Planet('Mercury',['NIL'],0,'No'),
        Planet('Venus',['Carbon Dioxide','Nitrogen'],0,'No'),
        Planet('Earth',['Nitrogen','Oxygen'],1,'No'),
        Planet('Jupitor',['Hydrogen','Helium'],79,'Yes'),
        Planet('Saturn',['Hydrogen','Helium'],83,'Yes'),
        Planet('Uranus',['Hydrogen','Helium','Methane'],27,'Yes')
    ]

    driver=Operator(D)

    print(driver.count_moons_with_rings())

    print(driver.gas_max_planets())







if __name__ == '__main__':
    main()
