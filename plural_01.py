import sys
from pprint import pprint as pp
def built_in_collections():
    #strings
    print(":::STRINGS:::")
    len("abcdef")
    strings = ';'.join(['#one','#two','#three','#four'])
    strings.split(';')
    "athomasfan".partition('thomas')
    print("The age of {0} is {1}".format('Thomas', 21))
    long_string = "abcdefg" \
                  "hijklmnop"\
                  "qrstuv"\
                  "wxyz"
    print(long_string)
    
    major = "Computer Science"
    print(f"Thomas majors in {major}")

    #range and enumerate
    print(":::RANGE and ENUMERATION:::")
    rande = [6, 363, 6363, 36363, 636363]
    for r in range(len(rande)):
        print(rande[r])
    
    for e in enumerate(rande):
        #constructs (index, value) tuples
        print(e)

    for i,v in enumerate(rande):
        print(f"i = {i}, v = {v}")
    
    #tuple - immutable, unreplaceable, unremovable
    print(":::TUPLES:::")
    t = ("Norway", 4.953,3)
    t = t*3
    t1 = (391,)
    t2 = ()
    t_a = 'jelly'
    t_b = 'bean'
    t_a,t_b = t_b, t_a 
    print(t_b, " ",t_a)

    #list
    print(":::LISTS:::")
    l = [1, 2, 3, 4, 5, 6, 7]
    l2 = list(l)
    l[2] = 33
    print(l, "  ",l2) #shallow copy: new list with same obj reference
                      # but dont copy reffered-to objects
    i = l.index(5)
    4 in l
    5 not in l
    del l[0] #remove by position
    l.remove(2) #remove by element

    #dict - shallow copying, copying only the reference to the key and 
    #       value objects, not the objects themselves
    print(":::DICT:::")
    url = {
        "google" : "www.google.com",
        "ebay" : "www.ebay.com",
        "microsoft" : "www.microsoft.com"
    }
    url["google"] #access an element
    url ["amazon"] = "www.amazon.com" #add an element
    del url["google"] #delete an element
    dict(a = 'alfa' , b = 'bravo', c = 'charlie', d = 'delta')
    for key in url:
        print(f"{key} => {url[key]}")
    for key,value in url.items():
        # url.keys() url.values() also exists
        print(f"{key} => {value}")
    
    #set = unordered, unique elements, mutable, elements inside are immutable
    #useful for set algebra: union, difference, intersection,subset, superset, disjoint
    print(":::SETS:::")
    s = {6,24,30,36}
    s2 = set()
    temp_list = [1,1,1,2,2,2,3,3,3,4,4,4,5]
    s3 = set(temp_list)
    s.add(42)
    s.update([48,54,60]) #adding multiple
    s.discard(6) #not as fussy as remove
    s.remove(24) #will be fussy if 24 does not exist
    print(s.union(s3))
    
def encode_decode():
    bytecode = "abcdefghijklmnop"
    encoded = bytecode.encode('utf8')
    decoded = encoded.decode('utf8')

def iterables():
    print(":::ITERABLES:::")
    #list comprehension
    words = ["johnny", "tommy", "elfy"]
    lengths = [len(word) for word in words] 
    """
    lengths = []
    for word in words:
        lengths.append(len(word))
    """
    
    #dictionary comprehension
    country_to_capital = { 'United Kingdom' :'London',
                           'Brazil': 'Brasilia',
                           'Morocco' : 'Rabat',
                           'Sweden' : 'Stockholm' }
    capital_to_country = {capital:country for country,capital in country_to_capital.items()}
    pp(capital_to_country)

    words2 = {x[0]:x*3 for x in words if len(x) > 4} #filtering a comprehension
    pp(words2)

    #iterable
    iterable = ['Spring','Summer', 'Autumn', 'Winter']
    iterator = iter(iterable)
    next(iterator) 

def generator(count, iterable):
    #good for infinite sequences like sensor readings and must include one yield statement
    #are python iterators, you can call next(g) on a generator object g
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item

def distinct_generator(iterable):
    #generators are lazy, computation only happen just in time when the next result is requested
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)

    #example generator expression : single use objects
    # million_squares = (x*x for x in range(1,1000001))
    # sum(x*x for x in range(1,1000001))
def convert(s):
    """
        Convert a string to an integer. Five Six = 56
        Can handle a KeyError. Ex: "eleventeen".split()
        Can handle a TypeError. Ex: 156
    """
    print(":::EXCEPTIONS:::")
    DIGIT_MAP = {
        'zero' : '0',
        'one' : '1',
        'two' : '2',
        'three' : '3',
        'four' : '4',
        'five' : '5',
        'six' : '6',
        'seven' : '7',
        'eight' : '8',
        'nine' : '9',
    }
    if not isinstance(s, list):
        raise TypeError("Argument must be a list")

    try:
        number = ''
        for token in s:
            number += DIGIT_MAP[token]
        return int(number)
    except (KeyError, TypeError) as e:
        print(f"Conversion error: {e!r}", 
              file=sys.stderr)
        raise #reraises exception that is being currently handled

def fileio():
    #mode r(read) w(write) a(appending) + b(binary mode) t (text mode)    
    f = open('wasteland.txt', mode = 'wt', encoding = 'utf-8')
    f.write('Whats up\n')
    f.close()

    g = open('wasteland.txt', mode='rt' , encoding='utf-8')
    print(g.read())
    g.seek(0)
    print(g.readline())
    g.close()

    h = open('wasteland.txt', mode = 'at' , encoding='utf-8')
    h.writelines(
         ['Son of man, \n',
          'You cannot say, or guess,',
          'for you know only, \n',
          'A heap of broken images, ',
          'where the sun beats\n'])
    h.close()

    #finally
    try:
        i = open('wasteland.txt', mode='rt', encoding= 'utf-8')
        for line in i:
            sys.stdout.write(line)
    finally:
         i.close()

    #with-blocks ensure that file is closed
    with open('wasteland.txt', mode='at', encoding= 'utf-8') as j:
        j.writelines("My Name is Jeff")


def main():
    #built_in_collections()
    #print(convert("five six".split()))
    #iterables()
    '''
    items = [3,6,6,2,1,1]
    for items in generator(3, distinct_generator(items)):
        print(items)
    '''
    #fileio()
if __name__ == "__main__":
    main()
    