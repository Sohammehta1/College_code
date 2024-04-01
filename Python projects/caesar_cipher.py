
text = '''
   _____                             _____ _       _               
  / ____|                           / ____(_)     | |              
 | |     ___  __ _ ___  __ _ _ __  | |     _ _ __ | |__   ___ _ __ 
 | |    / _ \/ _` / __|/ _` | '__| | |    | | '_ \| '_ \ / _ \ '__|
 | |___|  __/ (_| \__ \ (_| | |    | |____| | |_) | | | |  __/ |   
  \_____\___|\__,_|___/\__,_|_|     \_____|_| .__/|_| |_|\___|_|   
                                            | |                    
                                            |_|                  
'''
print(text)
def generate_letters()-> list:
    letters = []
    c= 'a'
    for i in range(26):
        letters.append(c)
        c = chr(ord(c)+1)
    return letters

letters = generate_letters()

def ceaserCipher(plain_text, offset,encrypt = 1):
    chars = [_ for _ in plain_text]
    offset = offset%26
    if encrypt:
        chars = [letters[(letters.index(c) +offset)%26] for c in chars]
    else:
        chars = [letters[(letters.index(c) +26-offset)%26] for c in chars]
    string = ''.join(chars)
    print(string)    



ceaserCipher('abc',27,encrypt=0)