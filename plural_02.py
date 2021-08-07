#import plural_01
from plural_02_definitions import *

def main():
    ''' 
    cC = callableClass()
    cC()
    '''
    '''
    me_callable = BasicFunctions()
    me_callable(True)
    print(callable(me_callable))
    me_callable.multiple_arguments(1,2,3,4,5)
    me_callable.keyword_arguments('img', src="monet.jpg",alt = "Sunrise by Claude", border =1)
    '''
    '''
    CandD = ClosuresandDecorators()
    
    cube = CandD.localFunction(3)
    square = CandD.localFunction(2)
    print(cube(3))
    print(square(5))
    print(square.__closure__)

    CandD.enclosing()

    city_decorated()

    l = [1,2,3]
    l = rotate_list(l)
    tracer.enabled = False

    hello('Fred')
    hello('Wilma')
    '''
    tc0 = TestContainer("YML","coffee")
    tc1 = TestContainer.create_empty("BBK")
    print(tc1.bic)

    cc0 = ChildContainer("BIO","chemical", celsius= 2.0)
    print(cc0.bic)
    cc0.celsius = 1.0
    print(cc0.celsius)
    



if __name__ == "__main__":
    main()