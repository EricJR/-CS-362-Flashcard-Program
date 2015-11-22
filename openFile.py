#Takes in THREEE arguments, the ./project1.py python script and the
#"inputname.txt" which includes the source code we want to read
#-----------------
if len(sys.argv) != 2:
    print('USEAGE: ./project1.py <inputname.txt>')
    exit(1)
if os.path.isfile(sys.argv[1]):
    pass
else:
    print('ERROR: File does not exist. Usage ./project1.py <inputname.txt>')
    exit(1)
#-----------------

#Assigns files to appropriate variables  
#-----------------
inputfile = sys.argv[1]
outputfile = sys.argv[2]
#-----------------

#Opens the files to be read / written to
infile = open(inputfile, 'r')
sys.stdout = open(outputfile, 'w')
