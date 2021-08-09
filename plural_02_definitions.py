import decimal
from decimal import Decimal

from fractions import Fraction

import datetime

from functools import reduce
import operator

def callableClass():
    return BasicFunctions() #returns a class object

class BasicFunctions:
    def __init__(self):
        i = 0
    def __call__(self, x = False): #define __call__ to make class instances callable
        #conditional expression
        print("ello boy... never hur somun lika you round hur") if x else print("yousa not fromaround hur")

        #lambdas
        lamb = lambda l: print(l+5+500)
        lamb(50)
        lamb2 = lambda: 5 % 2 == 1
    
        #chained comparisons
        if 1 < 2 < 3:
            print(".... 1 < 2 < 3")
    #order: arg, *args, kwarg, **kwargs
    def multiple_arguments(self,arg, *args): #*args itself doesn't handle an error call with no arguments well
        v = arg
        for item in args:
            v *= item

        if arg != -1:
            tup = (-1,4,v)
            t = self.multiple_arguments(*tup) #unpacking a tuple with *tup
                                              #unpack a dict with **dict
            print(v, "  * -4 =  ", t)
        return v
    
    def keyword_arguments(self,arg, **kwargs):
        print(arg,kwargs)

class ClosuresandDecorators:
    def localFunction(self,exp):
        def insideFunction(x):
            return pow(x,exp)
        return insideFunction

    def enclosing(self):
        #remember scope rule goes : Local -> Enclosing -> Global -> Builtin
        #classes dont introduce new scopes
        message = 'enclosing'
        def local():
            #global message will access the global variable
            #nonlocal will search from innermost to ourtermost scope for the name you give it
            nonlocal message
            message = 'local'

        print('enclosing message:',message)
        local()
        print('enclosing message:', message)      

#example method decorator
def escape_unicode(f):
    '''
    turns special characters into ascii code
    '''
    def wrap(*args,**kwargs):
        x =f(*args,**kwargs)
        return ascii(x)
    return wrap

@escape_unicode
def city_decorated():
    return 'Tromsø'

#example class instance decorator
class Trace:
    def __init__(self):
        self.enabled = True
    def __call__(self,f):
        def wrap(*args,**kwargs):
            if self.enabled:
                #prints: Calling <function escape_unicode.<locals>.wrap at blah blah blah>
                print('Calling {}'.format(f))
            return f(*args,**kwargs)
        return wrap
tracer = Trace()

@tracer #class instance as a decorator
def rotate_list(l):
    return l[1:] + [l[0]]

#example class decorator
class CallCount:
    def __init__(self,f):
        self.f = f
        self.count = 0
    def __call__(self,*args,**kwargs):
        self.count += 1
        return self.f(*args,**kwargs)
    
@CallCount
def hello(name):
    print('Hello, {}'.format(name))

#:::PROPERTIES AND CLASS METHODS:::
class TestContainer:
    example_serial = 8250

    #use static when no access is needed to either class or instance objects
    @staticmethod
    def _make_bic_code(owner_code,serial):
        return owner_code + str(serial)

    #transformed this into a class method below 
    @staticmethod
    def i_get_next_serial():
        result = TestContainer.example_serial
        TestContainer.example_serial += 1
        return result

    #use class when access to class object to call other class methods is needed
    @classmethod 
    def _get_next_serial(cls):
        result = cls.example_serial
        cls.example_serial += 1
        return result
    
    #returning a class object that is assignable to a variable
    #*args and **kwargs help __init__ in subclasses that need to pass more arguments that the base class
    @classmethod
    def create_empty(cls,owner_code, *args, **kwargs):
        return cls(owner_code,contents = None, *args, **kwargs)
    
    @classmethod
    def create_with_items(cls,owner_code,items, *args, **kwargs):
        return cls(owner_code, contents = list(items), *args, **kwargs)

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        #modifying class attributes, self._get_next_serial works as well
        #if you use self, child containers will run their own static methods
        #if you use TestContainer, child containers that __make_bic_code will use 
        #the definition from TestContainer. Try it!
        self.bic = self._make_bic_code(owner_code = owner_code,
                                serial = TestContainer._get_next_serial())

