print('''Machine code is read in bytes, that is in groups of 8.
Therefore, it is advised to type machine code in groups of 8. Support for spaces is added for user convenience.
For example: '01100001 01100010' will be read same as '0110000101100010'.
If length of code is not a multiple of 8, zeros will be added in front of code to achieve the same.
If text file is used as input, it should contain only 0's and 1's.\n
Machine code will be stored in an output file.''')

while True:
    i = input("\nEnter 'r' to read binary text from a .txt file.\nType 'exit' to exit the program.\nEnter Machine Code (0's and 1's):\n")
    i = i.replace(' ', '')
    
    if i == 'exit':
        break
    
    if i == 'r':
        file = input('\nEnter textfile name: ')
        if not file.endswith('.txt'):
            file += '.txt'
        
        try:
            with open(file, 'r') as f:
                i = f.read()
        except:
            print('\nFile Not Found')
            continue
    
    zeros = 8 - len(i)%8
    if zeros == 8:
        zeros = 0
    
    b = '0'*zeros + i
    del(i)
    
    
    barray = bytearray()
    try:
        for i in range(0, len(b), 8):
            byte = b[i:i+8]
            barray.append(int(byte, 2))
    
    except:
        print('\nInvaild Input')
        continue
    
      
    binary = bytes(barray)   
    
    name = input('\nEnter output file name (Enter "0" to type code again):\n')
    if name == '0':
        print('\n')
        continue
    
    try:
        with open(name, 'wb') as f:
            f.write(binary)
            print('\nOutput file generated successfully...')
            continue
    except:
        print('\nInvaild Filename')
        continue