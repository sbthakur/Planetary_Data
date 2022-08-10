from Planet import *
from Operator import *

def run_test():
    tmp=[
        Planet('A',[],2,'No'),
        Planet('B',['X','Y'],35,'Yes'),
        Planet('C',['Y','Z'],1,'Yes')
    ]

    tmp_driver=Operator(tmp)

    assert tmp_driver.count_moons_with_rings()==36

    assert tmp_driver.gas_max_planets()==[('Y',2)]

    print('All test case passed.')


if __name__ == '__main__':
    run_test()
