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