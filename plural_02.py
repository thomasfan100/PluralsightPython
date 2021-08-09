#import plural_01
from plural_02_definitions import *
from pprint import pprint as pp

def main():
    #basic functions
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
    #closures and decorators
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
    
    tc0 = TestContainer("YML","coffee")
    tc1 = TestContainer.create_empty("BBK")
    print(tc1.bic)

    cc0 = ChildContainer("BIO","chemical", celsius= 2.0)
    print(cc0.bic)
    cc0.celsius = 1.0
    print(cc0.celsius)
    '''
    #strings and representations
    '''
    sr = StringRepresentation(x= 42, y=69)
    print(str(sr))
    print(sr)
    print(repr(sr))
    #!r forces the use of __repr__ and !s forces the use of __str__. Often you don't need to use __format__
    print('{:r}'.format(StringRepresentation(1,2)))
    '''
    #numeric and scaler types
    #testingNumbers()

    #iterables and iteration
    '''
    advanced_iteration()
    for i in ExampleIterable():
        print(i)
    for i in AlternateIterable():
        print(i)
    '''

    #inheritance and polymorphism
    #method resolution order MRO = the class order it will look down to find a function
    print("MRO:      ",SortedIntList.__mro__) #.mro() returns a list
    print("BASES:    ",SortedIntList.__bases__) #tuple of base classes without the class itself
    
    pp(SortedIntList.mro())
    '''
    sil = SortedIntList()
    sil.add(6)
    ^^^ will use add of IntList(). The super() in that add method will refer not
    to SimpleList which it derives but to SortedList which is next in SortedIntList.mro
    ''' 
    sil = SortedIntList([5,15,10])
    super(SortedList,sil).add(6)
    print(sil)
    super(SortedList,sil).add('non-number type')
    print(sil)
    
if __name__ == "__main__":
    main()