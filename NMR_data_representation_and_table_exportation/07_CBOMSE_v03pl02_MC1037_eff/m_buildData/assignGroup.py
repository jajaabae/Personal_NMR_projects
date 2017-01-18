def assignGroup(atom, groups, iteration, prelimBonds, Bonds):
    global onceMore
    iterate=False
    if atom in groups and groups[atom]==-1:
        allBonds = prelimBonds+Bonds
        for b in allBonds:
            if atom in b:
                groups[atom]=iteration
                for pos in b[0:2]:
                    if not atom==pos:
                        iterate=True
                        assignGroup(pos, groups, iteration, prelimBonds, Bonds)
    return groups, iterate
