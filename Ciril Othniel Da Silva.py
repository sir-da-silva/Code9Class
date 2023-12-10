def verifye() :
    modpas = input('Antre yon modpas : ')
    while not modpas :
        modpas = input('Tanpri antre yon modpas : ')
        
    if len(modpas) < 7 :
        print('Motpass lan two kout, li dwe rive nan 7 karakte')
    else :
        testMajiskil = False
        testDijit = False
        testSpesyal = False
        
        for karakte in modpas :
            if karakte.isupper() :
                testMajiskil = True
            if karakte.isdigit() :
                testDijit = True
            if not karakte.isalpha() and not karakte.isdigit() :
                testSpesyal = True

        if not testMajiskil :
            print('Motpass lan dwe gen karakte majiskil ladan l')
            return False
        if not testDijit :
            print('Motpass lan dwe gen dijit ladan l')
            return False
        if not testSpesyal :
            print('Motpass lan dwe gen karakte spesyal ladan l')
            return False
        
        return True

while not verifye() :
    verifye()

print('Modpass ou an korek')