class ChildContainer(TestContainer):
    MAX_CELSIUS = 4.0 

    @staticmethod
    def _make_bic_code(owner_code, serial):
        return "You are now here my friend."
    
    @staticmethod
    def _c_to_f(celsius):
        return celsius * 9/5 + 32

    def __init__(self,owner_code, contents,celsius):
        super().__init__(owner_code,contents)
        self.celsius = celsius
    
    @property #is a getter that allows you to do something like x.celsius
    def celsius(self):
        return self._celsius

    #if overriding a setter, you must do @parentclassnamehere.celsius.setter
    @celsius.setter
    def celsius(self,value):
        if value > ChildContainer.MAX_CELSIUS:
            raise ValueError("Temperature too hot!")
        #in some cases: baseclass.celcius.fset(self,value)
        self._celsius = value

class StringRepresentation:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __str__(self): #use a str to tell a human everything they need to know
        return "({}, {})".format(self.x, self.y)
    def __repr__(self): #use a repr to tell debuggers information they need to know
        #repr also used when called in the REPR
        return 'StringRepresentation(x={}, y={})'.format(self.x,self.y)
    
    def __format__(self, f):
        if f == 'r':
            return '{}, {}'.format(self.y,self.x)
        else:
            return '{}, {}'.format(self.x,self.y)

def testingNumbers():
    print(.8 - .7)
    x = Decimal('0.8') - Decimal('0.7')
    print(x)
    x = Decimal(.8) - Decimal(.7) #base 10 are getting converted to base 2 as .8 and .7 are float objects
    print(x)
    decimal.getcontext().prec = 6
    x = Decimal('1.234567')
    print(x)
    Decimal('Infinity')
    Decimal('-Infinity')
    Decimal('NaN')

    #can perform + - * / // arithmetic on fractions.
    two_thirds = Fraction(2,3)
    print(two_thirds)
    Fraction(.5) # Fraction 1,2
    Fraction(Decimal('.1'))
    Fraction('22/7') # Fraction 22,7
 
    #complex numbers
    x = 2j #sqrt -1
    print("Complex: ", complex(-2,3))
    c = 3 + 5j
    print(c.real)
    print(c.imag)

    print(abs(-54))
    print(round(0.2812,3)) #rounds towards even numbers

    print(bin(42), oct(42), hex(42)[2:], int("acghd", base = 18)) #int base from 2-36

    #datetime
    datetime.date(year = 2014,month = 1,day = 6)
    d = datetime.date.today()
    print("Today is: ",d.year,"/",d.month,"/",d.day)
    d.strftime('%A %d %B %Y')
    print("The date is {:%A %d %B %Y}".format(d))

    datetime.time(hour =3,minute=1,second=2,microsecond=232)
    t = datetime.time(10,32,47,675623)
    print("Time HR/Min/Sec/MSec : ",t.hour,"/",t.minute,"/",t.second,"/",t.microsecond)
    print(t.strftime('%H    %M    %S'))
    print("{t.hour}h{t.minute}m{t.second}s".format(t=t))

    datetime.datetime(2003,5,12,14,33,22,245323) #year month day must be given
    dt = datetime.datetime.strptime("Monday 6 January 2014, 12:13:31", 
                                    "%A %d %B %Y, %H:%M:%S")
    print(dt)

    td = datetime.timedelta(weeks=1,minutes=2,milliseconds=5500)
    #only days seconds and microseconds are stored, the rest are summed up
    print("TimeDelta: ",td, "   Repr:", repr(td)) 
    print("TD day/sec/microsec: ",td.days,"/",td.seconds,"/",td.microseconds)
    a = datetime.datetime(year=2014,month=5,day=8,hour=14,minute=22)
    b = datetime.datetime(year=2014,month=3,day=14,hour=12,minute=9)
    d = a-b
    print(d.total_seconds())
    #arithmetic on time objects is not supported
    print(datetime.date.today() + datetime.timedelta(weeks=1) * 3)

    #utc -6
    CST = datetime.timezone(datetime.timedelta(hours=-6),"CST")

def advanced_iteration():
    #nested comprehensions
    values = [x-y
              for x in range(100)
              if x>50
              for y in range(100)
              if x-y != 0]
    two_vals = [[y*3 for y in range(x)] for x in range(10)]
    #print(two_vals)

    y = 50 #showing that y can be a variable outside of the comprehension
    me = [y+x for x in range(10)]
    #print(me)

    #mapping - lazy iterable so you have to use list or for loop to access elements
    sizes = ['small','medium','large','xtra large']
    colors = ['lavender','teal','burnt orange']
    animals = ['koala','platypus','salamander']
    def combine(size,color,animal):
        return '{} {} {}'.format(size,color,animal)
    print(list(map(combine,sizes,colors,animals)))
    #alternative way
    for x in map(combine, sizes, colors, animals):
        print(x)

    #filter: will only return the true elements
    positives = filter(lambda x: x>0, [1,-5,0,6,-2,3])
    print(list(positives))
    trues = filter(None, [0,1, False, True, [], [1,2,3]]) #removes all the false

    #reduce: repeatedly apply function to element of a sequence, reducing them to a single value
    print(reduce(operator.add,[1,2,3,4,5]))

