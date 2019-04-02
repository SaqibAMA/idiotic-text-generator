cap = ['a', 'c', 'e', 'g', 'h', 'j', 'l', 'o', 'q', 'r', 's', 'u', 'w', 'y']

print("::WELCOME TO IDIOTIC TEXT GENERATOR::")
print("::KEEP ON TYPING OR ENTER . TO EXIT")

def idiotize(str):
    str = str.lower()
    idioticStr = ''
    for c in str:
        
        if c in cap:
            idioticStr += c.upper()
        else:
            idioticStr += c
    
    return idioticStr

while True:
    line = input("Enter non-idiotic text: ")
    print(idiotize(line))
    if line == '.':
        print("Quitting program...")
        break
