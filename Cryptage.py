
###### SUBSTITUTION ######
def subsitution_crpyt(text, key):

    alph = "abcdefghijklmnopqrstuvwxyz0123456789 "
    crypt = ""
    text = text.lower()

    for c in text : 
        crypt += key[alph.index(c)]

    return crypt

def substitution_decrypt(encrypted_text, key):

    alph = "abcdefghijklmnopqrstuvwxyz0123456789 "
    decrypt =""
    encrypted_text = encrypted_text.lower()

    for c in encrypted_text :
        decrypt += alph[key.index(c)]
    
    return decrypt


###### DECALAGE ######

def decalage_crypt(text, key):

    text = text.lower()
    alph = "abcdefghijklmnopqrstuvwxyz0123456789 "
    crypt = ""

    for c in text :
        crypt += alph[(alph.index(c)+key)%(len(alph)-1)]

    return crypt

def decalage_decrypt(encrypted_text, key):

    encrypted_text = encrypted_text.lower()
    alph = "abcdefghijklmnopqrstuvwxyz0123456789 "
    decrypt = ""

    for c in encrypted_text:
        decrypt += alph[alph.index(c)-key]
    
    return decrypt


###### SCYTALE ######


def scytale_crypt(text, key):
    l= []
    text = text.lower()

    #Ajout d'élements manquants pour avoir le meme nombre d'elements dans chaque liste formée
    if (len(text))%key != 0 :
        text += ((len(text))%key)*"ϡ"
    
    listed_text = list(text)

    for i in range (key):
        l_temp = []
        for j in range (0,len(listed_text)-1,(len(listed_text)//key)-1):
            l_temp.append(listed_text[i+j])
        l.append(l_temp)
    return l

scytale = [['h', 'l', 'w', 'l'], ['e', 'o', 'o', 'd'], ['l', ' ', 'r', 'ϡ']]

def scytale_decrypt(list, key):
    dec_text = ""
    for i in range (len(list[0])):
        for j in range (key):
            if list[j][i] != 'ϡ' :
                dec_text += list[j][i]
            else :
                continue
    return dec_text


print(scytale_decrypt(scytale, 3))

