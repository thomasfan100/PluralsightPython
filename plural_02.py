import plural_01

class BasicFunctions:
    def __call__(self, x = False): #define __call__ to make class instances callable
        #conditional expression
        print("ello boy... never hur somun lika you round hur") if x else print("yousa not fromaround hur")

        #lambdas
        lamb = lambda l: print(l+5+500)
        lamb(50)
        lamb2 = lambda: 5 % 2 == 1

        
def callableClass():
    return BasicFunctions() #returns a class object

def main():
    
    me_callable = BasicFunctions()
    me_callable(True)
    print(callable(me_callable))
    ''' 
    cC = callableClass()
    cC()
    '''
if __name__ == "__main__":
    main()