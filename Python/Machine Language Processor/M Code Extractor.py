print('This program will save the Machine Code of any file in a txt file.\n')

while True:
    try:
        file = input('Enter file name: ')

        with open(file, 'rb') as f:
            b = f.read()
            break
    
    except:
        print('\nFile not found\n')
        continue

code = ''    
for byte in b:
    binary = bin(byte).replace('0b', '')
    if len(binary) != 8:
        zeros = 8 - len(binary)%8
        binary = '0'*zeros + binary
    
    code = code + binary
    
file = input('\nEnter output textfile name: ')

if not file.endswith('.txt'):
    file += '.txt'
    
with open(file, 'w') as f:
    f.write(code)
    