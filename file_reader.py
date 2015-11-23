import re
import sys

def main():

    infile, outfile = "text.txt", "text.txt"
    file_lines = []
    RE_lines = []
    
    with open(infile) as ifh:
        for line in ifh:
            file_lines.append(line)
            
    pattern = re.compile(r"@|~")
    
    for line in file_lines:
        RE_lines.append(pattern.split(line))
        
    for line in RE_lines:
        if line[0] == '':
            

if __name__ == "__main__":
    main()
