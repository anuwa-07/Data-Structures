
# HASH MAP || HASH TABLE
> Hash Map are use for fast searching.

    liner_search - O(n)
    Binary Search - O(log n )
    HashMap - O(1)


# Short Summary on HashMap AKA HashTable
    When insert on hash-table we get the position for that element by the size of that element. 
    HashTables will not allowed to have duplicate records.

# Drowbacks of HashTables
    It require more memory space.

# Mapping
    For mapping we use hash functions. 
        - One to One ( Ideal hashing ) - h(x) = x
        - Many to One - h(x) = x mod 10
        these types time complexcity is O(1)
    
    Ideal hasing will require more memory space to store the values.
    There for we use "Many to One" hasing func.
        But Many to One will come with "COLLISION"

# Avoid Collision 
    We have two options for that, 

    - Open Hashing ( Will require extra space )
        - Chaning

    - Close Hasing ( Size of the hash table will not increase )
        - Linear Probing
        - Quadratic Probing
        - Double Probing 

    
# CHANIING ( Open Hasing )
    Each index in HashTable will keep a List or Linked-list. 
    There for when we getting multiple records for same index, we can append those to list.
    When appending, make sure to sort values. This will helpful when searching.

    TIME COMPLEXCITY
    n = 100 ( number of values )
    size = 10 ( len of the hash-tree )
    
    loading factor ( /| )  = n / size ( 100/10 )
    
    Average successful search:
        t = 1 + (lf)/2
    
    Average unsucessful search:
        t = 1 + lf

    DELETE FOR HASHTABLE
    1. Use hash fuc to get index
    2. Search Index
    3. Delete value for the List or Linked-List


# LINEAR PROBING ( Close Hasing )
    h'(x) = ( h(x) + f(i) ) mod 10 
        where f(i) = i and i = {0, 1, 2, 3, 4 ..... n}

    to find the index for element to store in hash-table, we can use h'(x) func. 
    Where h(x) is the Hash-Function, which is define by the programmer.
    
    Same for when searcing.
        Use h'(x) function for serching. If value not found keep trying by increasing the "i"
    
    Search need to be stop when
        - When element is found
        - When you got a space ( None ) when searching by increasing the "i"

    DELETE FORM LINER PROBING
        Deleaction is not recomend in Linear probing. 
        Which require more oprating to process after element delete. 
        There for you can keep a status to get know, this element was deleated.

    ANALIZE ----------------------
    
        h'(x) = ( h(x) + f(i) ) mod 10
        
        lf ( loading factor )
        lf = n / size
        
        *** For Linear probing. "lf" always need to get value small that 0.5 
            lf =< 0.5 - there for every time hash-table must len 2x thant the total count of elements.
        
    ** Average successful search:
        t = 1/lf ln(1/lf-1)
    
    ** Average unsucessful search:
        t = 1/1-lf


# QUDRATIC PROBING ( Close Hasing )
    h'(x) = ( h(x) + f(i) ) mod 10
        where f(i) = i and i = {0x0, 1x1, 2x2, 3x3, 4x4 ..... nxn}

    10 - size of hash-table
    h(x) - hash function define by programmer

    Searching, Deleations, Insert same as LINEAR PROBING.

# DOUBLE HASING ( Close Hasing )
    We will use two functions to get location and search.
    
    01. h1(x) = x mod 10 ( hash func - define by programmer ) here 10 is size of hash-table.
    02. h2(x) = R(x mode R) ( R - will be the largest prime number location in Hash-Tree )
    
    h'(x) = h1(x) + i(h2(x)) mode 10
        where i = {0, 1, 2, 3, 4 .... n}
    


# HashMap using python.
Python "dict" is an Inbulid hashmap. But there are some drawbacks in python dict.
Main one is Collism. 


    