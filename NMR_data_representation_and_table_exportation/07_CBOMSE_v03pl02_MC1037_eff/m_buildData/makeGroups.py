def makeGroups(prelimBonds, Bonds, Hydrogens, Carbons, assignGroup):
    iteration=1
    
    groups = {}
    for H in Hydrogens:
        groups[H]=-1
    for C in Carbons:
        groups[C]=-1
    for atom in groups:
        [groups, iterate] = assignGroup(atom, groups, iteration, prelimBonds, Bonds)
        if iterate:
            iteration += 1
    return groups
