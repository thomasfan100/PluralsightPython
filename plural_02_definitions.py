import decimal
from decimal import Decimal
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
 