def dekripte () :
    kod = input('Antre yon kòd : ')
    while not kod :
        kod = input('Antre yon kòd : ')

    let = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    rezilta = ''

    # verifikasyon
    for pati, sekans in enumerate(kod.split()) :
        ere = f"Pati {pati+1} nan kòd ou an pa korek, tanpri reeseye"

        if sekans == 'quit' :
            global stop; stop = False
            print('Bye ! Mèsi dèske ou te itilize pwogram nou an')
            return
        elif not sekans[0] in '<>' :
            print(ere)
            return
        elif not sekans[1:-1].isdigit() :
            print(ere)
            return
        elif not sekans[-1].isalpha() :
            print(ere)
            return
        elif not sekans[-1].upper() in let :
            print(ere)
            return

        for e, v in enumerate(let) :
            if sekans[-1].upper() == v and sekans[0] == '<' and int(sekans[1:-1]) > e :
                print(ere)
                return
            elif sekans[-1].upper() == v and sekans[0] == '>' and (int(sekans[1:-1]) + e) > 25 :
                print(ere)
                return
            
            # dekriptaj
            elif sekans[-1].upper() == v and sekans[0] == '<' :
                rezilta += let[e - int(sekans[1:-1])]
            elif sekans[-1].upper() == v and sekans[0] == '>' :
                rezilta += let[e + int(sekans[1:-1])]

    print(f"Rezilta : '{rezilta}'")          
    
print('Byenvini nan program dekripte kòd nou an,')
print('antre yon kòd pou dekripte oubyen')
print('si ou vle kanpe pwogram nan antre \'quit\'')
print()

stop = True
while stop :
    dekripte()
    
# -----------------------------------------------
# bèl egzèsis :-) !
