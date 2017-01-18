def renameAtoms(HPrefix, CPrefix, Hydrogens, Carbons, correlations):
    Hs = Hydrogens
    for e, H in enumerate(Hs):
        Hydrogens[e] = HPrefix+H
    Cs = Carbons
    for e, C in enumerate(Cs):
        Carbons[e] = CPrefix+C
    cors = correlations
    for e, Cor in enumerate(cors):
        if Cor[2]=='c' or Cor[2]=='COSY':
            #Cor = [HPrefix+Cor[0], HPrefix+Cor[1], Cor[2]]
            Cor = [HPrefix+Cor[0], HPrefix+Cor[1], 'c']
        elif Cor[2]=='q' or Cor[2]=='HSQC':
            #Cor = [HPrefix+Cor[0], CPrefix+Cor[1], Cor[2]]
            Cor = [HPrefix+Cor[0], CPrefix+Cor[1], 'q']
        elif Cor[2]=='t' or Cor[2]=='TOCSY':
            #Cor = [HPrefix+Cor[0], HPrefix+Cor[1], Cor[2]]
            Cor = [HPrefix+Cor[0], HPrefix+Cor[1], 't']
        elif Cor[2]=='m' or Cor[2]=='HMBC':
            #Cor = [HPrefix+Cor[0], HPrefix+Cor[1], Cor[2]]
            Cor = [HPrefix+Cor[0], CPrefix+Cor[1], 'm']
            #print 'CPrefix', CPrefix
            #print 'HPrefix', HPrefix
        elif Cor[2]=='r' or Cor[2]=='ROESY':
            #Cor = [HPrefix+Cor[0], HPrefix+Cor[1], Cor[2]]
            Cor = [HPrefix+Cor[0], HPrefix+Cor[1], 'r']
        #print Cor
        correlations[e] = Cor
    #print correlations #tmp
    return correlations
