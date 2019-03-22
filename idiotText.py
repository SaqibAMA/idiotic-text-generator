cap = ['a', 'c', 'e', 'g', 'h', 'j', 'l', 'o', 'q', 'r', 's', 'u', 'w', 'y']

print("::WELCOME TO IDIOTIC TEXT GENERATOR::")

line = input("Enter non-idiotic text: ")

def idiotize(str):
    str = str.lower()
    idioticStr = ''
    for c in str:
        
        if c in cap:
            idioticStr += c.upper()
        else:
            idioticStr += c
    
    return idioticStr

print(idiotize(line))
exit = input("PRESS ENTER TO EXIT")