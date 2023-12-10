def verifye() :
    modpas = input('Antre yon modpas : ')
    while not modpas :
        modpas = input('Tanpri antre yon modpas : ')
        
    if len(modpas) < 7 :
        print('Motpass lan two kout, li dwe rive nan 7 karakte')
    else :
        m = False
        d = False
        s = False
        
        for karakte in modpas :
            if karakte.isupper() :
                m = True
            if karakte.isdigit() :
                d = True
            if not karakte.isalpha() and not karakte.isdigit() :
                s = True
            
        if not m :
            print('Motpass lan dwe gen karakte majiskil ladan l')
            return False
        elif not d :
            print('Motpass lan dwe gen dijit ladan l')
            return False
        elif not s :
            print('Motpass lan dwe gen karakte spesyal ladan l')
            return False
        else :
            return True
         
test = verifye()
while not test :
    test = verifye()

print('Modpass ou an korek')