class ExampleIterator:
    def __init__(self,data):
        self.index = 0
        self.data = data
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()

        result = self.data[self.index]
        self.index += 1
        return result

class ExampleIterable:
    def __init__(self):
        self.data = [1,2,3]
    def __iter__(self):
        return ExampleIterator(self.data)

class AlternateIterable:
    def __init__(self):
        self.data = [1,2,3]
    def __getitem__(self,index):
        return self.data[index]

#using the extended iter form iter(callable,sentinel), reads a file until the sentinel value
'''
with open('somefile.txt','rt') as f:
    for line in iter(lambda: f.readline().strip(), 'END'):
        print(line)
'''

#::::::INHERITANCE AND POLYMORPHISM::::::::

#typechecking: isinstance(456,int), issubclass(IntList,SimpleList)
#super returns a proxy object. bound =bound to specific class/instance. we will not use unbound here
'''
class bound
super(base-class, derived-class).add
take derived list MRO, find base-class in it, find first class base-class derives with a add
'''
'''
instance bound
super(class, instance-of-class)
find MRO of instance-of-class, find class in MRO, use everything after the class for resolving methods
'''
'''
super() with no arguments
instance method - super(class-of-method,self)
class method - super(class-of-method,class)
'''
class SimpleList:
    def __init__(self, items):
        self._items = list(items)

    def add(self, item):
        self._items.append(item)

    def __getitem__(self, index):
        return self._items[index]

    def sort(self):
        self._items.sort()

    def __len__(self):
        return len(self._items)

    def __repr__(self):
        return "SimpleList({!r})".format(self._items)

class SortedList(SimpleList):
    def __init__(self, items=()):
        super().__init__(items)
        self.sort()

    def add(self, item):
        super().add(item)
        self.sort()

    def __repr__(self):
        return "SortedList({!r})".format(list(self))

class IntList(SimpleList):
    def __init__(self, items=()):
        for x in items: self._validate(x)
        super().__init__(items)

    @staticmethod
    def _validate(x):
        if not isinstance(x, int):
            raise TypeError('IntList only supports integer values.')

    def add(self, item):
        self._validate(item)
        super().add(item)

    def __repr__(self):
        return "IntList({!r})".format(list(self))

class SortedIntList(IntList, SortedList):
    def __repr__(self):
        return 'SortedIntList({!r})'.format(list(self))

#::::::::Exceptions and Errors :::::::::::

#errors have mros
def Errors():
    print("indexerror: ",IndexError.mro())
    print("keyerror: ",IndexError.mro())

    num = 5
    if type(num) != int:
        raise ValueError("Not a int!")
    
    assert num > 1, "The condition was false."

#custom exception
class TriangleError(Exception):
    def __init__(self,text,sides):
        super().__init__(text)
        self._sides = tuple(sides)
    @property
    def sides(self):
        return self._sides
    def __str__(self):
        return "'{}' for sides {}".format(self.args[0],self._sides)
    def __repr__(self):
        return "TriangleError({!r},{!r}".format(self.args[0],self._sides) + ")"

#:::::CONTEXT MANAGERS:::::
class LoggingContextManager:
    def __enter__(self):
        return "__enter__"
    def __exit__(self,exc_type,exc_val,exc_tb): #return None if it does not end exceptionally
    #exception type, exception object, exception traceback
        if exc_type is None:
            print("no problemos bro")    
        else:
            print("big problem bro")
            print("Type = ", exc_type)
            print("Val = ",exc_val)
            print("TB = ",exc_tb)
            #if you dont return anything, it returns None which == False 
            #which instructs the with statement to propogate exceptions

def testContextManager():
    with LoggingContextManager() as x:
        print(x)
    
    #multiple context managers (all of the below are the same)
    #with cm1() as a, cm2() as b:

    #with cm1() as a,\
    #     cm2() as b:

    '''
    with cm1() as a:
        with cm2() as b:
    '''
