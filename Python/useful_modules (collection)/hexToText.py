'''
Pass a string containing hexes of characters you want to print seperated using semicolon(;)
into hexToText function.

Put the strings you want to print without hex conversion in square brackets.
You can put square brackets in square brackets to print them.
You can put a semicolon(;) in square brackets to print it.

This function can be used to get text of any language from its unicode
using only a english keyboard. Eg - Hindi, Japanese etc.
'''

def hexToText(hexes: str):
    hexes = hexes.strip()
    text = ""
    last = 0
    
    while(True):
        try:
            if hexes.strip().startswith('['):
                for i, c in enumerate(hexes):
                    if c == ']':
                        for x in hexes[i+1:]:
                            if not(x == ";" or x == ' '):
                                end = 0
                                break
                            elif x == ";":
                                end = 1
                                break
                        else:
                            end = 1
                            
                        if end:
                            hex = hexes[:i+1].strip()
                            hexes = hexes[i+1:][hexes[i+1:].index(';')+1:]
                            break

                else:
                    return "ERROR: Square bracket not closed"
            else:
                hex = hexes[:hexes.index(';')].strip()
                hexes = hexes[hexes.index(';')+1:]
                
        except ValueError:
            hex = hexes.strip()
            last = 1
            
          
        if hex.startswith("[") and hex.endswith("]"):
                text += hex[1:-1]
            
        else:
            try:
                text += chr(int(hex, 16))
            except ValueError:
                pass
            
        if last == 1:
            break
    
    return text
            
if __name__ == '__main__':
    print(hexToText("31; 62 ;[ 62];[ []]; [; ]; [Hex;]; [[]]"))