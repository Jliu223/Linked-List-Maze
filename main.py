#John Liu, jl4582
#Justyn Ngo, jmn365
#Karan Rai, kr3287

from birthday import Birthday

def getFileName():
    '''
    Purpose: get the correct name for the file you want to open (bdaylist.txt)
    Parameters: None
    Return: None
    Sample call: filename = getFileName()
    '''
    while True:
        #get the user input for the file name, run again if the file is not found 
        filename = input("Enter the name of the data file: ")
        try:
            with open(filename, 'r'):
                return filename
        except FileNotFoundError:
            print(f"File {filename} does not exist. Please try again.")

def readBirthdays(filename):
    '''
    Purpose: open the file, read the lines, and then close the file
    Paramaters: filename
    Return: lines
    Sample call: lines = readBirthdays(filename)
    '''
    #open and close simultaneously with "with"
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines
    
if __name__ == '__main__':
    filename = getFileName()
    lines = readBirthdays(filename)
    
    #create empty hash table as a dictionary and create the 12 lists within the hash table 
    hash_table = {}
    for i in range(12):
        hash_table[i] = []
    line_number = 0
   
    #split month, day, and year, convert to integers, pass them into the Birthday object, use the hash function, and then append the birthday at that specific hash value bucket
    for line in lines:
        parts = line.strip().split("/")
        date = int(parts[0])
        month = int(parts[1])
        year = int(parts[2])
        birth_date = Birthday(date, month, year)
        hash_value = hash(birth_date)
        hash_table[hash_value].append((birth_date, line_number))
        line_number += 1
    
    #print all 12 locations and the number of elements in them 
    for i in range(12):
        print(f"Hash location {i} has {len(hash_table[i])} elements")
