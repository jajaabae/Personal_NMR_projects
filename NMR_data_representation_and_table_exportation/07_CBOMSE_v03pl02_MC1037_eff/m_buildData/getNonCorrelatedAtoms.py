def getNonCorrelatedAtoms(atoms, allConnections):
    redundantAtoms = []
    for a in atoms:
        haveConnection = False
        for connect in allConnections:
            if a in connect:
                #print connect
                haveConnection=True
        if not haveConnection:
            redundantAtoms += [a]
            #print a
    return redundantAtoms
