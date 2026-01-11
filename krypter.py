#Imprterer 'sys' for å kunne la brukeren skrive tekst og antall samtidig de åpner filen via terminalen på systemet.
import sys


#FUNKSJONER

#Oppretter en funksjon som krypterer teksten til brukeren.
def caesar_encrypt(tekst, antall):
    resultat = '' #Variabel 'resultat' som skal lagre alle verdiene/tegnene som kommer av for-loopen under.

    for char in tekst: #Utfører en for-loop, som gjentar koden i seg for alle tegnene i strengen som er lagret i funksjonens variabel 'tekst'.
        char = char.upper() #Gjør alle bokstaver om til store bokstaver.
        if not char == ' ': #Hopper over alle mellomrom som befinner seg i teksten.
            char_index = alfabet.find(char) #Finner indexen til tegnet i vairabelen 'alfabet' som er lik 'char', og lagrer denne verdien i variabelen 'char_index'.
            if char_index == -1: #Om ikke tenget kan bli funnet i variabelen 'alfabet', vil indexen bli -1.
                resultat += char #Legger til tegnet 'char' i variabelen 'resultat'
            else: #Om indexen ikke er -1, som vil si at tegnet finnes i variabelen 'alfabet', kjøres koden under istedenfor.
                ny_char_index = char_index + antall #Legger sammen verdiene lagret i variablene 'char_index' og 'antall', og lagrer denne verdien i variabelen 'ny_char_index'.
                while ny_char_index >= tegn_i_alfabet: #Kjører en while-loop, som her kjører koden i seg så lenge verdien i 'ny_char_index' er større enn eller lik 'tegn_i_alfabet'. Dette blir gjort, siden variabelen 'alfabet' kun har indexverdier fra 0 med 'A' til og med 28 med 'Å'.
                    ny_char_index -= tegn_i_alfabet #Trekker verdien lagret i variabelen 'tegn_i_alfabet' fra variabelen 'ny_char_index', og lagrer verdien i variabelen 'ny_char_index'.
                resultat += alfabet[ny_char_index] #Leter etter tegnet i variabelen 'alfabet' med index som har den samme verdien lagret i variabelen 'ny_char_index'. Dette tegnet blir lagt til i variabelen 'resultat'
    return resultat #Returnerer det som er lagret i variabelen 'resultat' til hovedkoden og fortsetter koden.

#Oppretter en funksjon som dekrypterer teksten til brukeren. Samme funksjon som den forrige, med noen endringer. Kun de linjene som er endret for å dekryptere er kommentert.
def caesar_decrypt(kryptert_tekst, antall):
    resultat = ''

    for char in kryptert_tekst:
        char = char.upper()
        if not char == ' ':
            char_index = alfabet.find(char)
            if char_index == -1:
                resultat += char
            else:
                ny_char_index = char_index - antall #Trekker verdien lagret i variablen 'antall' fra verdien lagret i variabelen lagret i 'char_index', og lagrer denne verdien i variabelen 'ny_char_index'.
                while ny_char_index < 0: #Kjører en while-loop, som her kjører koden i seg så lenge verdien i 'ny_char_index' er mindere enn 0. Dette blir gjort, siden variabelen 'alfabet' kun har indexverdier fra 0 med 'A' til og med 28 med 'Å'.
                    ny_char_index += tegn_i_alfabet #Legger sammen verdien lagret i variabelen 'tegn_i_alfabet' med variabelen 'ny_char_index', og lagrer verdien i variabelen 'ny_char_index'.
                resultat += alfabet[ny_char_index]
    return resultat


#HOVEDKODE

alfabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÆØÅ' #Variabelen 'alfabet' med en streng med alle bokstavene i det norske alfabetet.
tegn_i_alfabet = len(alfabet) #Variabelen 'tegn_i_alfabet' med et heltall med antall tegn som er i strengen lagret i variabelen 'alfabet'.

print('Åpner ' + sys.argv[0], end='\n\n') #'sys.argv[0]' er navnet til filen.
tekst = sys.argv[1] #'sys.argv[1]' er den første inputen til brukeren, hvor alt mellom 2 anførselstegn regnes som en input. Dette lagres i variabelen 'tekst'.
antall = int(sys.argv[2]) #'sys.argv[2]' er den andre inputen til brukeren, som er etter et mellomrom etter den første inputen. Dette lagres i variabelen 'antall'.
#I terminalen skriver man 'python [filplassering]\krypter.py "[tekst]" [antall]'

'''
tekst = input('Skriv inn en tekst som skal krypteres: ') #Spør brukeren om å skrive inn en tekst, som blir lagret i variabelen 'tekst'.

while True: #En while-loop som kjører uendelig.
    try: #Try-except blir brukt for å forsikre at brukeren skriver inn et heltall.
        antall = int(input('Skriv antall (i heltall) bokstaver som skal forsyves i teksten: ')) #Spør om et heltall fra bruker. Denne verdien lagres i variabelen 'antall'.
        print() #Skriver en tom linje.
        break #Hopper ut av while-loopen om et heltall blir skrevet.
    except ValueError: #Om en ValueError oppstår, altså om brukeren ikke skriver inn et heltall, kjøres koden under.
        print('Du skrev ikke inn et heltall, prøv igjen.\n') #Gir en beskjed til brukeren, oppretter en ny linje, så gjentar loopen.
'''

kryptert_tekst = caesar_encrypt(tekst, antall) #Sender hva som er lagret i variablene 'tekst' og 'antall' til funksjonen 'caesar_encrypt', og lagrer det som blir returnert i variabelen 'kryptert_tekst'.
dekryptert_tekst = caesar_decrypt(kryptert_tekst, antall) #Sender hva som er lagret i variablene 'kryptert_tekst' og 'antall' til funksjonen 'caesar_decrypt', og lagrer det som blir returnert i variabelen 'dekryptert_tekst'.
print('Kryptert tekst:', kryptert_tekst) #Skriver en tekst som inkluderer verdien/strengen som er lagret i variabelen 'kryptert_tekst' til brukeren.
print('Dekryptert tekst fra kryptert tekst:', dekryptert_tekst) #Skriver en tekst som inkluderer verdien/strengen som er lagret i variabelen 'dekryptert_tekst' til brukeren.
