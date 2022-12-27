def read_file():
    f = open('/Users/dtmac/Desktop/IT_109/lab_assignment/IT109_Lab9_input.txt', 'r')
    lines = f.read()
    print( lines )
    f.close()
read_file()


while True:
    d = input("Choose Which file to open: 'books','clothing','electronics'. Or press 'q' to quit the program:  ")
    if not d:
        continue
    
    if d == 'books':
        def read_bfile():
            b = open('/Users/dtmac/Desktop/IT_109/lab_assignment/books.txt', 'r')
            lines = b.read()
            print( lines )
            b.close()
        read_bfile()
    
    if d == 'clothing':
        def read_cfile():
            c = open('/Users/dtmac/Desktop/IT_109/lab_assignment/clothing.txt', 'r')
            lines = c.read()
            print( lines )
            c.close()
        read_cfile()
    
    if d == 'electronics':
        def read_efile():
            e = open('/Users/dtmac/Desktop/IT_109/lab_assignment/electronics.txt', 'r')
            lines = e.read()
            print( lines )
            e.close()
        read_efile()
    
    if d == 'q':
        break