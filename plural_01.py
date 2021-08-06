def built_in_collections():
    #strings
    print(":::STRINGS:::")
    len("abcdef")
    strings = ';'.join(['#one','#two','#three','#four'])
    strings.split(';')
    "athomasfan".partition('thomas')
    print("The age of {0} is {1}".format('Thomas', 21))
    
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
    print("temporary")
def exceptions():
    try:
        print(5/0)
    except:
        print("bad")

def main():
    #built_in_collections()
    exceptions()

if __name__ == "__main__":
    main()