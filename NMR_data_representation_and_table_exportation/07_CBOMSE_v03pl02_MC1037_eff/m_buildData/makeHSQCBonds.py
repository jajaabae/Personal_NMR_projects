def makeHSQCBonds(correlations, Bonds):
    for cor in correlations:
        #print cor
        if cor[2]=='q':
            #Bonds.append([cor[0], cor[1]])
            Bonds.append([cor[0], cor[1], cor[2]])
